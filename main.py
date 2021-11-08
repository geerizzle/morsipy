import encode
import speech_recognition
import pyttsx3

if __name__ == "__main__":
    

    recognizer = speech_recognition.Recognizer()
    while True:
        # Init
        # Listening to the user speaking
        with speech_recognition.Microphone() as mic:
            print("Speak:", end=" \n")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            try:
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized: {text}")
            except:
                recognizer = speech_recognition.Recognizer()
                continue
