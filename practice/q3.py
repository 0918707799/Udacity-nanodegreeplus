# Question2

def question3(G):
    simple = {}
    count = 0
    for i in G:
        for j in G[i]:
            if count == 0:
                maxim = j[1]+1
            if j[1] < maxim:
                simple = {}
                maxim = j[1]
                simple[i] = j
            elif j[1] == maxim:
                if i in simple:
                    simple[i] = [simple[i]]
                    simple[i].append(j)
                else:
                    simple[i] = j
            count = count + 1

    print simple


g = {'A': [('B', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}

question3(g)
