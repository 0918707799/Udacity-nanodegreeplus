"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter...ord()

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
        self.dicty = {}
        

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        self.dicty[self.calculate_hash_value(string)] = string
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        for key,value in self.dicty.iteritems():
            if value ==  string:
                return key
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        a = []
        counter = 0
        for i in string:
            if (counter > 1):
                break
            a.append(i)
            counter =+ 1
        has_val = (ord(a[0])*100) + ord(a[1])
        return has_val
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')

