import time
from random import randint
from threading import Thread


class dataGenerator(Thread):
    def __init__(self,cps):
        Thread.__init__(self)
        self.minData=0
        self.maxData=10
        self.alert = 80
        self.cps=cps

    def run(self):
        while True:
            x = randint(0,100)
            if x > self.alert:
                self.cps.data.append(randint(self.minData*2,self.maxData*10))
            else:
                self.cps.data.append(randint(self.minData,self.maxData))

            time.sleep(1)
