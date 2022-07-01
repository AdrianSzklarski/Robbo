from random import randint
import time
t = time.time()

class Calc:

    def __init__(self):
        pass

    def position(self):

        self.positionX = []
        self.positionY = []

        self.positionX.append([(randint(1, 100) * x) for x in range(1, 2, 1)])
        self.positionY.append([(randint(1, 100) * y) for y in range(1, 2, 1)])

        return self.positionX, self.positionY


    def __str__(self):
        return {self.positionX, self.positionY}

if __name__ == '__main__':

        t = 0
        while t < 20:
            hear = Calc()
            print('X: ', hear.position()[0], 'Y: ', hear.position()[1])
            time.sleep(0.4)
            t += 1
