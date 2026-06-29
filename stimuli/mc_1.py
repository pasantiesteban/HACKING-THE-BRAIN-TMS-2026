class MyObject:
    b = 0  
    
    def __init__(self, x, y):
        self.a = x  
        MyObject.b = y  
    
    @staticmethod
    def main():
        o1 = MyObject(4, 3)
        o2 = MyObject(2, 1)
        
        print(f"{o1.a},{o1.b},{o2.a},{o2.b}")

if __name__ == "__main__":
    MyObject.main()


# Uncomment the correct answer below:
# a) print("4,3,2,1")
# b) print("4,3,2,2")
# c) print("2,1,2,1")
# d) print("4,1,3,1")
# e) print("4,1,2,1")
# f) Exception thrown
# g) Won't compile