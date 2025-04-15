# def find_anagrams(word, candidates):
#     anagrams = []

#     for i in candidates:
#         if len(i) == len(word) and i.lower() != word.lower():
#             word_copy = list(word.lower())
#             for x in i:
#                 if x.lower() in word_copy:
#                     word_copy.remove(x.lower())
#             if word_copy == []:
#                  anagrams.append(i)

#     return anagrams

#Chat GPT version
def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)

    return [w for w in candidates if w.lower() != word_lower and sorted(w.lower()) == sorted_word]