from datetime import datetime


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



def calculate_date(bet) -> str:
    day = calculate_day()
    month = calculate_month()
    year = calculate_year()
    return "" , day , " ", bet, " " , month , " ", bet, " ", year