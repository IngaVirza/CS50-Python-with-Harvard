import time

def decorator_timer(func):
    def wrapper(*args, **kwargs): 
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start}")

    return wrapper

@decorator_timer
def load_file(seconds):
    print("Loading...")
    time.sleep(2)


load_file(0.5)
load_file(1)    



# load_file = decorator_timer(load_file)    
@decorator_timer
def multiply(a, b):
    print("Caounting...")
    time.sleep(1)
    return a * b

multiply(2, 6)