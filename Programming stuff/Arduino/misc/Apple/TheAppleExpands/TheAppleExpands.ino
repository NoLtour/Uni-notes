#include <Servo.h>

Servo myServo;

#define G0 -1
#define G1 393
#define G2 441
#define G3 495
#define G4 556
#define G5 624
#define G6 661
#define G7 742

#define GL1 G1/2
#define GL2 G2/2
#define GL3 G3/2
#define GL4 G4/2
#define GL5 G5/2
#define GL6 G6/2
#define GL7 G7/2

#define GLL1 G1/4
#define GLL2 G2/4
#define GLL3 G3/4
#define GLL4 G4/4
#define GLL5 G5/4
#define GLL6 G6/4
#define GLL7 G7/4

#define GH1 G1*2
#define GH2 G2*2
#define GH3 G3*2
#define GH4 G4*2
#define GH5 G5*2
#define GH6 G6*2
#define GH7 G7*2

#define GHH1 G1*4
#define GHH2 G2*4
#define GHH3 G3*4
#define GHH4 G4*4
#define GHH5 G5*4
#define GHH6 G6*4
#define GHH7 G7*4

#define PIN_A 11 
#define PIN_B 10
#define PIN_C 9
#define PIN_D 6

long currentTime = 0;

int motorPos  = 0;
bool motorDir = false;

#define SOUND_PIN_COUNT 4
int SOUND_PINS [SOUND_PIN_COUNT] = { PIN_A, PIN_B, PIN_C, PIN_D };

class SoundManager{
  public:
    SoundManager(){
      for ( int i=0; i<SOUND_PIN_COUNT; i++ ){
        oupPeriods[i] = 0;
        oupStates[i]  = false;
        killTime[i]   = 0;
      }
    }

    void executeLoop(){

      currentTime = micros();

      updateOutputStates();
    }

    void playSound( int frequency, long millisecondLength ){
      millisecondLength = max( 0, millisecondLength );

      int period = 1000000/frequency;

      for ( int pinIndex=0; pinIndex<SOUND_PIN_COUNT; pinIndex++ ){
        if ( oupPeriods[pinIndex] <= 0 ){
          oupPeriods[pinIndex] = period;
          killTime[pinIndex] = currentTime + (millisecondLength*1000);

          return;
        }
      }
    }

  private:
    long oupPeriods [SOUND_PIN_COUNT];
    bool oupStates  [SOUND_PIN_COUNT];
    
    long killTime [SOUND_PIN_COUNT];

    void updateOutputStates(){
      for ( int pinIndex=0; pinIndex<SOUND_PIN_COUNT; pinIndex++ ){
        long dPinPeriod = oupPeriods[pinIndex];
        if ( dPinPeriod > 0 ){
          bool reqState = currentTime%dPinPeriod>dPinPeriod/2;

          if ( oupStates[pinIndex] != reqState ){
            if ( killTime[pinIndex] <= currentTime ){
              oupStates[pinIndex]  = 0;
              killTime[pinIndex]   = 0;
              oupPeriods[pinIndex] = 0;
              analogWrite(SOUND_PINS[pinIndex], 0 );

            }else{
              oupStates[pinIndex] = reqState;
              analogWrite(SOUND_PINS[pinIndex], reqState?255:0 );
            }
          }
        }

      }
    }
};


int notes1_1[] = { // *4
  G1, G1, G1, G1, G1, G1, G1,
  G1, G1, G1, G1, G1 
};
float times1_1[]={ 
  1, 1, 1, 0.25, 0.25, 0.25, 0.25,
  1, 1, 1, 0.5, 0.5,
};

int notes1_2[] = { // *2
  GLL6, G0, GLL6, GLL5, GLL6, GLL6, G0,   GLL6, GLL5, GLL6,
  GLL6, G0, GLL6, GLL5, GLL6, GLL6, GLL6, GL1,  GL2,  GL1, GL2,
  GLL6, G0, GLL6, GLL5, GLL6, GLL6, G0,   GLL6, GLL5, GLL6,
  GLL6, G0, GLL6, GLL5, GLL6, GL2,  GL1,  GL2,  GL1,  GLL6, G1
};
float times1_2[]={ 
  1, 0.25, 0.25, 0.25, 0.25, 1, 0.25, 0.25, 0.25, 0.25,
  1, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25,
  1, 0.25, 0.25, 0.25, 0.25, 1, 0.25, 0.25, 0.25, 0.25,
  1, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25
};

int notes2_1[] = { // 104 
GL6, GL7, G1, G2, G3, G6, G5, 
G3, GL6, G3, G2, G1, GL7, 
GL6, GL7, G1, G2, G3, G2, G1, 
GL7, GL6, GL7, G1, GL7, GL6, GL5, GL7, 
GL6, GL7, G1, G2, G3, G6, G5, 
G3, GL6, G3, G2, G1, GL7, 
GL6, GL7, G1, G2, G3, G2, G1, 
GL7, G1, G2, G3, 
GL6, GL7, G1, G2, G3, G6, G5, 
G3, GL6, G3, G2, G1, GL7, 
GL6, GL7, G1, G2, G3, G2, G1, 
GL7, GL6, GL7, G1, GL7, GL6, GL5, GL7, 
GL6, GL7, G1, G2, G3, G6, G5, 
G3, GL6, G3, G2, G1, GL7, 
GL6, GL7, G1, G2, G3, G2, G1, 
GL7, G1, G2, G3
}; 
float times2_1[]={ 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  1 ,  1 ,  0.5 ,  0.5 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  1 ,  1 ,  0.5 ,  0.5 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  1 ,  1 ,  1 ,  1 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  1 ,  1 ,  0.5 ,  0.5 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  1 ,  1 ,  0.5 ,  0.5 ,  0.5 ,  0.5 , 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 , 
  1 ,  1 ,  1 ,  1 
};

int notes3_1[] = { // 104 
G5, G6, G3, G2, G3, G2, G3, 
G5, G6, G3, G2, G3, G2, G3, 
G2, G1, GL7, GL5, GL6, GL5, GL6, 
GL7, G1, G2, G3, GL6, G3, G5 
}; 
float times3_1[]={ 
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 ,
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 ,
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 ,
  0.5 ,  0.5 ,  0.5 ,  0.5 ,  1 ,  0.5 ,  0.5 
};
int notes3_2[] = { // 104 
G5, G6, G3, G2, G3, G2, G3,
G5, G6, G3, G2, G3, G6, G7, 
GH1, G7, G6, G5, G3, G2, G3, 
G2, G1, GL7, GL5, GL6, G3, G5
};

int notes4_1[] = { // 104 
GL6, GL6, GL6, GL6, GL6, GL6, GL6, GL6
}; 
float times4_1[]={ 
  0.75 ,  0.25 ,  0.5 ,  0.5 ,  0.75 ,  0.25 ,  0.5 ,  0.5
}; 



int blockSize [] = {
  12, 12, 12, 12, 42, 42, 104, 28, 28, 28,  28, 28, 28, 28,  28, 8,  8,  8,  8,  8,  8,  8,  8, 
};
int * tuneBlocks [] = {
  notes1_1, notes1_1, notes1_1, notes1_1, notes1_2, notes1_2, notes2_1, notes3_1, notes3_1, notes3_1, notes3_2, notes3_1, notes3_1, notes3_1, notes3_2, notes4_1, notes4_1, notes4_1, notes4_1, notes4_1, notes4_1, notes4_1, notes4_1
};
float * timeBlocks [] = {
  times1_1, times1_1, times1_1, times1_1, times1_2, times1_2, times2_1, times3_1, times3_1, times3_1, times3_1, times3_1, times3_1, times3_1, times3_1, times4_1, times4_1, times4_1, times4_1, times4_1, times4_1, times4_1, times4_1
};

SoundManager soundManager = SoundManager();


void setup() {
  // put your setup code here, to run once:
  //soundManager.playSound( 1000 , 1000 );
  //soundManager.playSound( 2000 , 2000 );
  //soundManager.playSound( 4000 , 3000 );
  //soundManager.playSound( 8000 , 4000 );

  myServo.attach( 6 );

}

#define TIME_MUL 433

int cPos = 0;
long timeTillNext = 0;

int cBlockIndex = 4;

int * cTuneBlock = tuneBlocks[ cBlockIndex ];
float * cTimeBlock = timeBlocks[ cBlockIndex ];
int cBlockSize   = blockSize[ cBlockIndex ];

void loop() {
  // put your main code here, to run repeatedly:
  soundManager.executeLoop();

  if ( timeTillNext <= currentTime ){

    long nextLength = cTimeBlock[ cPos ] * TIME_MUL;
    long nextNote   = cTuneBlock[ cPos ];

    if ( cPos >= cBlockSize-1 ){
      cPos = 0;
      cBlockIndex = (cBlockIndex+1);
      if ( cBlockIndex >= 23 ){
        cBlockIndex = 0;
        delay( 10000 );
      }

      cTuneBlock = tuneBlocks[ cBlockIndex ];
      cTimeBlock = timeBlocks[ cBlockIndex ];
      cBlockSize = blockSize[ cBlockIndex ];
    }else{
      cPos++;
    }

    soundManager.playSound(nextNote, nextLength-30);
    //soundManager.playSound(nextNote-5, (nextLength -40)*0.8 );
    //soundManager.playSound(nextNote-10, (nextLength -40)*0.7 );
    //soundManager.playSound(nextNote-12, (nextLength -40)*0.6 );


    timeTillNext = currentTime + (nextLength * 1000);
  }


}
























