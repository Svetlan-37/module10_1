from time import sleep
import time
import threading



def write_words(word_count, file_name):
    count = 0
    with (open(file_name, 'w', encoding='utf-8') as file):
        while count < word_count:
            count += 1
            file.write(f'\nКакое-то слово № {count}')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time = time.time()
w1 = write_words(10, 'example1.txt')
w2 = write_words(30, 'example2.txt')
w3 = write_words(200, 'example3.txt')
w4 = write_words(100, 'example4.txt')
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Работа потоков {elapsed_time}')

start_time = time.time()
t1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
t2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
t3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
t4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Работа потоков {elapsed_time}')
