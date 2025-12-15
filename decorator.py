import time

# Timer decorator
def timer(func):

    def wrapper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before} seconds to execute")
       
    return wrapper

@timer
def myfunction():
    x = 1000
    result = 1
    for i in range(1,x):
        result*=i
    return result
# myfunction()


#Logging decorator

def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")

        return result
    return wrapper

@logger
def add(x,y):
    return x+y

#Access control decorator

def admin_required(func):

    def wrapper(user, *args, **kwargs):
        if user != 'admin':
            raise Exception("This function requires admin privileges")
        return func(*args, **kwargs)
    return wrapper

@admin_required
def delete_db():
    print("Database deleted")


#Memoization (caching)

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n in {0,1}:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def upperrize(func) : 

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper

@upperrize
def printer(txt):
    return txt



if __name__ == "__main__":

    print(printer("Hello world"))

