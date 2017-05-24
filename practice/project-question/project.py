# Question1

def question1(s, t):
    if t in s:
        return True
    elif t[::-1] in s:
        return True
    else:
        return False
