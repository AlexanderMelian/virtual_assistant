import pyttsx3

engine = pyttsx3.init()

def speak(param):
    engine.setProperty('rate',160)
    
    if param == "eng":
        output("Welcome")
        output("Wait a momment")
    elif param == "esp":
        engine.setProperty('voice','spanish')
        output("Bienvenido")
        output("Espera un momento")


def output(param):
    engine.say(param)
    engine.runAndWait()
