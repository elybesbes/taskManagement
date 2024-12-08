#Function to lowercase all caracters
def all_lower(my_list):
    return [x.lower() for x in my_list]

#Function to check if a string is palindrome
def isPalindrome(s):
    return s == s[::-1]

#Function to remove a non alphnumeric caracters
def removeNonAlpha(text):
    for i in text:
        if i.isalnum()==False:
            text = text.replace(i,"")
    return text

#Function to verify if text is palindrome
def textPalindrome(text):
    return isPalindrome(all_lower(removeNonAlpha(text)))

text = "Madam, in Eden, I'm Adam"
text1="Complete the project report"
print(textPalindrome(text))
print(textPalindrome(text1))