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



def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value

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
    
    

    
