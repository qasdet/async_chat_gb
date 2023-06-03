import socket


def login_required(func):
    '''
        Декоратор, проверяющий, что клиент авторизован на сервере.
        Проверяет, что передаваемый объект сокета находится в
        списке авторизованных клиентов.
        За исключением передачи словаря-запроса
        на авторизацию. Если клиент не авторизован,
        генерирует исключение TypeError
        '''

    def checker(*args, **kwargs):
        from Lesson_14_Vystrchil.server.core import MessageProcessor
        from Lesson_14_Vystrchil.common.variables import ACTION, PRESENCE
        if isinstance(args[0], MessageProcessor):
            found = False
            for arg in args:
                if isinstance(arg, socket.socket):
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True

            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == PRESENCE:
                        found = True
            if not found:
                raise TypeError
        return func(*args, **kwargs)

    return checker
