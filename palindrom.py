def is_palindrome(word):
    reversed_word=word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
print(is_palindrome("ajay"))
print(is_palindrome("madam"))        



# another way of palindrome using function

def is_palindrome(word):
    if word==word[::-1]:
        return "palindrome"
    return "not palindrome"
print(is_palindrome("akhilesh"))    
print(is_palindrome("naman")) 



# one more logic or palindrome

def is_palindrome(word):
    return word==word[::-1]
print(is_palindrome("akhilesh")) 
print(is_palindrome("naman"))    