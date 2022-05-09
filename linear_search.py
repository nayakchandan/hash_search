# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words

def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    # save file name 
    register = []  # list to hold filepaths which contain the search terms
    '''
    Iterate through the files present in files list and check for intersection in the search terms
    '''
    for file in files:
        #f = open(file,encoding='latin-1').read()
        s = get_text(file)
        s = words(s)
        if len(set(s).intersection(set(terms)))==len(terms):
            register.append(file)

    return register
