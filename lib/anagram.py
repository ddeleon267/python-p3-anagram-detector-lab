# your code goes here!
class Anagram():

    def __init__(self, word):
        self._word = word
        return None
    
    def match(self, array):
        # print("SELF IS!", self.word)
        # return None
        # turn word into a list and sort
        word_chars = sorted([letter for letter in self._word])
        anagrams = []
        for maybe_match in array:
            match_chars = sorted([letter for letter in maybe_match])
            if word_chars == match_chars:
                anagrams.append(maybe_match)
        
        return anagrams

        # go through array
            # for each item, turn into list and sort
            # is it equal to the given word?
#             ## return it as part of a list

## solution passes test, but would give false matches for words with same chars but diff length
#    def match(self, list):
#         return [word for word in list if set(word) == set(self._word)]