class Addition:
    def add(self, a, b):
        s = a + b
        return s

a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))

obj = Addition()
s = obj.add(a, b)

print("Addition of 2 Numbers:", s)