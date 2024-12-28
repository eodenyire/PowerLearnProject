# Smartphone class (with encapsulation)
class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.__battery_life = battery_life  # Private attribute to encapsulate battery life

    # Public method
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Battery life: {self.__battery_life} hours")

    # Method to access private attribute
    def get_battery_life(self):
        return self.__battery_life

    # Method to modify private attribute
    def set_battery_life(self, new_battery_life):
        if new_battery_life > 0:
            self.__battery_life = new_battery_life
        else:
            print("Battery life must be a positive value!")

# Inheritance: Smartphone -> CameraPhone (Polymorphism)
class CameraPhone(Smartphone):
    def __init__(self, brand, model, price, battery_life, camera_quality):
        super().__init__(brand, model, price, battery_life)
        self.camera_quality = camera_quality

    # Overriding display_info method (polymorphism)
    def display_info(self):
        super().display_info()
        print(f"Camera Quality: {self.camera_quality} MP")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 999, 20)
camera_phone = CameraPhone("Samsung", "Galaxy S22", 899, 18, 108)

# Display information
phone1.display_info()
camera_phone.display_info()
