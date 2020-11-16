from time import sleep


class TrafficLigh:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for t in range(3):
            print(TrafficLigh.__color[t])
            if t == 0:
                sleep(7)
            elif t == 1:
                sleep(2)
            elif t == 2:
                sleep(9)


tl = TrafficLigh()
tl.running()