
def question1(s, t):
    if t in s:
        return True
    elif t[::-1] in s:
        return True
    else:
        return False

# testcase for first questions
print "\ntest1__Q1"
print question1("abcdefghij", "ed")
print "-should be True-"

print "___________________"
print "\ntest2__Q1"
print question1("dancetime", "fun")
print "-should be False-"

print "___________________"
print "\ntest3__Q1"
print question1("hellohowareyou", "era")
print "-should be True-"

print "___________________"
print "\ntest4__Q1"
print question1("jamesbond", "almno")
print "-should be False-"


def question2(a):
    length = len(a)
    start = -1
    end = -1
    final_end = -1
    final_start = -1
    diff = 0

    # single char string is always palindromic
    if length == 1:
        return a
    for i in range(0,length):
        if i > (length/2):
            trial = length - i
        else:
            trial = i
        for j in range(1, trial):
            if (i-j) > 0 or (i+j) < length or (j-i) != (j+i):
                if a[i-j] == a[i+j]:
                    start = i-j
                    end = i+j
                else:
                    break
        if (end-start) > diff:
            diff = end - start
            final_end = end
            final_start = start
    if diff == 0:
        return None
    else:
        return a[final_start:final_end+1]

print "___________________"
print "\ntest1__Q2"
print question2("abqwertytrewqcdeyeheyeye")
print "-should be \"qwertytrewq\"="

print "___________________"
print "\ntest2__Q2"
print question2("abeyej")
print "-should be \"eye\"-"

print "___________________"
print "\ntest3__Q2"
print question2("a")
print "-should be \"a\"-"

print "___________________"
print "\ntest4__Q2"
print question2("qwertyuioopxfcgh")
print "-should be \"None\"-"
