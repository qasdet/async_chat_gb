import json
from variables import MAX_PACKAGE_LENGTH, ENCODING


def send_message(sock, message):
    json_msg = json.dumps(message)
    encoded_message = json_msg.encode(ENCODING)
    sock.send(encoded_message)


def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError
