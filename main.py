#try to find anagram of two words
def find_anagram(word, anagram):
    
    # Get lengths of both strings
    n1 = len(word)
    n2 = len( anagram)
  
    
    if n1 != n2:
        return 0
  
    # Sorting both strings
    word = sorted(word)
    anagram = sorted( anagram)
  
    # Compare sorted strings
    for i in range(0, n1):
        if word[i] !=  anagram[i]:
            return 0
  
    return 1
  
# anagram comparison
word = "reason"
anagram = "arsone"
  
# Function Call
if find_anagram(word,  anagram):
    print(
    "True")
else:
    print(
    "False")

    

