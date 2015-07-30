def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    def translate(text, k):    
        s = applyShift(text, 26-k) #get the original text        
        ex = string.punctuation + '0123456789'        
        for i in s:
            if i in ex:
                s = s.replace(i, " ")
        res = s.split(' ')
        return res
      
    ans, maxVal = 0, 0
    for k in range(1, 26):
        count = 0
        for word in translate(text, k):
            if isWord(wordList, word):
                count += 1
        if count > maxVal:
            maxVal = count
            ans = 26- k
    return ans
    ### TODO
