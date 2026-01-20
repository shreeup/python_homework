import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {list(args) or "None"}")
        logger.info("keyword parameters:")
        if(len(kwargs)>0):
            for key, value in kwargs.items():
                logger.info(f" {key}: {value}")
        else:
            logger.info("None")
        result = func(*args, **kwargs)
        logger.info(f"Return: {result}")
        return result
    return wrapper

@logger_decorator
def add_numbers(a, b):
    """Adds two numbers and accepts optional keyword arguments."""
    return a + b

@logger_decorator
def greet(name, greeting="Hello"):
    """Greets a person with an optional custom greeting."""
    return f"{greeting}, {name}!"

# Call the decorated functions
add_numbers(5, 3, source="test", user_id=123)
greet("Alice", greeting="Hi")
greet("Bob")