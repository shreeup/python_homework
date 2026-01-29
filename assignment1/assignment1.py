# Write your code here.
import re

def hello():
    return 'Hello!'


def greet(name):
    return f'Hello, {name}!'


def calc(a1,a2,op='multiply'):
    try:
        match op:
            case 'add':
                return a1+a2
            case 'divide':
                return a1/a2
            case 'multiply':
                return a1*a2
            case 'subtract':
                return a1-a2
            case 'modulo':
                return a1%a2
            case _:
                raise ZeroDivisionError
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except ValueError:
        return "You can't multiply those values!"
    except:
        return 'You can\'t multiply those values!'

def data_type_conversion(val,name):
    try:
        match name:
            case 'float':
                return float(val)
            case 'str':
                return str(val)
            case 'int':
                return int(val)
    except:
        return 'You can\'t convert banana into a int.'

def grade(*args):
    try:
        if not args:  # Check if no arguments were provided
            return 0.0
        
        total_sum = sum(args)
        number_of_arguments = len(args)
        
        result= total_sum / number_of_arguments
        match result:
            case _ if result >= 90:
                return 'A'
            case _ if result >= 80:
                return 'B'
            case _ if result >= 70:
                return 'C'
            case _ if result >= 60:
                return 'D'
            case _ if result >= 0:
                return 'F'
    except:
        return "Invalid data was provided."

def repeat(original,c):
    return original*c

def student_scores(pos,**kwargs):
    try:
        if pos=="best":
            result=None
            largest=float("-inf")
            for key, value in kwargs.items():
                if value>largest:
                    largest=value
                    result=key
            return result
        else:
            sumtotal=0
            for key, value in kwargs.items():
                sumtotal+=value
            return sumtotal/len(kwargs)
    except:
        raise ValueError

def titleize(param):
    littlewords=['a','on','an','the','of','and','is','in']
    words=param.split(' ')
    result=[]
    n=len(words)
    for i,word in enumerate(words):
        if i==0 or i==n-1 or word not in littlewords:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)

def hangman(secret,guess):
    guesschars=set(guess)
    result=[]
    for charecter in secret:
        if charecter in guesschars:
            result.append(charecter)
        else:
            result.append('_')
    return "".join(result)


def pig_latin(sentence):
    """
    Converts a sentence to Pig Latin based on rules:
    1. Vowel start: append 'ay'.
    2. Consonant start (including 'qu'): move leading cluster to end and append 'ay'.
    """
    words = sentence.split()
    pig_latin_words = []
    
    for word in words:
        if word[0] in "aeiouAEIOU":
            pig_latin_words.append(word + "ay")
        else:
            match = re.search(r"^([^aeiou]*qu|[^aeiou]+)([aeiou].*)", word, re.IGNORECASE)
            if match:
                consonant_cluster = match.group(1)
                rest = match.group(2)
                pig_latin_words.append(rest + consonant_cluster + "ay")
            else:
                pig_latin_words.append(word + "ay")
    
    return " ".join(pig_latin_words)
