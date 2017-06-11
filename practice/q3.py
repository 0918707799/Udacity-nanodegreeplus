# Question2

def question3(G):
    simple = {}
    tup = ()
    maxim = 111111111
    for i in G:
        for j in G[i]:
            if j[1] < maxim:
                simple = {}
                maxim = j[1]
                simple[i]=j
            elif j[1] == maxim:
                simple[i]=j

    print simple


g = {'A': [('BB', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}

question3(g)
