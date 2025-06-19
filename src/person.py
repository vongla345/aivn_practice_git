class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describe(self):
        print(f"Name is {self.name}, age is {self.age}")
        
def main():
    p1 = Person("Nhan", "12")
    p1.describe()
    
if __name__ == "__main__":
    main()