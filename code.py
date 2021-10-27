from random import *
import time
import os
from gtts import gTTS
from playsound import playsound


#The countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time Over')


# The Voice Player Function
def play(text):
    myobj = gTTS(text=text, lang='en')
    myobj.save('sound.mp3')
    playsound("sound.mp3")
    os.remove('sound.mp3')


text1 = "Welcome to the Just A Minute Game"
print(text1)
play(text1)
text2 = "Press Y for Start and N for Exit"
print(text2)
play(text2)
randomJList = [
    "Wi-Fi", "Women Empowerment", "Time management", 'Globalization',
    'Demonetization', 'Illiteracy In India', 'Education System In India',
    "Self-Confidence", "Indian Cinemas", "Leader Ship Qualities"
]
checker = input()
if (checker in ["Y", 'y']):
    text3 = "Random Topic Will be Chosen and Time limit is 1 Minute"
    print(text3)
    play(text3)
    n = randomJList[randint(0, len(randomJList)) - 1]
    play("Your topic is: " + n + " " + "And Your Time Starts Now")
    countdown(60)
    play("Well Done!")
else:
    play("Game Over")
time.sleep(5)