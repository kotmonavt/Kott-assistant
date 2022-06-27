import sys
import webbrowser
import speech_recognition as sr


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
    if command[0] == 'поиск' or command[0] == 'найди' or command[0] == 'найти':
        command.pop(0)
        search_name = " ".join(command)
        url = "https://www.google.com/search?q=" + search_name
        webbrowser.get().open(url)
    elif command[0] == 'выход' or command[0] == 'выйди' or command[0] == 'завершение':
        sys.exit()
    elif command[0] == 'раздели' or command[0] == 'разделить':
        divisible = int(command[1])
        divider = int(command[3])
        if divider != 0:
            print("Результат деления", divisible, "на", divider, "равен", divisible/divider )
        else:
            print("Правила математики запрещают мне делить на ноль, о мешок с костями")
    elif 'открой диспетчер задач' in take_command() or 'открыть диспетчер задач' in take_command():
        pass
    else:
        print("Команда не распознана, попробуйте снова")


while True:
    execute()
