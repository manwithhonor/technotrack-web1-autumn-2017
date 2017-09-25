import socket
import os

def get_page_not_found(message=None):
    response= 'HTTP/1.1 404 Not Found\n\n{}\n'.format(message)
    return response.encode()


def get_bad_request():
    response='HTTP/1.1 400 Bad Request\n\n400 Bad Request'
    return response.encode()

def get_good_request(message=None):
    response = 'HTTP/1.1 200 OK\n\n{}\n'.format(message)
    return response.encode()

def get_response(request):
    request = request.decode()

    try:
        type_of_request = request.split(' ', maxsplit=1)[0]
        path = request.split(' ', maxsplit=2)[1]
    except IndexError:
        return get_bad_request()

    if (type_of_request != "GET"):
        return get_bad_request()
    elif (path == '/'):
        user_agent = request.partition('User-Agent: ')[2]
        user_agent = user_agent.split('\n', maxsplit=1)[0]
        response = get_good_request("Hello mister!\nYou are: {}\n".format(user_agent))
        return response
    elif (path == '/test/'):
        response = get_good_request(request)
        return response
    elif (path.startswith('/media/')):
        file_name = path.partition('/media/')[2]
        if (file_name == ""):
            try:
                files = os.listdir('../files')
                list_of_files = '\n'.join(files)
                response =get_good_request (list_of_files)
                return response
            except:
                return get_bad_request()
        else:
            try:
                with open('../files/' + file_name, 'r') as file:
                    content_of_file = file.read()
                response =get_good_request(content_of_file)
                return response
            except IOError:
                response = get_page_not_found("File not found")
                return response
    else:
        response =get_page_not_found("Page not found")
        return response


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # Assigns address, consisted of two items: ip-address and port, to a socket
server_socket.listen(0)  #server_socket becomes able to accept connection requests via accept()
# parametr define number of input connection into queue

print ('Server started...\n')

while 1:
    try:
        (client_socket, address) = server_socket.accept()

        print ('Got new client', client_socket.getsockname())
        #Prints address of a socket, which is returned by accept()
        # and  send/receive data on the connection

        request_string = client_socket.recv(2048)  # receiving data from client, size of buffer is 2048 byte
        client_socket.send(get_response(request_string))   #  Sending server response to the other end of connection
        client_socket.close()
    except KeyboardInterrupt:  # stop endless cycle via combination ctrl+C
        print ('Stopped')
        server_socket.close()  # close socket,  close connection and release associated memory.
        exit()

