import speech_recognition as sr
import voice_output

r = sr.Recognizer()
r.pause_threshold = 0.5
r.energy_threshold = 400
r.voice = ''
language = ''

def take_command():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language=r.voice)
        except Exception as e:
            print("Error :  " + str(e))        
            return "None"
        return query
              

def set_spanish():
    r.voice = 'es-ES'

def set_english():
    r.voice = 'en-in'