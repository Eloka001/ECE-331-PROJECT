import speech_recognition as sr
import random
from time import sleep

WORDS = ["tea", "eat", "eye", "love", "rice", "egg"]
OPPORTUNITY = random.choice(WORDS)
trial = 1

#Instantiating the recognizer and microphone
r = sr.Recognizer()


print("Choose a word from 'tea, eat, eye, love, rice, egg'")
print("You have 3 trials!")
sleep(2)

while trial < 4:
    print(f"Guess {trial}")
    trial+=1
    file_name = input("Enter the file name: ")
    the_audio = sr.AudioFile(file_name)
    with the_audio as source:
        audio = r.record(source)
    try:
        if OPPORTUNITY == r.recognize_google(audio, show_all = False):
            print("Correct! You won!")
            break
        else:
            print("Try Again")
            continue
    except:
        print("An error occurred")

else:
    print("You have reached the maximum amount of guesses!")
    print("Good Bye!")
    print(f"I was thinking of {OPPORTUNITY}")
