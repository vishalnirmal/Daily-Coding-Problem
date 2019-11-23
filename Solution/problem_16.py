# You run an e-commerce website and want to record the last N order ids in a log.

class Log:
    def __init__(self, N=5):
        self.N = N
        self.log = []

    def record(self, id):
        if len(self.log) == 5:
            self.log.pop(0)
        self.log.append(id)
    
    def get_last(self, i):
        return self.log[i*-1:]

if __name__ == "__main__":
    log = Log(10)
    for i in range(5):
        log.record(i)
    print(log.get_last(4))