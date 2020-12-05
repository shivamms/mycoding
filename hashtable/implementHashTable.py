class hashTable:
    def __init__(self, key=None, value=None):
        self.keyvalues = [[None,None] for i in range(1000)]
        self.hash = 0
        if key is not None:
            self.hash = self.getHash(key)
            self.keyvalues[self.hash][0] = key
            self.keyvalues[self.hash][1] = value

    def getHash(self, key):
        self.hashnumber = 0
        for c in key:
            self.hashnumber = (self.hashnumber + ord(c))
        return self.hashnumber

    def getValue(self, key):
        self.hashnumber = self.getHash(key)
        return self.keyvalues[self.hashnumber][1]

    def setValue(self, key, value):
        self.hashnumber = self.getHash(key)
        self.keyvalues[self.hashnumber][0] = key
        self.keyvalues[self.hashnumber][1] = value

  