import logging
import socket


class Server:
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _create(self, domain: str, port: int, tries: int) -> None:
        self._socket.bind((domain, port))
        self._socket.listen(tries)
        return None

    def _parse_request(self) -> socket.socket:
        client_socket, address = self._socket.accept()
        client_request: str = client_socket.recv(5000).decode()
        client_request_pieces: list = client_request.split("\n")
        if len(client_request_pieces) > 0:
            logging.debug(f"{client_request_pieces[0]=}\n")
        return client_socket

    def _respond(self, client_socket: socket.socket) -> None:
        response_dict = {
            "protocol": "HTTP/1.1",
            "status": "200 OK",
            "headers": "Content-Type: text/html; charset=utf-8",
            "body": "<html><body>Hello World</body></html>",
        }
        response = f'{response_dict["protocol"]} {response_dict["status"]}\r\n{response_dict["headers"]}\r\n\r\n{response_dict["body"]}\r\n\r\n'
        client_socket.sendall(response.encode())
        client_socket.shutdown(socket.SHUT_WR)
        return None

    def run(self, domain: str = "localhost", port: int = 9000, tries: int = 5):
        logging.info(f"Running Server...\nAccess: http://localhost:9000")
        logging.debug(f"On domain: {domain} | port: {port} | tries: {tries}\n")

        try:
            self._create(domain=domain, port=port, tries=tries)
            while 1:
                client_socket = self._parse_request()
                self._respond(client_socket=client_socket)

        except KeyboardInterrupt:
            logging.info("Shutting Down Server...\n")
        except Exception as exc:
            logging.error(exc)
        finally:
            self._socket.close()
        return None


def main(debug: bool = False):
    logging_level = logging.DEBUG if debug == True else logging.INFO
    logging.basicConfig(level=logging_level)

    my_server = Server()
    my_server.run()


if __name__ == "__main__":
    main(debug=True)
