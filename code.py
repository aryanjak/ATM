class Car:
    def __init__(self, color, price, model, avg):
        self.color = color
        self.price = price
        self.model = model
        self.avg = avg

    def getColor(self):
        print("The Color of the Car is:" + self.color)

    def getPrice(self):
        print("Price of the Car:" + self.price)

    def gM(self):
        print("Model of the car:" + self.model)

    def avvg(self):
        print("Average of the car is:" + self.avg)

Fortuner = Car("White","51 Lac","2022","10")
Fortuner.avvg()

Lamborghini_Urus = Car("Red","3.43Cr","2022","7.5") 
Lamborghini_Urus.getPrice()