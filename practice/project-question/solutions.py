
# Question1
def question1(s, t):
    """returns true or false based on existance of anagram substring in a string"""
    if t in s:
        return True
    elif t[::-1] in s:
        return True
    else:
        return False
print "\n________________________Q1________________________"
# testcase for first questions
print "\n\n--> test1__Q1", "\t(should be \"True\")"
print question1("abcdefghij", "ed")

print "\n\n--> test2__Q1", "\t(should be \"False\")"
print question1("dancetime", "fun")

print "\n\n--> test3__Q1" "\t(should be \"True\")"
print question1("hellohowareyou", "era")

print "\n\n--> test4__Q1", "\t(should be \"False\")"
print question1("jamesbond", "almno")

print "\n\n--> test5__Q1", "\t(should be \"False\")"
print question1("", "almno")

# Question2
def question2(a):
    """returns the longest palindromic substring in given string"""
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
        # if current char is at n, then compares the char at (n-1,n-2,n-3,.., n-m) and (n+1,n+2,n+3,.., n+m) until they mismatche
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
        # this means there is no palindromic substring in the string
        return None
    else:
        return a[final_start:final_end+1]

print "\n________________________Q2________________________"
print "\n\n--> test1__Q2", "\t(should be \"qwertytrewq\")"
print question2("abqwertytrewqcdeyeheyeye")

print "\n\n--> test2__Q2", "\t(should be \"eye\")"
print question2("abeyej")

print "\n\n--> test3__Q2", "\t(should be \"a\")"
print question2("a")

print "\n\n--> test4__Q2", "\t(should be \"None\")"
print question2("qwertyuioopxfcgh")

print "\n\n--> test5__Q2", "\t(should be \"None\")"
print question2("")

# Question3

def find(parent, i):
    """returns the set of an element i"""
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

    # iterating through all the edges in the given graph
    for edge in range(c):
        a,b,c =  g[edge]
        x = find(parent, a)
        y = find(parent ,b)

        if x != y:
            final.append([a,b,c])
            rootx = find(parent, x)
            rooty = find(parent, y)

            # sorting tree based on ranking of tree and finding union of them
            if rank[rootx] < rank[rooty]:
                parent[rootx] = rooty
            elif rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            else :
                # one will be root if they have sam rank
                parent[rooty] = rootx
                rank[rooty] += 1

    for v1,v2,w in final:
        trial = [(reve[v2],w)]
        if reve[v1] not in fin_res:
            fin_res[reve[v1]] = trial
        else:
            fin_res[reve[v1]] = fin_res[reve[v1]].append(trial)
    return fin_res

# Question3
def question3(G):
    """returns the minimum spanning tree using kruskal's algo"""
    if type(G) is not dict:
        return "not dictionary"
    if len(G) < 1:
        return G
    simple = []
    temp = {}
    reve = {}
    c = 0

    # creating dict with node(key) and the position of the node(value)
    for i in G:
        temp[i] = c
        reve[c] = i
        c = c + 1

    for i in G:
        if len(G[i]) == 0:
            return "Dictionary has key without value"
        # converting graph into matrix form and saving them into list
        for j in G[i]:
            m,n,p = temp[i], temp[j[0]], j[1]
            simple.append([m,n,p])
    # sorting created list based on the value of weight
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

print "\n________________________Q3________________________"
print "\n\n--> test1__Q3", "\t(should be \"{'A': [('B', 2)], 'C': [('A', 2)]}\")"
print question3(g1)

print "\n\n--> test2__Q3", "\t(should be \"{'A': [('B', 2)], 'C': [('B', 5)]}\")"
print question3(g2)

print "\n\n--> test3__Q3", "\t(should be \"not dictionary\")"
print question3(g3)

print "\n\n--> test4__Q3", "\t(should be \"Dictionary has key without value\")"
print question3(g4)

print "\n\n--> test5__Q3", "\t(should be \"{}\")"
print question3(g5)

# Question4
def question4(T, r, n1, n2):
    """retruns the common least common ancestor"""
    if len(T) == 0:
        print "empty BST matrix"
        return None
    elif len(T) == 1:
        if n1 == n2 and n1 == r:
            return r
        elif n1 != len(T) or n2 != len(T):
            print "unappropriate n1/n2 for given matrix"
            return None
        else:
            return r

    temp = []
    dicti = {}
    # creating dictionary with node as key and list of child as value
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 1:
                temp.append(j)
                dicti[i] = temp
        temp = []


    path1 = []
    path2 = []

    # iterating through created dict and trying to match up n1 , n2 and to eleminate common path using abcd variable
    for a in dicti:
        for value in dicti.values():
            if a == value or a in value:
                abcd = a
            if n1 in dicti[a]:
                path1 = a
            if n2 in dicti[a]:
                path2 = a
    # print path1, path2, abcd
    if abcd == path1:
        return path2
    elif abcd == path2:
        return path1

print "\n________________________Q4________________________"
print "\n\n--> test1__Q4", "\t(should be \"3\")"
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)

print "\n\n--> test2__Q4", "\t(should be \"empty BST matrix -newline- None\")"
print question4([],
                None,
                None,
                None)

print "\n\n--> test3__Q4", "\t(should be \"unappropriate n1 for given matrix -newline- None\")"
print question4([[1]],
                1,
                0,
                7)

print "\n\n--> test4__Q4", "\t(should be \"7\")"
print question4([[7]],
                7,
                7,
                7)

print "\n\n--> test5__Q4", "\t(should be \"1\")"
print question4([[0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                1,
                0,
                6)

class Node(object):
    """class of the Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def ll_length(link):
    if link is None:
        return 0
    else:
        c = 0
        while (link):
            c += 1
            link = link.next
        return c + 1

def question5(ll, m):
    """returns the node at the given m -- vounting from the lsat """
    if type(ll) == int or type(ll) == str:
        return None
    counter = 1
    current = ll
    max_len = ll_length(ll)
    m = max_len - m
    if m < 1:
        return None
    while current and counter <= m:
        # iterating through the linked list and if it finds the mth element then returns it or else goes to the next
        if counter == m:
            return current.data
        current = current.next
        counter += 1
    return None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

print "\n________________________Q5________________________"
print "\n\n--> test1__Q5", "\t(should be \"4\")"
print question5(n1, 5)

a =""
print "\n\n--> test2__Q5", "\t(should be \"None\")"
print question5(a, 5)

b1 = Node(1)
print "\n\n--> test3__Q5", "\t(should be \"None\")"
print question5(b1, 5)

c = 55
print "\n\n--> test4__Q5", "\t(should be \"None\")"
print question5(c, 1)

d = "hello udacity"
print "\n\n--> test5__Q5", "\t(should be \"None\")"
print question5(c, 7)
