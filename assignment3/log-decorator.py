import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Format positional parameters
        pos_params = list(args) if args else "none"
        
        # Format keyword parameters
        key_params = kwargs if kwargs else "none"
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Logging with the required labels and format
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {key_params}")
        logger.log(logging.INFO, f"return: {result}")
        
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def var_positional(*args):
    return True

@logger_decorator
def var_keywords(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    var_positional(10, "Apple", True)
    var_keywords(user="Admin", status="Active", id=505)
