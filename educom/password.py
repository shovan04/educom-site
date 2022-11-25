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
