class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def show_message(self):
        print("from singleton")

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

obj1.show_message()

# Explanation:
# The __new__ method ensures only one instance of the class exists.
# If _instance is None, it creates a new object, otherwise, it returns the existing instance.
