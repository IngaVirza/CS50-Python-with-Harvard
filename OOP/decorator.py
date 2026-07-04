import time

def decorator_timer(func):
    def wrapper(): 
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start}")

    return wrapper

@decorator_timer
def load_file():
    print("Loading...")
    time.sleep

# load_file = decorator_timer(load_file)    

load_file()
