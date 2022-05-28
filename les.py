import os
import random
import speech_recognition
import datetime


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    "commands": (dict(
            execute_cmd=("текущее время", "который час", "сейчас времени"),
            greenting=("привет", "добрый вечер", "зравствуй", "добрый день", "доброе утра", "привет мой старый друг"),
            play_music=("включи музыку", " запусти проигрыватель", "включи песню", "воспроизведи композицию "),
            create_task=('добавить задачу', "задача", "поставить задачу", "записать задачу"))
                 )

}
def listen_commend():
    """ The function will return the recognized command"""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return  "Dawn... Непонял что ты сказал :/"

def play_music():
    """Play a random mp3 file"""

    files = os.listdir("music")
    random_file = f"music/{random.choice(files)}"
    os.system(f' {random_file}')

    return f'Танцуй под этот трек {random_file.split("/")[-1]}'

def execute_cmd(cmd):
    if cmd == 'ctime':
       #сказать текущее время
        now = datetime.datetime.now()
        print("Сейчас" + str(now.hour) + ':' + str(now.minute))

def create_task():
    """Create a todo task"""

    print("Что добавим в список дел?")

    query = listen_commend()

    with open('todo-list.txt', 'a') as file:
        file.write(f' {query}\n')
        return f'Задача {query} добавлена в todo-list!'

def greeting():
    """Greeting funtion"""

    return "Hello friend!"

def main():
    query = listen_commend()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())
    else:
        print("Поговорим когда научишься разговаривать! >:|")


if __name__ == '__main__':
    main()