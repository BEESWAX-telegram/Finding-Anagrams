# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    # [assignment] Add your code here


  sorted_word1 = sorted(word1)
  sorted_word2 = sorted(word2)

  if (sorted_word1 == sorted_word2):
     return True
  else:
     return False
word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

print (find_anagram(word1, word2))  #return True

