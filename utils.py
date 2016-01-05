def patternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count+=1                
    return count



def symbolToNumber(c):
    charToNum = {
        'A': 0 ,
        'C': 1 ,
        'G': 2 ,
        'T': 3
    }
    
    if c=='A':
        return 0
    elif c=='C':
        return 1
    elif c=='G':
        return 2
    elif c=='T':
        return 3
    else:
        raise "Please give ACGT"

def numberToSymbol(c):
    if c==0:
        return 'A'
    elif c==1:
        return 'C'
    elif c==2:
        return 'G'
    elif c==3:
        return 'T'
    return "false"

def numberToPattern(index , k):
    res = ""
    for i in range(k):
        res += numberToSymbol(index%4)
        index //= 4
    return res[::-1]
    
def patternToNumber(pattern):
    res = 0
    for i in range(len(pattern)):
        res*=4
        res+= symbolToNumber(pattern[i])
    return res

def frequentWords(text,k):
    frequentPatterns = set()
    count = [0 for i in range(len(text))]
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        count[i] = patternCount(text,pattern)
    maxCount = max(count)
    for i in range(len(text)-k+1):
        if count[i]==maxCount:
            frequentPatterns.add(text[i:i+k])
    return frequentPatterns

def computingFrequencies(text,k):
    frequencyArray = [0 for i in range(4**k)]
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = patternToNumber(pattern)
        frequencyArray[j] += 1
    return frequencyArray
                       

def fasterFrequentWords(text, k):
    frequentPatterns = set()
    frequencyArray = computingFrequencies(text,k)
    maxCount = max(frequencyArray)
    for i in range(4**k):
        if frequencyArray==maxCount:
            pattern = NumberToPattern(i,k)
            frequentPatterns.add(pattern)
    return frequentPatterns


def findingFrequentWordsBySorting(text,k):
    pass

def neucleotideComplement(n):
    relations ={
        'A':'T',
        'T':'A',
        'G':'C',
        'C':'G'
    }
    if n in relations.keys():
        return relations[n]
    else:
        return False
def reverseComplement(dna):
    res = ''
    for i in range(len(dna)-1,-1,-1):
        res+=neucleotideComplement(dna[i])
    return res


def patternMatchPos(pattern,text):
    res = []
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            res.append(i)
    return res
