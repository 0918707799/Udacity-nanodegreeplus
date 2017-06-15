
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
print "-should be \"qwertytrewq\"-"

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

# Question3

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def KruskalAlgo(g, c, reve):
    i = 0
    parent = list(range(c))
    rank = [0]*c
    final = []
    trial = []
    fin_res = {}

    for edge in range(c):
        a,b,c =  g[edge]
        x = find(parent, a)
        y = find(parent ,b)

        if x != y:
            final.append([a,b,c])
            rootx = find(parent, x)
            rooty = find(parent, y)

            if rank[rootx] < rank[rooty]:
                parent[rootx] = rooty
            elif rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            else :
                parent[rooty] = rootx
                rank[rooty] += 1

    for v1,v2,w in final:
        trial = [(reve[v2],w)]
        if reve[v1] not in fin_res:
            fin_res[reve[v1]] = trial
        else:
            fin_res[reve[v1]] = fin_res[reve[v1]].append(trial)
    return fin_res



def question3(G):
    if type(G) is not dict:
        return "not dictionary"
    if len(G) < 1:
        return G
    simple = []
    temp = {}
    reve = {}
    c = 0

    for i in G:
        temp[i] = c
        reve[c] = i
        c = c + 1

    for i in G:
        if len(G[i]) == 0:
            return "Dictionary has key without value"
        for j in G[i]:
            m,n,p = temp[i], temp[j[0]], j[1]
            simple.append([m,n,p])

    simple =  sorted(simple ,key=lambda item: item[2])

    return KruskalAlgo(simple, c, reve)


g1 = {'A': [('B', 2)],
    'B': [('A', 4), ('C', 2)],
    'C': [('A', 2), ('B', 5)]}

g2 = {'A': [('B', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}

g3 = "SDfsdf"

g4 = {'A': [],}

g5 = {}


print "___________________"
print "\ntest1__Q3"
print question3(g1)
print "-should be \"{'A': [('B', 2)], 'C': [('A', 2)]}\"-"

print "___________________"
print "\ntest2__Q3"
print question3(g2)
print "-should be \"{'A': [('B', 2)], 'C': [('B', 5)]}\"-"

print "___________________"
print "\ntest3__Q3"
print question3(g3)
print "-should be \"not dictionary\"-"

print "___________________"
print "\ntest4__Q3"
print question3(g4)
print "-should be \"Dictionary has key without value\"-"

print "___________________"
print "\ntest5__Q3"
print question3(g5)
print "-should be \"{}\"-"
