import threading

class FibonacciThread(threading.Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num