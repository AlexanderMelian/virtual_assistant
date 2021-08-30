import pyttsx3
from src import language
from src import functions_help

#class pyttsx3
class Out_engine:
    engine = pyttsx3.init()

    def __init__(self):
        self.engine.setProperty('rate', 150)

    def set_spanish(self):
        self.engine.setProperty('voice', 'spanish')
        self.lang = "es"

    def set_english(self):
        self.engine.setProperty('voice', 'english')
        self.lang = "en"

    def say_listening(self):
        self.say(self.number_command(0))

    def say_searching(self):
        self.say(self.number_command(1))
    
    def say_wait_me(self):
        self.say(self.number_command(2))
    
    def say_current_time(self):
        self.say(self.number_command(3))
        self.say(functions_help.current_time(self.number_command(17)))
    
    def say_current_temperature(self):
        self.say(self.number_command(4))
    
    def say_current_weather(self):
        self.say(self.number_command(5))
    
    def say_current_date(self):
        self.say(self.number_command(6))
        self.say(functions_help.calculate_date(self.number_command(17)))
    
    def say_welcome(self):
        self.say(self.number_command(7))
    
    def say_good_day(self):
        self.say(self.number_command(8))

    def say_good_afternoon(self):
        self.say(self.number_command(9))

    def say_good_evening(self):
        self.say(self.number_command(10))
    
    def say_what_should_i_search(self):
        self.say(self.number_command(11))

    def say_good_bye(self):
        self.say(self.number_command(12))
    
    def say_i_do_not_understand(self):
        self.say(self.number_command(13))

    def say_repeat(self):
        self.say(self.number_command(14))

    def say_try_again_later(self):
        self.say(self.number_command(18))

    def say(self, text):
        self.engine.say(text)
        self.run()

    def say_im_remember(self, query):
        self.say(self.number_command(19))
        functions_help.remember_spanish(query)

    def run(self):
        self.engine.runAndWait()

    def say_calculate_hour(self):
        hour = functions_help.calculate_hour()
        if hour == "day":
            self.say_good_day()
        elif hour == "afternoon":
            self.say_good_afternoon()
        else:
            self.say_good_evening()

    def commands(self, number) -> str:
        if self.is_english():
            return str(language.english_commands[number])
        else:
            return str(language.spanish_commands[number])

    def call_attendee(self):
        self.engine.say_listening()

    def number_command(self, number):
        if self.is_english():
            return str(language.englishwords[number])
        else:
            return str(language.spanishwords[number])

    def is_english(self):
        return self.lang == "en"
