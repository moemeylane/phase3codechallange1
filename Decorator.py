def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    decorated_func = decorator_func(func)
    return decorated_func

@apply_decorator
def my_function():
    print("Hello, World!")

my_function()
