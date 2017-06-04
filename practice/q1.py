# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s, t):
    if t in s:
        return True
    elif t[::-1] in s:
        return True
    else:
        return False

print "\ntest1"
print question1("abcdefghij", "ed")
print "-should be True-"

print "___________________"
print "\ntest2"
print question1("abcdefghij", "de")
print "-should be True-"

print "___________________"
print "\ntest3"
print question1("abcdefghij", "xe")
print "-should be False-"

print "___________________"
print "\ntest3"
print question1("abcdefghij", "aj")
print "-should be False-"

print "___________________"
print "\ntest3"
print question1("abcdefghij", "fj")
print "-should be False-"

print "___________________"
print "\ntest3"
print question1("abcdefghij", "mn")
print "-should be False-"
