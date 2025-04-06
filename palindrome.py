def isaPalindrome(word=""):
    if len(word) <= 1:
        return True
    word = word.replace(" ", "")
    word = word.upper()
    if word[0] == word[-1] and isaPalindrome(word[1:--1]):
        return True
    return False
