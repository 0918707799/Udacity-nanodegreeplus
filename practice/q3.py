# Question2

def question3(G):
    for i in G:
        print i
        print G[i][0]


g = {'A': [('BB', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}

question3(g)
