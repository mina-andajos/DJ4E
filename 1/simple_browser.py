import socket
from typing import List, Optional


class MyConnection:
    def __init__(self, properties=(socket.AF_INET, socket.SOCK_STREAM)) -> None:
        self.socket = socket.socket(*properties)  # ? opens the socket

    def send_request(
        self,
        domain: str = "data.pr4e.org",
        document: str = "page1.htm",
        port: int = 80,
    ):
        self.socket.connect((domain, port))  # ? dials up
        cmd: bytes = f"GET http://{domain}/{document} HTTP/1.0\r\n\r\n".encode()
        self.socket.send(cmd)
        return cmd

    def receive_response(self):
        _data: List[str] = []

        while True:
            _response: str = self.socket.recv(512).decode()
            if len(_response) < 1:
                break
            _data.append(_response)

        self.socket.close()
        return "".join(_data)


def main():
    my_connection = MyConnection()
    print(
        my_connection.send_request(domain="localhost", document="", port=9000),
        end="\n",
    )
    print(my_connection.receive_response())


if __name__ == "__main__":
    main()
