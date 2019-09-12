################################################################################
# MUST USE PYTHON 3
# SOURCE:
# > https://dbader.org/blog/python-decorators
#
################################################################################

def null_decorator(func):
    return func

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def greet():
    return 'Hello!'


greet2 = null_decorator(greet)
print( greet2() )

greet3 = uppercase(greet)
print( greet3() )

@uppercase
def salut():
    return 'Ciao!'

print( salut() )

print( '\nWhat are these new functions?' )
print( '                greet = ' + str(greet) )
print( 'null_decorator(greet) = ' + str(null_decorator(greet)) )
print( '     uppercase(greet) = ' + str(uppercase(greet)) )


################################################################################
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

print( '\nUsing two decorators at once!')
print( greet() )


################################################################################
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '+
              f'returned {original_result!r}')

        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

print( '\nWhat happens when I give arguments?')
print( say('Jane', 'Hello, World') )


################################################################################
print( '\nBe careful with decorated functions data/info:' )

def greet():
    """Return a friendly greeting."""
    return 'Hello!'

decorated_greet = uppercase(greet)

print( 'greet name and doc:' )
print( greet.__name__ )
print( greet.__doc__ )
print( 'decorated greet name and doc:' )
print( decorated_greet.__name__ )
print( decorated_greet.__doc__ )


################################################################################
print( '\nBut this can be fixed with functools!:' )

import functools

def good_uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@good_uppercase
def good_greet():
    """Return a friendly greeting."""
    return 'Hello!'

print( 'good greet name and doc:' )
print( good_greet.__name__ )
print( good_greet.__doc__ )


################################################################################
