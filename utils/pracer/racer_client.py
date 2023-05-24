import socket
from abc import ABC

from pracer.racer_error_result import RacerErrorResult
from pracer.racer_operation_api import RacerOperationAPI
from pracer.racer_result import RacerResult


class RacerClient(RacerOperationAPI, ABC):

    def __init__(self, host, port) -> None:
        self._host = host
        self._port = port
        self.racer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.racer_socket.connect((self._host, self._port))
        except ConnectionError:
            print('Connection to Racer server failed.')

    def disconnect(self):
        self.racer_socket.close()

    def send(self):
        pass

    def racer_call(self, *args) -> RacerResult:

        buffer = args[0] + ' '
        if len(args) > 1:
            if type(args[1]) is tuple:
                buffer += ' '.join(el for el in args[1])
            else:
                for el in args[1:]:
                    if el is not None:
                        buffer += str(el) + ' '

        buffer = buffer.rstrip(' ')
        buffer = '(' + buffer + ')\n'

        try:
            self.racer_socket.send(buffer.encode())
        except Exception:
            print('No socket')
            return RacerErrorResult('No Socket')

        recv = ''
        while '\n' not in recv:
            recv += self.racer_socket.recv(64).decode()

        return RacerResult(recv)
