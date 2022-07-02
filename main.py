import sys
import webbrowser
import subprocess
import speech_recognition as sr
import pyttsx3


# Настройка для голового ответа ассистента
kott = pyttsx3.init()
voices = kott.getProperty('voices')
kott.setProperty('voice', 'ru')


def talk(text):
    kott.say(text)
    kott.runAndWait()


# Модуль для распознавания речи
r = sr.Recognizer()



def take_command():
    try:
        with sr.Microphone(device_index=1) as source:
            talk('Котт к вашим услугам. Скажите что-нибудь')
            print('Say anything... ')
            audio = r.listen(source)
            query = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + query)

    except sr.WaitTimeoutError:
        talk('Проверьте работу своего микрофона и повторите ввод снова')

    return query


# Модуль выполнения
def execute():
    command = (take_command().split(" "))
    if command[0] == 'поиск' or command[0] == 'найди' or command[0] == 'найти':
        talk('Уже ищу в интернете')
        command.pop(0)
        search_name = " ".join(command)
        url = "https://www.google.com/search?q=" + search_name
        webbrowser.get().open(url)
        sys.exit()

    elif command[0] == 'выход' or command[0] == 'выйди' or command[0] == 'завершение':
        talk('Всего хорошего')
        sys.exit()

    elif command[0] == 'раздели' or command[0] == 'разделить':
        talk('Секунду, считаю')
        divisible = int(command[1])
        divider = int(command[3])
        if divider != 0:
            print("Результат деления", divisible, "на", divider, "равен", divisible/divider)
        else:
            print("Ошибка вычисления. На 0 делить нельзя")
            talk("Правила математики запрещают мне делить на ноль, о мешок с костями")
        sys.exit()

    elif " ".join(command) == 'открой диспетчер задач' or " ".join(command) == 'открыть диспетчер задач':
        talk('Открываю диспетчер задач')
        subprocess.run("taskmgr", shell=True)
        sys.exit()

    elif " ".join(command) == 'открой настройки' or " ".join(command) == 'открыть настройки'\
        or " ".join(command) == 'открой панель управления' or " ".join(command)== 'открыть панель управления':
        talk('Открываю панель управления')
        subprocess.run("control", shell=True)
        sys.exit()

    elif " ".join(command) == 'открой папку пользователя' or " ".join(command) == 'открыть папку пользователя':
        talk('Открываю вашу папку')
        subprocess.run("start %windir%\explorer.exe %userprofile%", shell=True)
        sys.exit()

    elif " ".join(command) == 'выключи wi-fi' or " ".join(command) == 'выключить wi-fi':
        talk('Вы уверены, что хотите выключить интернет? Для продолжения скажите "да"')
        with sr.Microphone(device_index=1) as source:
            print("Say 'да' to continue")
            audio = r.listen(source)
            answer = r.recognize_google(audio, language="ru-RU").lower()
            if answer == 'да':
                subprocess.run("netsh wlan disconnect", shell=True)
            else:
                pass
        sys.exit()
    else:
        print("Команда не распознана, попробуйте снова")
        talk("Команда не распознана, попробуйте снова")


# Запуск через бесконечный цикл
while True:
    execute()
