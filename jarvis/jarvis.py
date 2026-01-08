
import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_song(song_name):
    song_name = song_name.lower()
    if song_name in musiclibrary.musiclibrary:
        webbrowser.open(musiclibrary.musiclibrary[song_name])
        print(f"Playing {song_name}...")
    else:
        print("Song not found in library!")
        speak("Song not found in library!")

def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
  






    elif "play" in command:   # Example: "play apna bana le"
        song_name = command.replace("play", "").strip()
        # if song_name:
        if song_name in musiclibrary.musiclibrary:

            play_song(song_name)
            speak(f"Playing {song_name}")
        else:
            speak("Please say the song name after play.")


if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    speak("Yes")
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        process_command(command)
        except Exception as e:
            print(f"Error: {e}")