"""Author:Rawan Khaled"""

import speech_recognition as sr
import webbrowser
import random
import pygame.mixer
import os
from gtts import gTTS
from time import ctime

recognizer = sr.Recognizer()

def Voice_Recognizer():
    global voice
    voice = ''
    try:
        with sr.Microphone() as source:
            # Start listening
            audio = recognizer.listen(source, timeout=2)

            # Recognize what you said using Google's speech recognition
            voice = recognizer.recognize_google(audio)

            # Print the recognized speech
            print("You said:", voice)

    except sr.WaitTimeoutError:
        alexa_speaks("Timeout error: No speech detected.")
    except sr.RequestError as e:
        alexa_speaks(f"Could not request results; {e}")
    except sr.UnknownValueError:
        alexa_speaks("Sorry, I could not understand what you said.")

    return voice

def response(voice_audio):
    if 'what is your name' in voice_audio or "what's your name" in voice_audio:
        alexa_speaks("My name is Alexa, Nice to meet you!")

    if 'what time is it' in voice_audio:
        alexa_speaks(f"It is:  {ctime()} in cairo.")

    if 'how old are you' in voice_audio:
        alexa_speaks("Sorry, I'm just a robot, I have no age.")

    if 'search' in voice_audio:
        alexa_speaks("What do you want me to search for?")
        search=Voice_Recognizer()
        url = 'https://google.com/search?q='+search
        webbrowser.get().open_new_tab(url)
        alexa_speaks(f"Here is your search output for: {search}")

    if 'location' in voice_audio:
        alexa_speaks("What is the location you are asking for?")
        location=Voice_Recognizer()
        url = 'https://google.nl/maps/place/'+ location + '/&amp;'
        webbrowser.get().open_new_tab(url)
        alexa_speaks(f"Here is the location of: {location}")

    if "exit" in voice_audio or "quit" in voice_audio:
        alexa_speaks("Thank you for using Alexas, See you Soon, Good Bye!")
        exit()

def alexa_speaks(audio_str):
    pygame.mixer.init()
    tts = gTTS(text=audio_str, lang='en')
    r = random.randint(1, 10000000)
    audio_file_name = "audio" + str(r) + ".mp3"
    tts.save(audio_file_name)
    pygame.mixer.music.load(audio_file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick value as needed for your desired playback speed
    print(audio_str)
    pygame.mixer.quit()
    os.remove(audio_file_name)


while True:
    alexa_speaks("Google Speech Recognition Assistant here. How can I help you?")
    print("Say something...")
    voice_audio = Voice_Recognizer()
    voice_audio=voice_audio.lower()
    response(voice_audio)





