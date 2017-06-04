# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

# NOTE:
# if string has two similar length palindromic substring then function will return the first substring


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

# ans should be "qwertytrewq"
print question2("abqwertytrewqcdeyeheyeye")

# ans should be "eye"
print question2("abeyej")

# ans should be "a"
print question2("a")

# ans should be "None"
print question2("qwertyuioopxfcgh")
