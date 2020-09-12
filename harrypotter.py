import os
import vlc
import time
def screen_clear():

   if os.name == 'posix':
      _ = os.system('clear')
   else:

      _ = os.system('cls')
screen_clear()
print("\t\t\t\t\t\t\t\t\t\t Tom Riddle Diary")
hp=input('my name is ')
time.sleep(1)
screen_clear()
ht=hp.split()
print("\nhello ",ht[0],",my name is tom riddle\n")
time.sleep(2)

hp1=input()
if hp1=="do you know anything about the chamber of secrets?":
    print('\nyes')
    time.sleep(2)
    screen_clear()

    hp3=input()
    if hp3=="can you tell me?":
        time.sleep(2)
        screen_clear()

        print('\nNO')
        time.sleep(2)
        screen_clear()


        print("\nbut i can show you")
        time.sleep(2)
        screen_clear()

        print("\nlet me take you back fifty years ago")
        time.sleep(2)
        screen_clear()

        print('\n\n\n13th june')
        media=vlc.MediaPlayer("harrytom.mp4")
        media.play()
        time.sleep(6)
        hp2=input('press enter to stop :')
        media.stop()
        screen_clear()

    else:
        print("sorry i have to go, bye")



else: print('i know nothing about that')
