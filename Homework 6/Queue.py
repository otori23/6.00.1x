class Queue(object):
    
    def __init__(self):
        self.elems = []
        
    def insert(self, e):
        self.elems.append(e)
        
    def remove(self):
        if len(self.elems) == 0:
            raise ValueError('Pop form empty list')
        return self.elems.pop(0)    