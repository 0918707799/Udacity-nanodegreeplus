# Question3
parent = {}

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

print question3(g1)
# {'A': [('B', 2)], 'C': [('A', 2)]}

print question3(g2)
# {'A': [('B', 2)], 'C': [('B', 5)]}

print question3(g3)
# not dictionary

print question3(g4)
# Dictionary has key without value

print question3(g5)
# {}


# references:
# http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/GraphAlgor/kruskalAlgor.htm
#  https://www.ics.uci.edu/~eppstein/PADS/MinimumSpanningTree.py
