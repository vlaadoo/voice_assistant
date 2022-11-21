import prog_config
import stt
import tts
from fuzzywuzzy import fuzz
import random
import json
import utils.commands as commands

def boot():
    # Opening JSON file
    with open('user.json') as f:
        js_config = json.load(f)

    if (not js_config["VA_USER_NAME"] and not js_config["VA_USER_CITY"]):
        first_boot()
        stt.va_listen(va_respond)



    else:
        print(f"{prog_config.VA_NAME} (v{prog_config.VA_VER}) начал свою работу ...")
        stt.va_listen(va_respond)


def first_boot():
    with open("user.json", "r+") as config_json:
        js_config = json.load(config_json)
        print(js_config)
        config_json.seek(0)
        name_text = "Скажите как Вас зовут"
        tts.va_speak(name_text)
        print(name_text)
        
        name_query = stt.va_listen_once(clean_voice)


        city_text = "Скажите Ваш город"
        tts.va_speak(city_text)
        print(city_text)
        city_query = stt.va_listen_once(clean_voice)
        js_config["VA_USER_NAME"] = name_query
        js_config["VA_USER_CITY"] = city_query
        json.dump(js_config, config_json)
        print("qu " + name_query)
        print("qu " + city_query)
        config_json.close()


def va_respond(voice: str):
    print(voice)
    if voice.startswith(prog_config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in prog_config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def clean_voice(voice: str):
    cmd = filter_cmd(voice)



def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in prog_config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in prog_config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in prog_config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text =  "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        tts.va_speak(text)
        pass

    if cmd == 'ctime':
        tts.va_speak(commands.play_time())

    if cmd == "cdate":
        tts.va_speak(commands.play_date())


    if cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    if cmd == 'weather':
        tts.va_speak(commands.get_weather())

 
    # elif cmd == "shutdown":


    # elif cmd == "sleep":


    # elif cmd == "reboot":


    if cmd == "browser":
        tts.va_speak(commands.open_browser())


    if cmd == "notepad":
        tts.va_speak(commands.open_notepad())


    if cmd == "coin":
        tts.va_speak(commands.play_coin())

    if cmd == "dice":
        tts.va_speak(commands.play_dice())



# начать прослушивание команд
# stt.va_listen(va_respond)
boot()
