from .methods import get_names

class HashTable:
    def __init__(self, size, Dict={}):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.Dict = Dict
        self.position = 0
        for k,v in self.Dict.items():
            self.put(k, v)
            
    def put(self, key, data):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data    #replace
            else:
                next_slot = self.rehash(hash_value)
                while (self.slots[next_slot] is not None and
                        self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data     # replace

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def get(self, key):
        start_slot = self.hash_function(key)

        data = None
        stop = False
        found = False
        position = start_slot
        while (self.slots[position] != None and 
                not found and 
                not stop): 
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        return data

    def __len__(self):
        return self.size
    
    def __bool__(self):
        return self.size != 0
    
    def __repr__(self):
        D = dict(zip(self.slots, self.data))
        s = f"{self.size}, " + "{"
        for key in D:
            s = s + f"{repr(key)}:{repr(D[key])}, "
        return 'HashTable(' + s + '})'
    
    def __str__(self):
        return f'Hashtable({self.size})'
    
    def __getitem__(self, key):
        val = self.get(key)
        if not val:
            raise KeyError
        
        return val
    
    def __setitem__(self, key, data):
        self.put(key, data)
        
    def __delitem__(self, key):
        if key in self.slots:
            self.data[self.slots.index(key)] = None
            self.slots[self.slots.index(key)] = None
        else:
            raise KeyError
                
    def __contains__(self, item):
        return item in self.slots
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= self.size:
            self.position = 0
            raise StopIteration
        for i in range(self.position, len(self.slots)):
            self.position = i+1
            if self.slots[i] is not None:
                return self.slots[i]
            

if __name__ == '__main__':
    names = get_names()
    print(names[0])
    #names = [(item.split()[0], item.split()[3]) for item in names]
    #print(names)
    h = HashTable(20)
    h[40] = 'rohan'
    h[30] = 'random'
    print(h)
    print(h.slots)
    print(h.data)


