class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} {self.price}"
class Order:
    def __init__(self, receipt):
        self.receipt = receipt
    def add_item(self,item):
        self.receipt.append(item)
    def calculate_taxes(self):
        x = 0
        for item in self.receipt:
            x += item.price * 0.07
        return x
    def calculate_total(self):
        taxes = self.calculate_taxes()
        total = 0
        for item in self.receipt:
           total = item.price + total
        return total
    def print_reciept(self):
        for item in self.receipt:
            print(item)
        print(f"----\n taxes:{self.calculate_taxes()}\n ----\n total:{self.calculate_total()}")

def main():
   
   menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
     
   order1 = Order([])
   order1.add_item(menu[1])
   order1.add_item(menu[1])
   order1.add_item(menu[3])

   total = order1.calculate_total()
   print("The total due is " + str(total))

   order1.print_reciept()
   

if __name__ == '__main__':
    main()
