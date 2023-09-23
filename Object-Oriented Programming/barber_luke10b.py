class Gumball_Machine:
    
    #constructor
    def __init__(self, capacity, money):
        self.capacity = capacity
        self.money = money
        self.list = []
        for gum in range(0,self.capacity):
            import random
            num = [1,2,3]
            rand = random.choice(num)
            if rand == 1:
                color = "red"
                self.list.append(color)
            elif rand == 2:
                color = "green"
                self.list.append(color)
            elif rand == 3:
                color = "blue"
                self.list.append(color)
        print('Gumball Mahcine created with',self.capacity,'random gumballs')
        print()

    def report(self):
        print('Gumball Machine Report:')
        print('- Gumballs in machine:',self.capacity)
        self.cash = '$'+format(self.money,',.2f')
        print('- Money in machine:', self.cash)
        print()

    def dispense(self, value):
        self.value = value
        if self.capacity > 0:
            if self.value == .25:
                ball = self.list.pop()
                self.capacity -= 1
                self.money += 0.25
                print("Accepting 0.25: Dispensing a",ball,"gumball")
                print()
                
            elif self.value != .25:
                print("Invalid coin, no gumball will be dispensed")
                print()
        else:
            print("Machine is empty, no gumball will be dispensed")
            print()

        
    def count_gumballs_by_type(self, flavor):
        colorcount = 0
        for item in self.list:
            if item == 'red' and flavor == 'red':
                colorcount += 1
            if item == 'green' and flavor == 'green':
                colorcount += 1
            if item == 'blue' and flavor == 'blue':
                colorcount += 1
        print("there are",colorcount, flavor,"gumballs in the machine")
        print()
        


def main():
    machine = Gumball_Machine(5,0)
    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")

    machine.dispense(0.10)
    machine.dispense(0.50)
    machine.dispense(0.01)

    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")

    machine.dispense(0.25)
    machine.dispense(0.25)
    machine.dispense(0.25)

    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")

    machine.dispense(0.25)
    machine.dispense(0.25)
    machine.dispense(0.25)

    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")


main()


            
        
