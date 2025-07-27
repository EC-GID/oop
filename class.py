class Smartphone:
    def __init__(self, brand, model, battery_life, price):
        self.brand = brand
        self.model = model
        self._battery_life = battery_life 
        self.price = price

    def turn_on(self):
        print(f"{self.model} is now ON.")

    def turn_off(self):
        print(f"{self.model} is now OFF.")

    def check_battery(self):
        print(f"{self.model} battery life is {self._battery_life}%.")

    def set_battery_life(self, battery_life):
        if 0 <= battery_life <= 100:
            self._battery_life = battery_life
        else:
            print("Invalid battery life percentage. It should be between 0 and 100.")

    def get_battery_life(self):
        return self._battery_life
phone1 = Smartphone("Apple", "iPhone 13", 85, 999)
phone1.turn_on()
phone1.check_battery()
phone1.set_battery_life(90)
phone1.check_battery()
phone1.turn_off()