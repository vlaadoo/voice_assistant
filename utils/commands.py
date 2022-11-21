from datetime import datetime
import webbrowser
import os
import random
from pyowm import OWM
from sys import platform
import json

from utils.num_to_text_ru import num2text


global js_config

with open('user.json') as f:
    js_config = json.load(f)

owm = OWM('528494a2fb6c40a6e96816537b3026e5')
mgr = owm.weather_manager()


def open_notepad():
    os.system("NOTEPAD")

def open_browser():
    webbrowser.open('http://google.com', new=2)


def play_date():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    weekday = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"][datetime.weekday(now)]
    return ("сегодня "+weekday+", "+get_date(date))


def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('-')
    return (day_list[int(date_list[2]) - 1] + ' ' +
            month_list[int(date_list[1]) - 1] + ' '
            #date_list[0] + ' года'
            )


def play_time():
    now = datetime.now()
    hours = int(now.strftime("%H"))
    mins = int(now.strftime("%M"))
    return ("сейчас " + num2text(hours) + " " + num2text(mins))


def play_coin(): 
    arrR = [
        "Выпал орел",
        "Выпала решка",
    ]
    return (arrR[random.randint(0, len(arrR) - 1)])

def play_dice(): 
    arrR = [
        "Выпала единица",
        "Выпало два",
        "Выпало три",
        "Выпало четыре",
        "Выпало пять",
        "Выпало шесть",
    ]
    return (arrR[random.randint(0, len(arrR) - 1)])


def get_weather():
    # погода
    observation = mgr.weather_at_place(js_config['VA_USER_CITY'])
    weather = observation.weather
    status = weather.detailed_status
    temperature = weather.temperature('celsius')["temp"]
    wind_speed = weather.wind()["speed"]

    return ("На улице сейчас " + num2text(int(temperature)) + " градус и скорость ветра " + num2text(int(wind_speed)) + " метр в секунду")



    
        #     if platform == "linux" or platform == "linux2":
    #         # linux
    #         pass
    #     elif platform == "darwin":
    #         os.system("sudo shutdown -h +1")
    #     elif platform == "win32":
    #         # Windows...
    #         pass



        #     if platform == "linux" or platform == "linux2":
    #         # linux
    #         pass
    #     elif platform == "darwin":
    #         os.system(os.getlogin(), "sudo shutdown -s +1")
    #     elif platform == "win32":
    #         # Windows...
    #         pass


        #     if platform == "linux" or platform == "linux2":
    #         # linux
    #         pass
    #     elif platform == "darwin":
    #         os.system("sudo shutdown -r +1")
    #     elif platform == "win32":
    #         # Windows...        
    #         pass