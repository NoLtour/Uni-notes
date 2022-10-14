
#define PULSE_PERIOD 14

#define DEBUG_LIGHT_PIN LED_BUILTIN

#define LIGHT_A_PIN 12
#define LIGHT_B_PIN 11
#define LIGHT_C_PIN 10


class Task;
class TaskManager;
unsigned long cycleTime = 0;


void pinPulse( long pin, float fraction, long totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  long onTime = (long) (PULSE_PERIOD*fraction);
  long offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(pin, HIGH);   
    delay(onTime);                       
    digitalWrite(pin, LOW);  
    delay(offTime);
  }
}

enum ErrorType{ GENERIC=1 };

void pinNumberPulse( long pin, long pulseCount ){
  pulseCount = pulseCount<0?0:pulseCount;

  for ( long i=0; i<pulseCount; i++ ){
    pinPulse( pin, 0, 120  );
    pinPulse( pin, 1, 30 );
    pinPulse( pin, 0, 120  );
  }
}

// highest is 4
void errorProtocol( long errorNumber=1 ){
  errorNumber = errorNumber<=0?1:errorNumber;

  for ( ;; ){
    pinPulse( DEBUG_LIGHT_PIN, 0, 3000 );

    pinNumberPulse( DEBUG_LIGHT_PIN, errorNumber );
  }
}

#define TASK_LOCAL_STORAGE_SIZE 8
 

class Task{
  public:
    long customStates [TASK_LOCAL_STORAGE_SIZE];

    Task(){
      reconstructTask( NULL, 0, 0, 0, 0 );
    }

    void reconstructTask( void (*nTaskFunction)( Task* ), long nRepeats, long nDelay, long nTmpExtraDelay, unsigned long forcedExecuteTime=1, long initCustomStates[TASK_LOCAL_STORAGE_SIZE]=NULL, unsigned long forceInitTime=0 ){
      taskFunction = nTaskFunction;
      repeats = nRepeats<0?-1:nRepeats;
      delay = nDelay<0?0:nDelay;
      executeTime = (forcedExecuteTime==1)?(cycleTime + delay):forcedExecuteTime;
      isCanceled = false;
      isExecuted = false;
      tmpExtraDelay = nTmpExtraDelay;

      initTime = forceInitTime==0?cycleTime:forceInitTime;

      if ( initCustomStates != NULL ){
        for ( long i=0; i<TASK_LOCAL_STORAGE_SIZE; i++ ){
          customStates[i] = initCustomStates[i];
        }
      }

      if ( delay == 0 ){
        execute();
      }
    }

    void addTmpExtraDelay( long extraDelay ){
      tmpExtraDelay += extraDelay;
    }

    void changeRelativeDelay( long microsecondDelay ){
      microsecondDelay = microsecondDelay<0?0:microsecondDelay;
      executeTime = cycleTime + microsecondDelay;
      delay = microsecondDelay;
    }

    unsigned long getInitTime(){
      return initTime;
    }

    /*void changeAbsoluteDelay( long millisecondDelay ){
      millisecondDelay = millisecondDelay<0?0:millisecondDelay;
      executeTime = (executeTime + millisecondDelay) - delay;
      delay = millisecondDelay;

      isExecuted = false;
    }*/

    void cancel(){
      isCanceled = true;
    }

    void copyFrom( Task * refrence ){
      reconstructTask(
        refrence->taskFunction,
        refrence->repeats,
        refrence->delay,
        refrence->tmpExtraDelay,
        refrence->executeTime,
        refrence->customStates,
        refrence->initTime
      );
    }

    bool checkCanceled(){
      return isCanceled;
    }

    bool canExecute(){
      return !( isCanceled || isExecuted );
    }

    bool checkExecuted(){
      return isExecuted;
    }

    void attemptRun(){
      if ( isCanceled ){
        errorProtocol( 2 );
      }
      
      if ( cycleTime >= executeTime+tmpExtraDelay ){
        executeTime += tmpExtraDelay;
        tmpExtraDelay = 0;
        execute();
      }
    }

  private:
    void (*taskFunction)( Task* );
    long repeats;
    long delay;
    long tmpExtraDelay;
    bool isCanceled;
    bool isExecuted;
    unsigned long executeTime;
    unsigned long initTime;
    
    void execute(){
      executeTime += (unsigned long) delay;

      if ( repeats == 0 ){
        isExecuted = true;
        return;
      }else{
        repeats--;
      }
      
      if ( taskFunction != NULL ){
        taskFunction( this );
      }
    }
}; 

#define MAX_TASKS 8



class TaskManager{
  public:
    TaskManager(){
       
    }

    void executeCycle(){
      bool didExecute = false;

      cycleTime = micros();

      for ( long i=0; i<tasks; i++ ){
        Task * cTask = &allTasks[i];

        if ( cTask->canExecute() ){
          didExecute = true;
          cTask->attemptRun();
        }else{
          deleteTask( i );
          i--;
        }

        digitalWrite(DEBUG_LIGHT_PIN, didExecute?HIGH:LOW );
      }
    }

    Task * addRepeatingTask( void (*nTaskFunction)( Task* ), long nDelay, long repeats, long startDelay=0 ){
      return addTask( nTaskFunction, repeats, nDelay, startDelay );
    }

    Task * addInfRepeatingTask( void (*nTaskFunction)( Task* ), long nDelay, long startDelay=0 ){
      return addTask( nTaskFunction, -1, nDelay, startDelay );
    }

    Task * addSingleTask( void (*nTaskFunction)( Task* ), long nDelay, long startDelay=0 ){
      return addTask( nTaskFunction, 1, nDelay, startDelay );
    }

    void deleteTask( long taskIndex ){
      if ( tasks <= 0 ){
        errorProtocol( 3 );
      }

      Task * delTask = &allTasks[taskIndex];
      delTask->cancel();

      //for ( long i=taskIndex; i<tasks-1; i++ ){
      //  allTasks[i].copyFrom( &(allTasks[i+1]) );
      //} 
      allTasks[taskIndex].copyFrom( &allTasks[tasks-1] );

      tasks--;
    }

  private:
    Task allTasks [MAX_TASKS];
    long tasks = 0; 

    Task * addTask( void (*nTaskFunction)( Task* ), long repeats, long nDelay, long startDelay ){
      if ( tasks == MAX_TASKS ){
        errorProtocol( 4 );
      }

      Task * cTask = &allTasks[ tasks ];
      cTask->reconstructTask(nTaskFunction, repeats, nDelay, startDelay );

      tasks++;

      return cTask;
    }
};

//DynList<long> Timez;

TaskManager taskManager = TaskManager();

void playFreqFunc( Task * asTask ){
  long pin = asTask->customStates[0];
  long isOn = asTask->customStates[1];

  if ( isOn == 1 ){
    digitalWrite(pin, LOW);
    asTask->customStates[1] = 0;
  }else{
    digitalWrite(pin, HIGH);
    asTask->customStates[1] = 1;
  }
}

void runPulseFunc( Task * thisTask ){
  bool isOn = (thisTask)->customStates[1] == 1;
  long pinNumber = (thisTask)->customStates[0];

  long  onLength = (thisTask)->customStates[2];
  long offLength = (thisTask)->customStates[3]; 


  if ( (isOn || onLength==0) && offLength != 0 ){
    (thisTask)->changeRelativeDelay( offLength );
    analogWrite( pinNumber, 0 );
    (thisTask)->customStates[1] = 0;
  }else{
    (thisTask)->customStates[4]--;
    (thisTask)->changeRelativeDelay( onLength );
    analogWrite( pinNumber, 255 );
    (thisTask)->customStates[1] = 1;
  }
}

// stored: pinNumber , on/off , onLength , offLength , repeatsLeft
void pulsePin( long pinNumber, long onLengthMicros, long offLengthMicros, long repeats, long startDelay ){
  Task * asTask = taskManager.addRepeatingTask( &runPulseFunc, onLengthMicros, repeats*2-1, startDelay );
  digitalWrite( pinNumber, HIGH );
  
  (asTask)->customStates[0] = pinNumber;
  (asTask)->customStates[1] = 1;
  (asTask)->customStates[2] = onLengthMicros;
  (asTask)->customStates[3] = offLengthMicros;
}

void playFreq( long pin, long frequency, long durationMillis ){

  //Task * asTask = taskManager.addRepeatingTask( &playFreqFunc, 500/frequency, (frequency*duration)/500 );

  //asTask->customStates[0] = pin;
  //asTask->customStates[1] = 0;
  long periodMicros = 1000000/frequency;

  pulsePin( pin, periodMicros/2, periodMicros/2, (durationMillis*1000)/periodMicros, 0 );

}

void changeSoundFunc( Task * asTask ){
  long freq = asTask->customStates[1];
  long pin = asTask->customStates[0];

  playFreq(pin, freq, 1000);

  if ( freq <= 0 ){
    //noTone( asTask->customStates[0] );
  }else{
    //tone( asTask->customStates[0], freq );
  }
  
}

void changeSound( long pin, long value, long repeatTime, long startDelay=0 ){
  Task * asTask = taskManager.addInfRepeatingTask( &changeSoundFunc, repeatTime*1000, startDelay*1000 );

  asTask->customStates[0] = pin;
  asTask->customStates[1] = value;
}

#define PIN_A 11 
#define PIN_B 10
#define PIN_C 9
#define PIN_D 6

void setup() {
  // put your setup code here, to run once:
  
  long repTime = 10000; 

  //playFreq( PIN_A, 1000, 2000000 );

  //pulsePin( PIN_A, 1000, 1000, 500, 0 );

  changeSound(PIN_A, 500, repTime, 0000);
  changeSound(PIN_B, 1000, repTime, 1000);
  changeSound(PIN_C, 2000, repTime, 2000);
  changeSound(PIN_D, 5000, repTime, 3000);
  //analogWrite(11, 100);
}

void loop() {
  
  taskManager.executeCycle();
  //analogWrite(PIN_A, millis()%50<25?50:10 );

}
