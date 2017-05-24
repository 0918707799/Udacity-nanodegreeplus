# Question1

def question1(s, t):
    if t in s:
        return True
    elif t[::-1] in s:
        return True
    else:
        return False

# testcase for first questions
print "\ntest1"
print question1("abcdefghij", "ed")
print "-should be True-"

print "___________________"
print "\ntest3"
print question1("dancetime", "fun")
print "-should be False-"

print "___________________"
print "\ntest2"
print question1("hellohowareyou", "era")
print "-should be True-"

print "___________________"
print "\ntest3"
print question1("jamesbond", "almno")
print "-should be False-"
