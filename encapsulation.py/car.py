class car:
    def __init__(self, speed, fuel_level):
        self.__speed = speed
        self._fuel_level = fuel_level

    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            print("invalid speed")
    
    def __fuel_efficiency(self):
        return self.__speed / 10
    
    def show_efficiency(self):
        print(f"fuel efficiency: {self.__fuel_efficiency()} km/1")

car1 = car(100, 50)
car1.show_efficiency()
car1.set_speed(150)
car1.show_efficiency()
car1.set_speed(250)
print("fuel level:", car1._fuel_level)