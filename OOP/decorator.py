import time

def decorator_timer(func):
    def wrapper(): 
        print('start')
        func()
        print('end')

    return wrapper

@decorator_timer
def load_file():
    print("Loading...")
    time.sleep

# load_file = decorator_timer(load_file)    

load_file()
