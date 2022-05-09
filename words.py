import os
import re
import string


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    files = []
    for (dirpath,dirname,filename) in os.walk(root,topdown=False):
        for file in filename:
            pp = os.path.join(dirpath,file)
            files.append(pp)
    return files

def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s

def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """

    content = ''
    for i in range(min(100,len(docs))):
        line = return_line(docs[i],terms)
        hyper = f"\t\t\t<p><a href=\"file://{str(docs[i])}\">{str(docs[i])}"+"</a><br>"+line+"<br><br>\n"
        content = content+hyper
    terms_expansion = ' '.join(terms)
    begin = "<html>\n\t<body>"
    headline = "\t\t<h2>Search results for </b>"+terms_expansion+"</b> in "+ str(len(docs)) + " files</h2>"
    end = "\t</body>\n</html>"

    return begin+headline+content+end

def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

def return_line(doc,terms):
    """
    takes in a file on disk and returns the lines containing the search terms
    """
    text = open(doc).read().splitlines()
    for lines in text:
        if lines.lower().find(terms[0]) != -1:
            return (lines)