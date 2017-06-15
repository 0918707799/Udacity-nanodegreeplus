def question4(T, r, n1, n2):
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
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 1:
                temp.append(j)
                dicti[i] = temp
        temp = []

    path1 = []
    path2 = []

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

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
# 3

print question4([],
                None,
                None,
                None)
# empty BST matrix
# None


print question4([[1]],
                1,
                0,
                7)
# unappropriate n1 for given matrix
# None

print question4([[7]],
                7,
                7,
                7)
# 1


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
# 2
