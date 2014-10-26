# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    def insertAfter(atMe, newFrob):
        afterMe = atMe.getAfter()
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        if afterMe != None:
            newFrob.setAfter(afterMe)
            afterMe.setBefore(newFrob)
    
    def insertBefore(atMe, newFrob):
        beforeMe = atMe.getBefore()
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        if beforeMe != None:
            newFrob.setBefore(beforeMe)
            beforeMe.setAfter(newFrob)
            
    def insertRecursive(atMe, newFrob, seenFrobs, direction):
        if atMe == None and direction < 0:
            lastSeen = seenFrobs.pop()
            insertBefore(lastSeen, newFrob)
        elif atMe == None and direction > 0:
            lastSeen = seenFrobs.pop()
            insertAfter(lastSeen, newFrob)  
        elif atMe.myName() == newFrob.myName():
            insertAfter(atMe, newFrob)  
        elif (atMe in seenFrobs) and direction < 0:
            lastSeen = seenFrobs.pop()
            insertBefore(lastSeen, newFrob)
        elif (atMe in seenFrobs) and direction > 0: 
            lastSeen = seenFrobs.pop()
            insertAfter(lastSeen, newFrob)
             
        elif atMe.myName() > newFrob.myName():
            seenFrobs.append(atMe)
            insertRecursive(atMe.getBefore(), newFrob, seenFrobs, -1)
        elif atMe.myName() < newFrob.myName():
            seenFrobs.append(atMe)
            insertRecursive(atMe.getAfter(), newFrob, seenFrobs, 1)
                                    
    insertRecursive(atMe, newFrob, [], 0)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())
        
def printList(atMe):
    while atMe != None:
        print atMe.myName() + '-',
        atMe = atMe.getAfter()
         
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
insert(eric, Frob('martha'))
printList(ruth)
print
printList(findFront(ruth))                                