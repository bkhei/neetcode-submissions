# Reverse the string and if it's equal return true
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.replace(" ", "") # Remove spaces
        stripped = stripped.lower() # Convert to lowercase
        finalString = "" # Create final string
        
        for char in stripped: # For each letter in the string
            if char in "abcdefghijklmnopqrstuvwxyz0123456789": # If the character
                finalString += char # If we don't have alphanumerics remove the letter

        finalStringReverse = finalString[::-1]

        if finalStringReverse == finalString:
            return True
        else:
            return False