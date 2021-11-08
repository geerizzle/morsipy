import encode
import speech_recognition
import pyttsx3


def start_listening(func):
    """
        NAME
            start_listening(<function to encode with>) 

        DESCTIPTION
            Function used to initialize the listener that then sends the text to the Google API
            tasked with getting us the spoken words as a string.
    """
    # Init
    recognizer = speech_recognition.Recognizer()
    while True:
        # Listening to the user speaking
        with speech_recognition.Microphone() as mic:
            print("Speak:", end=" \n")
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)
            try:
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized: {text}")
                print(func(text))
            except:
                recognizer = speech_recognition.Recognizer()
                continue


if __name__ == "__main__":
    start_listening(encode.encode_morse)
    

   
