#!/usr/bin/env python

''' zeromq server example.

    One front facing server and three workers are instantiated.
    Front facing server accepts connections from multiple clients and distributes computation requests among workers. 
    Also it collects computed results from workers and send the result back to the original client.

    Demonstrables:
        Multiple client connections.
        Work distribution among a pool of workers. '''

# Author - Kasun Herath <kasunh01 at gmail.com>
# Source - https://github.com/kasun/

import threading

import zmq

class Server(object):
    ''' Front facing server. 
        Instantiate workers, Accept client connections, distribute computation requests among workers and route computed results back to clients. '''

    def __init__(self):
        pass

    def start(self):
        pass

class Worker(threading.Thread):
    ''' Workers accept computation requests from front facing server.
        Does computations and return results back to server. '''

    def __init__(self):
        threading.Thread.__init__(self)
        self.zmq_context = zmq.Context()

    def run(self):
        ''' Main execution. '''
        socket = self.zmq_context.socket(zmq.DEALER)

        while True:
            # First string recieved is client ID
            client_id = socket.recv()
            request = socket.recv()
            result = self.compute(request)

            # For successful route of result to correct client first the client ID should be sent
            socket.send(client_id, zmq.SNDMORE)
            socket.send(result)

    def compute(self, request):
        ''' Computation takes place here. Adds the two numbers which are in the request and return result. '''
        numbers = request.split(':')
        return str(int(numbers[0]) + int(numbers[1]))

if __name__ == '__main__':
    server = Server().start()
