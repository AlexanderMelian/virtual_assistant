from datetime import datetime
from builds import telegraf
from src import language
import tokens

def calculate_hour() -> str:
        hour = int(current_hour())
        if hour >= 6 and hour <= 12:
            return "day"
        elif hour >= 12 and hour <= 18:
            return "afternoon"
        else:
            return "evening"

def current_time(an) -> str:
    hour = int(current_hour())
    minute = int(current_minute())
    return  "", hour, " ", an, " ", minute

def current_hour() -> int:
    return datetime.now().strftime('%H')

def current_minute() -> int:
    return datetime.now().strftime('%M')

def calculate_day() -> int:
    return int(datetime.now().strftime('%d'))
    
def calculate_month() -> int:
    return int(datetime.now().strftime('%m'))
    
def calculate_year() -> int:
    return int(datetime.now().strftime('%Y'))

def remember_spanish(query):
    telegraf.send_message(query)


def remember_english(query):
    query = query.split(' ')

def calculate_date(bet) -> str:
    day = calculate_day()
    month = calculate_month()
    year = calculate_year()
    return "" , day , " ", bet, " " , month , " ", bet, " ", year


def spanish_number_calculator(numero_str):
    numero_int = 0
    if type(numero_str) == str:
        numero_str = numero_str.split(' ')
    if len(numero_str) == 1:
        if numero_str[0] in language.UNIDADES:
            return language.UNIDADES.get(numero_str[0])
        elif numero_str[0] in language.DIEZ_DIEZ:
            return language.DIEZ_DIEZ.get(numero_str[0])
        elif numero_str[0] in language.DECENAS_VEINTE:
            return language.DECENAS_VEINTE.get(numero_str[0])        
        elif numero_str[0] in language.DECENAS_DIEZ:
            return language.DECENAS_DIEZ.get(numero_str[0])
        elif numero_str[0] == language.CIENTOS[1]:
            return language.CIENTOS[1]

    elif len(numero_str) == 2:
        if numero_str[0] in language.CIENTOS:
            numero_int += language.CIENTOS.get(numero_str[0])
        elif numero_str[0] in language.DIEZ_DIEZ:
            numero_int += language.DIEZ_DIEZ.get(numero_str[0])
        if numero_str[1] in language.UNIDADES:
            numero_int += language.UNIDADES.get(numero_str[1])
        elif numero_str[1] in language.DECENAS_DIEZ:
            numero_int += language.DECENAS_DIEZ.get(numero_str[1])
        elif numero_str[1] in language.DECENAS_VEINTE:
            numero_int += language.DECENAS_VEINTE.get(numero_str[1])
        return numero_int

    elif len(numero_str) == 3:
        if numero_str[1] != 'y':
            return "ERROR"
        if numero_str[0] in language.DIEZ_DIEZ:
            numero_int += language.DIEZ_DIEZ.get(numero_str[0])
        if numero_str[2] in language.UNIDADES:
            numero_int += language.UNIDADES.get(numero_str[2])
        return numero_int

    elif len(numero_str) == 4:
        if numero_str[2] != 'y':
            return "ERROR"
        if numero_str[0] in language.CIENTOS:
            numero_int += language.CIENTOS.get(numero_str[0])
        if numero_str[1] in language.DIEZ_DIEZ:
            numero_int += language.DIEZ_DIEZ.get(numero_str[1])
        if numero_str[3] in language.UNIDADES:
            numero_int += language.UNIDADES.get(numero_str[3])
        return numero_int
    return "ERROR"