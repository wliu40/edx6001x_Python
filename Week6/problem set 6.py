def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    def helper(index, num):        
        if (index+num) < 26:
            return index+num
        else:
            return (index+num)%26
    dic = {}
    for i in range(26):
        dic[string.ascii_lowercase[i]] = string.ascii_lowercase[helper(i, shift)]
        dic[string.ascii_uppercase[i]] = string.ascii_uppercase[helper(i, shift)]
    return dic
    
    
    ### TODO 


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    s = ''
    ex = string.punctuation + ' ' + '0123456789'
    for i in text:
        if i in ex:
            s += i
            continue
        s += coder[i]
    return s
    ### TODO


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    return applyCoder(text, buildCoder(shift))
    ### HINT: This is a wrapper function.


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


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    ciphertext = getStoryString()
    wordList = loadWords()
    shift = findBestShift(wordList, ciphertext)
    return applyShift(ciphertext, shift)

