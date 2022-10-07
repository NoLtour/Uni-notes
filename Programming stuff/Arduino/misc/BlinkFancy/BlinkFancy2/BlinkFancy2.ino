

#define PULSE_PERIOD 14

#define DEBUG_LIGHT_PIN LED_BUILTIN

void light( float fraction, int totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  int onTime = (int) (PULSE_PERIOD*fraction);
  int offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(LED_BUILTIN, HIGH);   
    digitalWrite(12, LOW);   
    delay(onTime);                       
    digitalWrite(LED_BUILTIN, LOW);  
    digitalWrite(12, HIGH);
    delay(offTime); 
    
  }
}

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

void smoothLight( float stBright, float enBright, int transTime ){
  stBright = stBright<0?0:( stBright > 1?1:stBright );
  enBright = enBright<0?0:( enBright > 1?1:enBright );
  
  float brightness = stBright;
  float transRate  = (enBright-stBright) * PULSE_PERIOD/( (float) transTime);

  for ( int timePassed=0; timePassed<=transTime; timePassed +=PULSE_PERIOD ){
    light( brightness, PULSE_PERIOD );

    brightness += transRate;
  }
}

float takesFunc( float (*func)(float ), float x  ){
  return func( x );
}

float pFunc( float a  ){
  return a;
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

void errorProtocol( int errorNumber=1 ){
  errorNumber = errorNumber<=0?1:errorNumber;

  for ( ;; ){
    pinPulse( DEBUG_LIGHT_PIN, 0, 260 );
    pinPulse( DEBUG_LIGHT_PIN, 1, 2000 );
    pinPulse( DEBUG_LIGHT_PIN, 0, 500 );

    pinNumberPulse( DEBUG_LIGHT_PIN, errorNumber );
  }
}

enum TaskType{ REPEATING, SINGLE };

class Task{
  public:
    Task( void (*nTaskFunction)( Task ), TaskType nTaskType, int nDelay ){
      taskFunction = nTaskFunction;
      taskType = nTaskType;
      delay = nDelay;
      executeTime = millis() + delay;
    }

    void cancel(){
      isCanceled = true;
    }

    bool checkCanceled(){
      return isCanceled;
    }

  private:
    void (*taskFunction)( Task );
    TaskType taskType;
    int delay;
    bool isCanceled = false;
    unsigned long executeTime;
};

#define MAX_LIST_SIZE 60

template<typename T>
class DynList{
  public:
    DynList(){
      length = 0;
    }

    ~DynList(){
      
    }

    void add( T * nContent ){
      if ( length + 2 == MAX_LIST_SIZE ){
        errorProtocol( 4 );
      }
      /*
      T ** newListContents = new T * [length+1];

      for ( int i=0; i<length; i++ ){
        newListContents[i] = listContents[i];
      }

      newListContents[length] = nContent;

      delete listContents;
      listContents = newListContents;*/
      listContents[length] = nContent;
      length++;
    }

    void remove( int index ){
      if ( index >= length || index < 0 ){
        errorProtocol( 2 );
      }

      /*T ** newListContents = new T * [length-1];

      for ( int i=0; i<index; i++ ){
        newListContents[i] = listContents[i];
      }

      for ( int i=index+1; i<length; i++ ){
        newListContents[i-1] = listContents[i];
      }

      delete listContents;
      listContents = newListContents;*/

      for ( int i=index; i>=length-1; i-- ){
        listContents[i] = listContents[i+1];
      }

      length--;
    }

    T * get( int index ){
      if ( index < 0 || index >= length ){
        errorProtocol( 3 );
      }

      return listContents[ index ];
    }

    int getLength(){
      return length;
    }

  private:
    int length;
    T * listContents [MAX_LIST_SIZE];


};

class TaskManager{

  public:
    TaskManager(){
      allTasks = DynList<Task>();
    }

    void addRepeatingTask( void (*nTaskFunction)( Task ), int nDelay ){

      allTasks.add( new Task( nTaskFunction, REPEATING, nDelay ) );

    }

    void deleteTask( int taskIndex ){
      Task * delTask = allTasks.get( taskIndex );

      (*delTask).cancel();

      delete delTask;
    }

  private:
    DynList<Task> allTasks;

};

DynList<int> Timez;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(12, OUTPUT);
  
  Timez = DynList<int>();

  int * n1 = new int();
  *n1 = 1;
  Timez.add( n1 );
  int * n2 = new int();
  *n2 = 4;
  Timez.add( n2 );
  int * n3 = new int();
  *n3 = 3;
  int * n4 = new int();
  *n4 = 2;
  int * n5 = new int();
  *n5 = 5;

  Timez.add( n3 );
  Timez.add( n4 );
  Timez.add( n5 );
}


// the loop function runs over and over again forever
void loop() {
  smoothLight( 0, 1, 1000 );
  smoothLight( 1, 0, 1000 );

  digitalWrite(12, LOW);  
  digitalWrite(13, LOW);  

  for ( int i=0; i<Timez.getLength(); i++ ){
    int cTime = *Timez.get(i);

    if ( cTime > 20 ){
      errorProtocol( 5 );
    }

    delay(500);
    pinNumberPulse( 12 ,cTime );
    delay(500);
  }
  /*
  int genList [] = { 1,2,3,4 };
  for ( int i=0; i<4; i++ ){
    int cTime = genList[i];

    if ( cTime > 20 ){
      errorProtocol( 5 );
    }

    delay(500);
    pinNumberPulse( 12 ,cTime );
    delay(500);
  }*/

}
