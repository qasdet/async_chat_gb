import subprocess
import locale
import chardet

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

print('---------------------Задача №1------------------------------------')
string1 = 'разработка'
string2 = 'сокет'
string3 = 'декоратор'

var_str = [string1, string2, string3]

for _ in var_str:
    print(f'Содержимое: {_}, тип {type(_)}')

string1_utf8 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
string2_utf8 = '\u0441\u043e\u043a\u0435\u0442'
string3_utf8 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

var_utf8 = [string1_utf8, string2_utf8, string3_utf8]

for _ in var_utf8:
    print(f'Содержимое: {_}, тип {type(_)}')

# 2. Каждое) из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
print()
print('------------------Задача №2------------------------------')

data = [b'class', b'function', b'method']

for _ in data:
    print(f'Содержимое: {_}, тип {type(_)}, длина {len(_)}.')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
print()
print('------------------Задача №3------------------------------')

data = ['attribute', 'класс', 'функция', 'type']

for i in data:
    try:
        print(f'Слово <{i}> в виде байтовой строки {bytes(i, "ascii")}')
    except UnicodeEncodeError:
        print(f'Слово <{i}> невозможно записать в виде байтовой строки')

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).
print()
print('------------------Задача №4------------------------------')

data = ['разработка', 'администрирование', 'protocol', 'standard']

for i in data:
    print(f'Слово <{i}> в байтовом виде: <{i.encode("utf8")}>, обратное преобразование: <{i.encode("utf8").decode()}>.')

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# тип на кириллице.

print()
print('------------------Задача №5------------------------------')

for sites in ['yandex.ru', 'youtube.com']:
    args = ['ping', sites]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.

print()
print('------------------Задача №6------------------------------')

def_co = locale.getpreferredencoding()
print(f'Кодировка по умолчанию: {def_co}')

f = open('file.txt', 'w')
f.writelines(['сетевое программирование\n', 'сокет\n', 'декоратор\n'])
f.close()

print()
print(f'Файл в кодировке по умолчанию ({def_co}).')
print('--------------------------------------------')
with open('file.txt', encoding=def_co) as f_n:
    for el_str in f_n:
        print(el_str[:-1])
print('--------------------------------------------')
f_n.close()

print()
print(f'Файл в кодировке UTF-8.')
print('--------------------------------------------')

with open('file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str[:-1])

print('--------------------------------------------')
f_n.close()