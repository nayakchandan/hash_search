"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

from re import search


def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for x in range(nbuckets)]

def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if type(o) == int:
        return o
    else:
        h = 0
        for i in range(len(o)):
            h=h*31+ord(o[i])
        return h

def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    pass

def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    nbuckets = len(table) # first we find the lenght of the hashtable, to use the modulo
    bucket = hashcode(key)%nbuckets # find the bucket using the hash function on key and then compressing

    # This gives the list containing all keys with the same encodings.
    search_region = table[bucket]
    # Linear search begins
    counter = []
    for element in search_region:
        k,v = element
        if k == key:
            counter.append(k)
            v.add(value)
            break # exit as no need to search any further
    if key not in counter: # no match found then create a new key,value pair
        #search_region.append(((key,{value})))
        if type(value)== int:
            search_region.append((key,{value}))
        else:
            search_region.append((key,value))

"""
def htable_put(table, key, value):

    nbuckets = len(table) # first we find the lenght of the hashtable, to use the modulo
    bucket = hashcode(key)%nbuckets # find the bucket using the hash function on key and then compressing

    # This gives the list containing all keys with the same encodings.
    search_region = table[bucket]
    # Linear search begins
    counter = []
    for element in search_region:
        k,v = element
        if k == key:
            counter.append(k)
            v.add(value)
            break # exit as no need to search any further
    if key not in counter: # no match found then create a new key,value pair
        #search_region.append(((key,{value})))
        if type(value)== int:
            search_region.append((key,{value}))
        else:
            search_region.append((key,value))
"""

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    nbuckets = len(table)
    bucket = hashcode(key)%nbuckets

    search_region = table[bucket]
    counter = []
    for element in search_region:
        k,v = element
        if k == key:
            counter.append(k)
            return v
    if len(counter) == 0:
        return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    content = ''
    for i in range(len(table)):
        #bucket = table[i]
        padding = 4-len(str(i))
        start = ('0'*padding+str(i)+"->")
        if len(table[i]) == 0:
            content=content+start+'\n'
            #print((i,content))
        else:
            values_str = ''
            for j in range(len(table[i])):
                k = table[i][j][0]
                v = table[i][j][1]
                values_str = values_str + str(k)+':'+",".join([str(x) for x in v])+', '
            content = content + start+values_str[:len(values_str)-2]+'\n'
            #content = content[:len(content)-2]
    return content


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    result = ''
    for i in range(len(table)):
        bucket = table[i]
        for pairs in bucket:
            if len(pairs) == 0:
                result = result +''
            else:
                key = pairs[0]
                value = pairs[1]
                val_expansion = ','.join(str(x) for x in value)
                result = result+str(key)+':'+val_expansion+", "
                #result = result+str(key)+':'+str(list(value)[0])+", "

    if result == '':
        return "{}"
    else:
        return "{"+result[:len(result)-2]+"}"

"""
    result = ''
    for i in range(len(table)):
        bucket = table[i]
        for pairs in bucket:
            if len(pairs) == 0:
                result = result +''
            else:
                key = pairs[0]
                value = pairs[1]
                result = result+str(key)+':'+str(list(value)[0])+", "


    if result == '':
        return "{}"
    else:
        return "{"+result[:len(result)-2]+"}"
"""
    
    

    