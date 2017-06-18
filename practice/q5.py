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
