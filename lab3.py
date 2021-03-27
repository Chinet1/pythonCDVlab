# ZAD 1

def isPalindrome(text):
    return text == text[::-1]

print(isPalindrome(input("Wpisz tekst: ")))