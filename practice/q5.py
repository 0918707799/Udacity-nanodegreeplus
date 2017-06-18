class Node(object):
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
    counter = 1
    current = ll
    max_len = ll_length(ll)
    m = max_len - m
    if m < 1:
        return None
    while current and counter <= m:
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
print question5(n1, 5)
# Should print 4

b =""
print question5(b, 5)
