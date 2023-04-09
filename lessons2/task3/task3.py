"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

"""

import yaml

first_key = [
    'list_item1',
    'list_item2',
    'list_item3',
    'list_item4'
]

second_key = 100

third_key = {
    'first_value':  str(100) + u'\u20BD',
    'second_value': str(200) + u'\u20AC',
    'third_value': str(300) + u'\u20BF',
}

to_yaml = {'first_key': first_key, 'second_key': second_key, 'third_key': third_key}

with open('test.yaml', 'w', encoding='utf-16') as t_f:
    yaml.dump(to_yaml, t_f, allow_unicode=True, default_flow_style=False, default_style='"')

with open('test.yaml', 'r', encoding='utf-16') as file_read:
    print(f'Данные совпадают? {yaml.safe_load(file_read) == to_yaml}')
