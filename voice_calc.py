import speech_recognition as sr
import pyttsx3
import re
import operator

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return None

def calculate(command):
    operators = {
        'plus': operator.add,
        'minus': operator.sub,
        'times': operator.mul,
        'divided by': operator.truediv
    }
    
    pattern = re.compile(r'([0-9]+)\s*(plus|minus|times|divided by)\s*([0-9]+)')
    match = pattern.search(command)
    
    if match:
        num1, op, num2 = match.groups()
        num1, num2 = int(num1), int(num2)
        result = operators[op](num1, num2)
        return result
    else:
        return "Sorry, I couldn't perform that calculation."

def main():
    speak("How can I help you?")
    command = recognize_speech()
    if command:
        result = calculate(command)
        print("Result:", result)
        speak(f"The answer is {result}")

if __name__ == "__main__":
    main()