import welcome_user
import voice_output
import voice_input

out = voice_output.Out_engine()

def main():
    while True:
        # get voice input and make a string
        query = voice_input.take_command()
        if query.lower() == out.commands(0): # if query is equal to assistant
            out.say_calculate_hour()
            out.say_listening()
            try_help()

#you have three tries to say a valid command 
def try_help():
    attempt = 3
    while attempt > 0:
        query = voice_input.take_command()
        if query.lower() in out.commands(1):
            out.say_current_date()

        elif query.lower() in out.commands(2):
            out.say_current_time()

        #elif query.lower() in out.commands(3):
        #    out.say_current_temperature()

        #elif query.lower() in out.commands(4):
        #    out.say_current_weather()
        else:
            attempt -= 1
            if attempt > 0:
                out.say_i_do_not_understand()
            else:
                out.say_try_again_later()

def menu():
    print("Select language")
    print("1. English")
    print("2. Spanish")
    lang = int(input("Enter a number: "))
    if lang == 1:
        print("You have selected English")
        welcome_user.speak("eng")
        out.set_english()
        voice_input.set_english()
    elif lang == 2:
        print("You have selected Spanish")
        welcome_user.speak("esp")
        out.set_spanish()
        voice_input.set_spanish()
    else:
        print("Invalid input")
        menu()
    
if __name__ == '__main__':
    menu()
    main()