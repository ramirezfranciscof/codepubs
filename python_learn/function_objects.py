################################################################################
#
# SOURCE:
# > https://dbader.org/blog/python-first-class-functions
#
################################################################################

def yell( text ):
    yell_text = text.upper() + '!'
    return yell_text


bark = yell

print( bark( 'woof' ) )

del yell
try:
    print( yell('hello?') )
except:
    print( 'yell no longer exists but bark does:' )
    print( bark('hey') )

print( 'String identifier assign at creation time: ' )
print( bark.__name__ )


funcs = [bark, str.lower, str.capitalize]
print( '\nFunctions can be stored in lists and accessed iteratively:' )
print( funcs )
for f in funcs:
    print( f.__name__, f('hey ThErE') )

print( '\nAnd also called individually: funcs[0]("heyho")' )
print( funcs[0]( 'heyho' ) )

################################################################################

def greet( func ):
    greeting = func( 'Hi, I am a Python program' )
    print( greeting )

def whisper( text ):
    whisper_text = text.lower() + '...'
    return whisper_text

def speak( text ):
    def whisper2( t ):
        return t.lower() + '...'
    print whisper(text)
    return whisper( text )


greet( bark )
greet( funcs[1] )
greet( whisper )

maplist = list( map( bark, ['hello', 'hey', 'hi'] ) )
print( maplist )

speak( 'Hello world' )


################################################################################

def get_speak_func1(volume):
    def speak_down(text):
        return text.lower() + '...'
    def speak_up(text):
        return text.upper() + '!'
    if volume > 0.5:
        return speak_up
    else:
        return speak_down

def get_speak_func2(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper


speak_func = get_speak_func1(0.3)
print( speak_func( 'HellO' ) )
speak_func = get_speak_func1(0.7)
print( speak_func( 'HellO' ) )

print( get_speak_func2( 'Hello World', 0.3 )() )
print( get_speak_func2( 'Hello World', 0.7 )() )


################################################################################

def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print( plus_3(4) )
print( plus_5(4) )

################################################################################

print( '\nObjects can be made callable so that they behave like functions.' )

class Adder:
    def __init__(self, n):
         self.n = n
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print( plus_3(4) )

print( 'Is it callable??' )
print( 'plus_3 = ', callable(plus_3) )
print( 'bark   = ', callable(bark) )
print( 'True   = ', callable(True) )

################################################################################





