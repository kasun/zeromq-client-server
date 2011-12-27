#!/usr/bin/env python

''' zeromq client example.

    Three clients are instantiated.
    Each client would generate a pair of numbers and send them to a server to be computed. 
    The computation is adding the two numbers together.
    Once the computed result is recieved from the server it would be printed to standard out. 

    Demonstrables:
        Multiple client architecture.
        Response getting delivered to correct client. '''

# Author - Kasun Herath <kasunh01 at gmail.com>
# Source - https://github.com/kasun/

import threading

class Client(threading.Thread):
    ''' Represents an example client '''
    def __init__(self, identity):
        threading.Thread.__init__(self)
        self.identity = identity

    def run(self):
        num1, num2 = self.generate_numbers()

    def send(self, socket, data):
        pass

    def receive(self, socket):
        pass 

    def get_connection(self):
        pass

    def generate_numbers(self):
        pass
