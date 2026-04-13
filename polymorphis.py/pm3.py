class vehicle:
    def start(self):
        print("vehicle starting")

class car(vehicle):
    def start(self):
        print("car engine starting")

v = vehicle()
c = car()

v.start()
c.start()