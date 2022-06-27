import sys
import webbrowser

import speech_recognition as sr

# Блок команд
command = {
    "search": ('найди', 'поиск', 'найти'),
    "open_manager": ('диспетчер задач'),
    "open_settings": ('настройки', 'панель управления'),
    "close": ('выход', 'завершение', 'закрыть', 'выйди', 'закрой'),
    "open_folder": ('папку'),
    "open": ('открой', 'открыть'),
    "wifi_on": ('включи', 'включить'),
    "wifi_off": ('выключи', 'выключить'),
    "div": ('раздели', "разделить", 'делить')
}


# Модуль для распознавания речи
r = sr.Recognizer()
def take_command():
    try:
        with sr.Microphone(device_index=1) as source:
            print("Say anything...")
            audio = r.listen(source)

            query = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + query)
    except:
        pass
    return query


# Модуль выполнения
def execute():
    command = (take_command().split(" "))
    if command[0] == 'поиск' or 'найди' or 'найти':
        command.pop(0)
        search_name = " ".join(command)
        url = "https://www.google.com/search?q=" + search_name
        webbrowser.get().open(url)
    elif command[0] == 'выход' or 'выйди' or 'завершение':
        sys.exit()

while True:
    execute()


