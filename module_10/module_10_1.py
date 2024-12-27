import threading
from datetime import datetime
from time import sleep

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

started_at = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
ended_at = datetime.now()
print(f"Работа потоков {ended_at - started_at}")

started_at2 = datetime.now()
thread = threading.Thread(target=wite_words,args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words,args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words,args=(100, 'example7.txt'))
thread4 = threading.Thread(target=wite_words,args=(200, 'example8.txt'))

thread.start()
thread2.start()
thread3.start()
thread4.start()

thread.join()
thread2.join()
thread3.join()
thread4.join()

ended_at2 = datetime.now()
print(f"Работа потоков {ended_at2 - started_at2}")