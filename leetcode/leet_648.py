def replaceWords(dictionary, sentence):
    dic = set(dictionary)     #hash set
    words = sentence.split(' ')  #spilt
    for i, word in enumerate(words):     # spilt and enumerate
        for j in range(1, len(words) + 1):   # a word  ef:sentence-> s st ste
            if word[:j] in dic:          #output
                words[i] = word[j]
                break
    return ' '.join(words)