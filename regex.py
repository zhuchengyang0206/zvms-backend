import re

def encode(a):
    a = re.sub("/", "~s", a) # slash
    a = re.sub(" ", "~e", a) # empty
    a = re.sub('"', "~d", a) # double quote
    a = re.sub("'", "~q", a) # quote

def decode(a):
    a = re.sub("~s", "/", a) # slash
    a = re.sub("~e", " ", a) # empty
    a = re.sub("~d", '"', a) # double quote
    a = re.sub("~q", "'", a) # quote
