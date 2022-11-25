import random
encPass = (
    ('a', '@'),
    ('A', '@'),
    ('s', '$'),
    ('S', '$'),
    ('and', '&&'),
    ('AND', '&&'),
    ('b', 'x#y#b!'),
    ('B', '!x#y#B'),
    ('c', 'x#y#!c'),
    ('C', 'x!#y#C'),
    ('d', 'x#y#d$'),
    ('D', 'x$#y#D'),
    ('123', 'x#1#y$%$#2#z#3#'),
    ('321', 'x%$$#3#y#2#z#1#'),
)


def strPass(pasw):
    for i in range(3):
        pasw += pasw
    return pasw


def secPass(password):
    for a, b in encPass:
        password = password.replace(a, b)
    return strPass(password)


def genSecKey(leng=20):
    word = "abcdefghijklmnopqrstuvwxyz"
    WORDe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = 1234567890
    speChar = "@|%^$&"
    key = ""

    for i in range(leng):
        key += random.choice(word)
        key += random.choice(WORDe)
        key += random.choice(str(num))
        key += random.choice(speChar)

    return key


# if __name__ == "__main__":
#     print(genSecKey())