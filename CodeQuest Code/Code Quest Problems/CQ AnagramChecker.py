"""
first check if length is same AND words arent exactly the same
then go thru and for each letter
THEN
to check if annagarm:
- count of each letter is same as in second word
"""
import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

def count_letters(word):
    word_letters = {}
    for letter in word:
            if letter in word_letters:
                word_letters[letter] += 1
            else: 
                word_letters.update({letter : 1})
    return word_letters

for case in inputs:
    words_pair = case.split('|')
    # check if lengths are same AND words arent equal
    if (words_pair[0] != words_pair[1]) and (len(words_pair[0]) == len(words_pair[1])):
        #check if each letter of word 1 is same as in word 2, and that they appear same amount of times in both
        #make dictionary of frequencies of each letter
        word_one_dict = count_letters(words_pair[0])
        word_two_dict = count_letters(words_pair[1])
        if(word_one_dict == word_two_dict):
            print(f"{words_pair[0]}|{words_pair[1]} = ANAGRAM")
        else:
            print(f"{words_pair[0]}|{words_pair[1]} = NOT AN ANAGRAM")


    else:
        print(f"{words_pair[0]}|{words_pair[1]} = NOT AN ANAGRAM")


