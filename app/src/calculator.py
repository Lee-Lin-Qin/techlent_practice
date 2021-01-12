class Calculator():
    def add(self, num1, num2):
        num3= num1+num2
        return(num3)
    def substrate(self, num1, num2):
        num3=num1-num2
        return(num3)
if __name__ == "__main__":
    cal = Calculator()               #Initialize the program
    print(cal.add(1,3))
