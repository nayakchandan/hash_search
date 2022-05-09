from collections import defaultdict  # https://docs.python.org/2/library/collections.html
from operator import itemgetter
from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs.
    Return a dict object mapping a word to a set of doc IDs.
    """
    index = defaultdict(list) #dict object containing the list of data

    for i in range(len(files)):
        file = files[i]
        s = get_text(file)
        s = list(set(words(s)))
        for word in s:
            index[word].append(i)

    return index
            


def index_search(files, index, terms):

    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter 
    """
    # get a list of all files that contain each search term and append a list
    common_words = []
    for term in terms:
        common_words.append(set(index[term]))
    
    # perform set intersection on the list to get common doc ids
    if len(common_words) == 0:
        return []
    else:
        results = list(set.intersection(*common_words))
        if len(results) == 0:
            return []
        else:
            file_list = []
            for i in results:
                file_list.append(files[i])
            return file_list



    


    #return - list object 
