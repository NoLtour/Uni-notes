
#include <Servo.h>

#define PULSE_PERIOD 14

#define DEBUG_LIGHT_PIN LED_BUILTIN

#define LIGHT_A_PIN 12
#define LIGHT_B_PIN 11
#define LIGHT_C_PIN 10

class Task;
class TaskManager;
unsigned long cycleTime = 0;


void pinPulse( int pin, float fraction, int totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  int onTime = (int) (PULSE_PERIOD*fraction);
  int offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(pin, HIGH);   
    delay(onTime);                       
    digitalWrite(pin, LOW);  
    delay(offTime);
  }
}

enum ErrorType{ GENERIC=1 };

void pinNumberPulse( int pin, int pulseCount ){
  pulseCount = pulseCount<0?0:pulseCount;

  for ( int i=0; i<pulseCount; i++ ){
    pinPulse( pin, 0, 120  );
    pinPulse( pin, 1, 30 );
    pinPulse( pin, 0, 120  );
  }
}

// highest is 4
void errorProtocol( int errorNumber=1 ){
  errorNumber = errorNumber<=0?1:errorNumber;

  for ( ;; ){
    pinPulse( DEBUG_LIGHT_PIN, 0, 3000 );

    pinNumberPulse( DEBUG_LIGHT_PIN, errorNumber );
  }
}

#define TASK_LOCAL_STORAGE_SIZE 8
 

class Task{
  public:
    int customStates [TASK_LOCAL_STORAGE_SIZE];

    Task(){
      reconstructTask( NULL, 0, 0, 0, 0 );
    }

    void reconstructTask( void (*nTaskFunction)( Task* ), int nRepeats, int nDelay, int nTmpExtraDelay, unsigned long forcedExecuteTime=1, int initCustomStates[TASK_LOCAL_STORAGE_SIZE]=NULL, unsigned long forceInitTime=0 ){
      taskFunction = nTaskFunction;
      repeats = nRepeats<0?-1:nRepeats;
      delay = nDelay<0?0:nDelay;
      executeTime = (forcedExecuteTime==1)?(cycleTime + delay):forcedExecuteTime;
      isCanceled = false;
      isExecuted = false;
      tmpExtraDelay = nTmpExtraDelay;

      initTime = forceInitTime==0?cycleTime:forceInitTime;

      if ( initCustomStates != NULL ){
        for ( int i=0; i<TASK_LOCAL_STORAGE_SIZE; i++ ){
          customStates[i] = initCustomStates[i];
        }
      }

      if ( delay == 0 ){
        execute();
      }
    }

    void addTmpExtraDelay( int extraDelay ){
      tmpExtraDelay += extraDelay;
    }

    void changeRelativeDelay( int millisecondDelay ){
      millisecondDelay = millisecondDelay<0?0:millisecondDelay;
      executeTime = cycleTime + millisecondDelay;
      delay = millisecondDelay;
 
    }

    unsigned long getInitTime(){
      return initTime;
    }

    /*void changeAbsoluteDelay( int millisecondDelay ){
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
    int repeats;
    int delay;
    int tmpExtraDelay;
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

#define MAX_TASKS 53



class TaskManager{
  public:
    TaskManager(){
       
    }

    void executeCycle(){
      bool didExecute = false;

      cycleTime = millis();

      for ( int i=0; i<tasks; i++ ){
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

    Task * addRepeatingTask( void (*nTaskFunction)( Task* ), int nDelay, int repeats, int startDelay=0 ){
      return addTask( nTaskFunction, repeats, nDelay, startDelay );
    }

    Task * addInfRepeatingTask( void (*nTaskFunction)( Task* ), int nDelay, int startDelay=0 ){
      return addTask( nTaskFunction, -1, nDelay, startDelay );
    }

    Task * addSingleTask( void (*nTaskFunction)( Task* ), int nDelay, int startDelay=0 ){
      return addTask( nTaskFunction, 1, nDelay, startDelay );
    }

    void deleteTask( int taskIndex ){
      if ( tasks <= 0 ){
        errorProtocol( 3 );
      }

      Task * delTask = &allTasks[taskIndex];
      delTask->cancel();

      //for ( int i=taskIndex; i<tasks-1; i++ ){
      //  allTasks[i].copyFrom( &(allTasks[i+1]) );
      //} 
      allTasks[taskIndex].copyFrom( &allTasks[tasks-1] );

      tasks--;
    }

  private:
    Task allTasks [MAX_TASKS];
    int tasks = 0; 

    Task * addTask( void (*nTaskFunction)( Task* ), int repeats, int nDelay, int startDelay ){
      if ( tasks == MAX_TASKS ){
        errorProtocol( 4 );
      }

      Task * cTask = &allTasks[ tasks ];
      cTask->reconstructTask(nTaskFunction, repeats, nDelay, startDelay );

      tasks++;

      return cTask;
    }
};

//DynList<int> Timez;

TaskManager taskManager = TaskManager();

void runPulseFunc( Task * thisTask ){
  bool isOn = (thisTask)->customStates[1] == 1;
  int pinNumber = (thisTask)->customStates[0];

  int  onLength = (thisTask)->customStates[2];
  int offLength = (thisTask)->customStates[3];



  if ( (isOn || onLength==0) && offLength != 0 ){
    (thisTask)->changeRelativeDelay( offLength );
    digitalWrite( pinNumber, LOW );
    (thisTask)->customStates[1] = 0;
  }else{
    (thisTask)->customStates[4]--;
    (thisTask)->changeRelativeDelay( onLength );
    digitalWrite( pinNumber, HIGH );
    (thisTask)->customStates[1] = 1;
  }
}

// stored: pinNumber , on/off , onLength , offLength , repeatsLeft
void pulsePin( int pinNumber, int onLength, int offLength, int repeats, int startDelay ){
  Task * asTask = taskManager.addRepeatingTask( &runPulseFunc, onLength+startDelay, repeats*2-1, startDelay );
  digitalWrite( pinNumber, HIGH );
  
  (asTask)->customStates[0] = pinNumber;
  (asTask)->customStates[1] = 1;
  (asTask)->customStates[2] = onLength;
  (asTask)->customStates[3] = offLength;
}

#define SMOOTH_LIGHT_FLICKER_PERIOD 16
#define SMOOTH_LIGHT_UPDATE_PERIOD  (SMOOTH_LIGHT_FLICKER_PERIOD*3)

void lightLED( int pinNumber, float brightness, int maxFlickerPeriod, int time, int startDelay=0 ){
  float brightnessUnit = 1/maxFlickerPeriod;

  if ( brightness >= 1-brightnessUnit ){
    pulsePin( pinNumber, time, 0, 1, startDelay );
  }else if ( brightness <= brightnessUnit ){
    pulsePin( pinNumber, 0, time, 1, startDelay ); // POSSIBLE ERRORS
  }else{
    maxFlickerPeriod = max( 1, maxFlickerPeriod );

    int onTime = (int) round( brightness * maxFlickerPeriod );
    int offTime = maxFlickerPeriod - onTime;

    pulsePin( pinNumber, onTime, offTime, time/maxFlickerPeriod, startDelay );

    int deadTime = time%maxFlickerPeriod;

    if ( deadTime != 0 ){
      onTime = (int) round( brightness * deadTime );
      offTime = deadTime - onTime;

      pulsePin( pinNumber, onTime, offTime, 1, startDelay+time-deadTime );
    }
  }
}

void runSmoothLightFunc( Task * thisTask ){
  float brightness = (((float) thisTask->customStates[1])/100) + 
      ( (((float) thisTask->customStates[2])/100) * ( cycleTime - thisTask->getInitTime() ) / ((float) thisTask->customStates[3]) );

  if ( brightness >= 1 || brightness <0 ){
    //errorProtocol( 5 );
    //return;
  }

  lightLED( thisTask->customStates[0], brightness, SMOOTH_LIGHT_FLICKER_PERIOD, SMOOTH_LIGHT_UPDATE_PERIOD );
}


// stored: pinNumber, startbrightness, brighnessChange, timeChange
void smoothLightPin( int pinNumber, float startBrightness, float endBrightness, int transitionTime, int startDelay=0 ){
  startBrightness = min( 1, max( startBrightness, 0 ) );
  endBrightness = min( 1, max( endBrightness, 0 ) );

  Task * asTask = taskManager.addRepeatingTask( &runSmoothLightFunc, SMOOTH_LIGHT_UPDATE_PERIOD, (transitionTime/SMOOTH_LIGHT_UPDATE_PERIOD), startDelay );
  lightLED( pinNumber, startBrightness, SMOOTH_LIGHT_FLICKER_PERIOD, SMOOTH_LIGHT_UPDATE_PERIOD, startDelay );

  asTask->customStates[0] = pinNumber;
  asTask->customStates[1] = startBrightness*100;
  asTask->customStates[2] = (endBrightness - startBrightness)*100;
  asTask->customStates[3] = transitionTime;

  int deadTime = SMOOTH_LIGHT_UPDATE_PERIOD + (transitionTime%SMOOTH_LIGHT_UPDATE_PERIOD);
  if ( deadTime != 0 ){
    int onTime = round(endBrightness*deadTime);
    pulsePin( pinNumber, onTime, deadTime-onTime, 1, transitionTime+startDelay-(deadTime) );
  }
}

void runSmoothLightPulseFunction( Task * thisTask ){

  int pinNumber = thisTask->customStates[0];
  float startBrightness = ((float) thisTask->customStates[1])/100;
  float endBrightness = ((float) thisTask->customStates[2])/100;
  int transitionTime = thisTask->customStates[3];

  //pulsePin( LIGHT_B_PIN , 30, 100, 2, 0);
  
  // 1 means its at endbrightness
  if ( thisTask->customStates[4] == 1 ){
    smoothLightPin( pinNumber, endBrightness, startBrightness, transitionTime );
    thisTask->customStates[4] = 0;
  }else{
    smoothLightPin( pinNumber, startBrightness, endBrightness, transitionTime );
    thisTask->customStates[4] = 1;
  }

}

// pinNumber, startbrightness, endbrightness, timeChange, transitionState
void smoothLightPulse( int pinNumber, float startBrightness, float endBrightness, int transitionTime, int startDelay=0, int repeats=-1 ){
  if ( repeats == 0 ){
    return;
  }

  smoothLightPin( pinNumber, startBrightness, endBrightness, transitionTime, startDelay );
  
  Task * asTask;
  if ( repeats<0 ){
    asTask = taskManager.addInfRepeatingTask( &runSmoothLightPulseFunction, transitionTime, startDelay);
  }else{
    asTask = taskManager.addRepeatingTask( &runSmoothLightPulseFunction, transitionTime, repeats, startDelay );
  }
  
  asTask->customStates[0] = pinNumber;
  asTask->customStates[1] = startBrightness*100;
  asTask->customStates[2] = endBrightness*100;
  asTask->customStates[3] = transitionTime;
  asTask->customStates[4] = 1;
}

void basicPulse( Task * eee ){
  int pin = eee->customStates[1];

  eee->customStates[0]++;


  if ( eee->customStates[0] >= 2 ){
    eee->cancel();
  }

  delay(50);
  digitalWrite( pin, HIGH );
  delay(50);
  digitalWrite( pin, LOW );
}

Servo myServo;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  //pinMode(12, OUTPUT);

  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);  

  //pulsePin( LIGHT_A_PIN, 0, 22, 10000, 0 );
  //pulsePin( LIGHT_B_PIN, 100, 250, 10, 250 );
  //pulsePin( LIGHT_C_PIN, 1, 15, 10000, 0 );

  //smoothLightPin( LIGHT_A_PIN, 1,    0, 10000 );
  //lightLED( LIGHT_B_PIN, 0.05,  21,   5000 );
  ///lightLED( LIGHT_C_PIN, 1, 16, 10000 );
  
  //float on  = 0.95;
  //float off = 0;
  //int jump = 100;
  //int loopTime = 360;

  //smoothLightPulse( LIGHT_A_PIN, on, off, loopTime, jump*0 );
  //smoothLightPulse( LIGHT_B_PIN, on, off, loopTime, jump*1 );
  
  Serial.begin( 9600 );

  myServo.attach( 6 );
}

bool lState = false;

// the loop function runs over and over again forever
void loop() {
  
  //taskManager.executeCycle();
  Serial.println( analogRead( A0 ) );
  
  bool thing = analogRead( A0 )<80;

  
  digitalWrite( 11, thing?HIGH:LOW );
  digitalWrite( 10, (!thing)?HIGH:LOW );

  
  myServo.write( rand()%180 );
  delay( 300 );

}














