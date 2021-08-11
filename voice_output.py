import pyttsx3
import language
import functions_help

#class pyttsx3
class Out_engine:
    engine = pyttsx3.init()

    def __init__(self):
        self.engine.setProperty('rate', 150)
        self.lang = ""
        self.listening = ""
        self.searching = ""
        self.wait_me = ""
        self.current_time = ""
        self.current_temperature = ""
        self.current_weather = ""
        self.current_date = ""
        self.welcome = ""
        self.good_day = ""
        self.good_afternoon = ""
        self.good_evening = ""
        self.what_should_i_search = ""
        self.good_bye = ""
        self.i_do_not_understand = ""
        self.repeat = ""
        self.of = ""

    def set_spanish(self):
        self.engine.setProperty('voice', 'spanish')
        self.lang = "es"
        self.listening = language.spanishwords[0]
        self.searching = language.spanishwords[1]
        self.wait_me = language.spanishwords[2]
        self.current_time = language.spanishwords[3]
        self.current_temperature = language.spanishwords[4]
        self.current_weather = language.spanishwords[5]
        self.current_date = language.spanishwords[6]
        self.welcome = language.spanishwords[7]
        self.good_day = language.spanishwords[8]
        self.good_afternoon = language.spanishwords[9]
        self.good_evening = language.spanishwords[10]
        self.what_should_i_search = language.spanishwords[11]
        self.good_bye = language.spanishwords[12]
        self.i_do_not_understand = language.spanishwords[13]
        self.repeat = language.spanishwords[14]
        self.attendee = language.spanishwords[15]
        self.of = language.spanishwords[16]
        self.an = language.spanishwords[17]

    def set_english(self):
        self.engine.setProperty('voice', 'english')
        self.lang = "en"
        self.listening = language.englishwords[0]
        self.searching = language.englishwords[1]
        self.wait_me = language.englishwords[2]
        self.current_time = language.englishwords[3]
        self.current_temperature = language.englishwords[4]
        self.current_weather = language.englishwords[5]
        self.current_date = language.englishwords[6]
        self.welcome = language.englishwords[7]
        self.good_day = language.englishwords[8]
        self.good_afternoon = language.englishwords[9]
        self.good_evening = language.englishwords[10]
        self.what_should_i_search = language.englishwords[11]
        self.good_bye = language.englishwords[12]
        self.i_do_not_understand = language.englishwords[13]
        self.repeat = language.englishwords[14]
        self.attendee = language.englishwords[15]
        self.of = language.englishwords[16]
        self.an = language.englishwords[17]

    def say_listening(self):
        self.say(self.listening)

    def say_searching(self):
        self.say(self.searching)
    
    def say_wait_me(self):
        self.say(self.wait_me)
    
    def say_current_time(self):
        self.say(self.current_time)
        self.say(functions_help.current_time(self.an))
    
    def say_current_temperature(self):
        self.say(self.current_temperature)
    
    def say_current_weather(self):
        self.say(self.current_weather)
    
    def say_current_date(self):
        self.say(self.current_date)
        self.say(functions_help.calculate_date(self.of))
    
    def say_welcome(self):
        self.say(self.welcome)
    
    def say_good_day(self):
        self.say(self.good_day)

    def say_good_afternoon(self):
        self.say(self.good_afternoon)

    def say_good_evening(self):
        self.say(self.good_evening)
    
    def say_what_should_i_search(self):
        self.say(self.what_should_i_search)

    def say_good_bye(self):
        self.say(self.good_bye)
    
    def say_i_do_not_understand(self):
        self.say(self.i_do_not_understand)

    def say_repeat(self):
        self.say(self.repeat)

    def say(self, text):
        self.engine.say(text)
        self.run()

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
        if self.lang == "en":
            return str(language.english_commands[number])
        else:
            return str(language.spanish_commands[number])


    def call_attendee(self):
        self.engine.say_listening()
