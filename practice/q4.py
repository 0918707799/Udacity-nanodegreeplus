def question4(T, r, n1, n2):
    if len(T) == 0:
        return T
    elif len(T) == 1:
        return r

    temp_root1 = []
    temp1 = -1
    temp_root2 = []
    temp2 = -1
    for i in range(len(T)):
        if i == r:
            break
        if T[i][n1] == 1:
            print n1
            n1 = i
            temp_root1.append(i)
    for j in range(len(T)):
        print n2
        if j == r:
            print "________", j
            break
        if T[i][n2] == 1:
            n2 = j
            temp_root2.append(j)

    print temp_root1, temp_root2

    for a1 in temp_root1:
        for a2 in temp_root2:
            if a1 == a2:
                return a1




print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
