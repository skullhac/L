# Implementation of the Map ADT using closed hashing and a probe with
# double hashing.

from Chapter2.myarray import Array

# Storage class for holding the key/value pairs.
class _MapEntry( object ):
    def __init__( self, key, value ):
        self.key = key
        self.value = value

class HashMap:
    UNUSED = None
    EMPTY = _MapEntry( None, None )

    def __init__( self ):
        self._table = Array( 7 )
        self._count = 0
        self._maxCount = len( self._table ) - len( self._table ) // 3
        self._keylist = list()

    def __len__( self ):
        return self._count

    def __contains__( self, key ):
        slot = self._findSlot( key, False )
        return slot is not None
                
    # Adds a new entry to the map if the key does not exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add( self, key, value ):
        if key in self:
            slot = self._findSlot( key , False )
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot( key, True )
            #print slot
            self._table[slot] = _MapEntry( key, value )
            self._count += 1
            self._keylist.append(key)
            if self._count == self._maxCount:
                self._rehash()
            return True

    # Returns the value associated with the key.
    def valueOf( self, key ):
        slot = self._findSlot( key, False )
        assert slot is not None, "Invalid map key"
        return self._table[slot].value

    # Remove the entry associated with the key.
    def remove( self, key ):
        slot = self._findSlot( key, False )
        assert slot is not None, "Invalid map key"
        self._table[slot] = self.EMPTY
        self._count -= 1
        self._keylist.remove(key)

    # Returns an iterator for traversing the keys in the map.
    def __iter__( self ):       
        return _HashTableIterator( self._keylist )
        #pass

    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _findSlot( self, key, forInsert ):
        slot = self._hash1( key )
        #print 'slot', slot
        step = self._hash2( key )

        M = len( self._table )
        #print '..', self._table[slot]
        while self._table[slot] is not self.UNUSED:
            if forInsert and \
               (self._table[slot] is self.UNUSED or self._table[slot] is self.EMPTY):
                #print 'insert here'
                return slot
            elif not forInsert and \
                 (self._table[slot] is not self.EMPTY and self._table[slot].key == key):
                #print 'find it'
                return slot
            else:
                #print 'continue probe'
                slot = (slot + step) % M

        if forInsert:
            return slot
        else:
            return None

    # Rebuilds the hash table.
    def _rehash( self ):
        oriTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array( newSize )

        self._count = 0
        self._maxCount = newSize - newSize // 3

        for entry in oriTable:
            if entry is not self.UNUSED and entry is not self.EMPTY:
                slot = self._findSlot( entry.key, True )
                self._table[slot] = entry
                self._count += 1

    # The main hash function for mapping keys to table
    def _hash1( self, key ):
        return abs( hash(key) ) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2( self, key ):
        return 1 + abs( hash(key)) % (len(self._table) - 2)

class _HashTableIterator:
    def __init__( self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ):
            entry = self._arrayRef[ self._curNdx ]
            #print (entry)
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

if __name__ == '__main__':
    mydict = HashMap()
    mydict.add( 45, 100 )
    mydict.add( 23, 20 )
    mydict.add( 2, 86 )
    mydict.add( 64, 90 )

    print('M: %d' % len(mydict))
    print('N: %d' % len(mydict._table))
    for key in mydict:
        print(key, mydict.valueOf(key))
    print ('===================')
    
    mydict.add( 123, 10)
    mydict.add( 73, 38)
    print ('M: %d' % len(mydict))
    print ('N: %d' % len(mydict._table))
    #print mydict.valueOf( 'James' )
    for key in mydict:
        print (key, mydict.valueOf(key))
    print ('===================')

    mydict.remove( 2 )
    #print mydict.valueOf( 'Ryuka' )
    print ('M: %d' % len(mydict))
    print ('N: %d' % len(mydict._table))
    for key in mydict:
        print (key, mydict.valueOf(key))
    print ('===================')

    

    

    
