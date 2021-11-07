import encode
import speech_recognition
import pyttsx3

if __name__ == "__main__":
    
    # Init
    recognizer = speech_recognition.Recognizer()
    while True:

        # Listening to the user speaking
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                print(f"Recognized {text}")

        except speech_recognition.UnknownValueError():
        
            recognizer = speech_recognition.Recognizer()
            continue
