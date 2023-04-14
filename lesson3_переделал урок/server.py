from socket import *
import time
import json
import argparse
import ipaddress

from lesson3.global_vars import *


def get_message(client):
    """
    Получает сообщение от клиента
    :param client:
    :return: строку сообщения
    """
    msg = client.recv(BUFFERSIZE).decode(ENCODING)
    return json.loads(msg)


def preparing_response(response_code: int, action: str = 'presence'):
    """Готовит ответ клиенту"""
    data = {
        'action': action,
        'time': time.time(),
        'response': response_code,
    }
    return json.dumps(data).encode(ENCODING)


def send_message(client, message: bytes):
    client.send(message)


def get_socket(address: str, port: int, listen: int = 5):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(listen)
    return s


def start(address: str, port: int):
    s = get_socket(address, port)

    while True:
        client, addr = s.accept()
        cm = get_message(client)
        print(cm['message'])
        msg = preparing_response(OK)
        send_message(client, msg)
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, default=7777,
                        help='TCP-порт для работы (по умолчанию использует 7777)')
    parser.add_argument('-a', dest='address',
                        help='IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)')
    args = parser.parse_args()

    address = args.address or ''
    if address:
        try:
            ipaddress.ip_address(address)
        except ValueError:
            parser.error(f'Введен не корректный ip адрес "{address}"')

    start(address, args.port)
