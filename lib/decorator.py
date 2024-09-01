def apply_decorator(func):
    def decorator_func():
        print ("Decorator Applied")
        func()
    return decorator_func

def get_called():
    print("I am the function.")
    
get_called = apply_decorator(get_called)
get_called()