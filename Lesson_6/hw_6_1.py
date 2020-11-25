from time import sleep


class TrafficLight:
    __color = 'Blinked'

    @staticmethod
    def running():
        while True:
            TrafficLight.color = 'Red'
            print(TrafficLight.color)
            sleep(7)
            TrafficLight.color = 'Yellow'
            print(TrafficLight.color)
            sleep(2)
            TrafficLight.color = 'Green'
            print(TrafficLight.color)
            sleep(7)


tl = TrafficLight()
tl.running()
