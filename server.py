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

class Server(object):
    ''' Front facing server. 
        Instantiate workers, Accept client connections, distribute computation requests among workers and route computed results back to clients. '''

    def __init__(self):
        pass

    def start(self):
        pass

if __name__ == '__main__':
    server = Server().start()
