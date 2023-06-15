# create a function that iterates though the list finding
# words in the list that are similar then sort them the check if any equal 

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):

        matching_word = sorted(self.word)
        indices = [index for index, w in enumerate(words) if sorted(w) == matching_word]
        
        return[words[index] for index in indices]