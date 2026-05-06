def palindrome(string):
    lpos = 0#lpos=left rpos =right
    rpos = len(string)-1
    while rpos >= lpos:
        if string[lpos] != string[rpos]:
            return False
        lpos += 1
        rpos -= 1
        
    return True
print(palindrome('naman'))
print(palindrome('adit'))