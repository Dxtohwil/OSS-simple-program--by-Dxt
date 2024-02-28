import time
import os
import  platform
Seconds = input("How many seconds to countdown?\n")
Minutes = input("How many minutes to countdown?\n")
Hours = input("How many hours to countdown?\n")

TotalTime = int(Seconds) + int(Minutes) * 60 + int(Hours) * 3600
TimerTime = TotalTime
RemainingSecondsAfterHours = 0
RemainingSecondsAfterMinutes = 0
TimerHours=0
TimerMinutes=0
TimerSeconds=0
SecondsPassed= 0

for i in range(TotalTime+1):
    #debugging print(TimerTime)
    
    if(platform.system() != "Windows"):
        os.system("clear")
    else:
        os.system("cls")
    

    TimerSeconds= TimerTime
    
    if TimerTime >= 3600:
        TimerHours = int(TimerTime/3600)
        RemainingSecondsAfterHours = TimerTime-TimerHours*3600
        #debugging print("TimerHours: ", TimerHours)
    else: 
        TimerHours=0
        RemainingSecondsAfterHours=TimerSeconds

    if RemainingSecondsAfterHours > 60 or TimerSeconds > 60: 
        TimerMinutes=int(RemainingSecondsAfterHours/60)
        RemainingSecondsAfterMinutes= RemainingSecondsAfterHours-TimerMinutes*60
        #debugging print("\nTimerMinutes: ", TimerMinutes)
        TimerSeconds=RemainingSecondsAfterMinutes
    else: 
        TimerMinutes=0

    if TimerSeconds < 10:
        TimerSeconds = str("0")+str(TimerSeconds)
    if TimerMinutes < 10:
        TimerMinutes = str("0")+str(TimerMinutes)
    if TimerHours < 10:
        TimerHours = str("0")+str(TimerHours)

    #debugging print("\nTimerSeconds: ", TimerSeconds)
    print("Timer:", TimerHours,":",TimerMinutes,":",TimerSeconds)
    print("Seconds passed:", SecondsPassed)
    TimerTime-=1
    SecondsPassed+=1
    time.sleep(1)
# this only works on a linux system with sox installed and with the appropriate sound file in the right file location.
# os.system("play /home/-your-username-/SoundEffects/ping.mp3  > /dev/null 2>&1")
print("Time Over!")
