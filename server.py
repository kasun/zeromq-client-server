#!/usr/bin/env python

''' zeromq server example.

    One front facing server and three workers are instantiated.
    Front facing server accepts connections from multiple clients and distributes computation requests among workers. 
    Also it collects computed results from workers and send the result back to the original client.

    Demonstrables:
        Multiple client connections.
        Work distribution among a pool of workers. '''

# Author - Kasun Herath <kasunh01 at gmail.com>
# Source - https://github.com/kasun/zeromq-client-server.git

import threading

import zmq

class Server(object):
    ''' Front facing server. '''

    def __init__(self):
        self.zmq_context = zmq.Context()

    def start(self):
        ''' Main execution. 
            Instantiate workers, Accept client connections, 
            distribute computation requests among workers and route computed results back to clients. '''

        # Front facing socket to accept client connections.
        socket_front = self.zmq_context.socket(zmq.ROUTER)
        socket_front.bind('tcp://127.0.0.1:5001')

        # Backend socket to distribute work.
        socket_back = self.zmq_context.socket(zmq.DEALER)
        socket_back.bind('inproc://backend')

        # Start three workers.
        for i in range(1,4):
            worker = Worker(self.zmq_context, i)
            worker.start()

        # Use built in queue device to distribute requests among workers.
        # What queue device does internally is,
        #   1. Read a client's socket ID and request.
        #   2. Send socket ID and request to a worker.
        #   3. Read a client's socket ID and result from a worker.
        #   4. Route result back to the client using socket ID. 
        zmq.device(zmq.QUEUE, socket_front, socket_back)

class Worker(threading.Thread):
    ''' Workers accept computation requests from front facing server.
        Does computations and return results back to server. '''

    def __init__(self, zmq_context, _id):
        threading.Thread.__init__(self)
        self.zmq_context = zmq_context
        self.worker_id = _id

    def run(self):
        ''' Main execution. '''
        # Socket to communicate with front facing server.
        socket = self.zmq_context.socket(zmq.DEALER)
        socket.connect('inproc://backend')

        while True:
            # First string recieved is socket ID of client
            client_id = socket.recv()
            request = socket.recv()
            print('Worker ID - %s. Recieved computation request.' % (self.worker_id))
            result = self.compute(request)
            print('Worker ID - %s. Sending computed result back.' % (self.worker_id))

            # For successful routing of result to correct client, the socket ID of client should be sent first.
            socket.send(client_id, zmq.SNDMORE)
            socket.send(result)

    def compute(self, request):
        ''' Computation takes place here. Adds the two numbers which are in the request and return result. '''
        numbers = request.split(':')
        return str(int(numbers[0]) + int(numbers[1]))

if __name__ == '__main__':
    server = Server().start()
