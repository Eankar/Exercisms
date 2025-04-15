def is_pangram(sentence):
    
    letters = set("abcdefghijklmnopqrstuvwxyz")

    if len(set(sentence.lower()) & letters) == 26:
        return True
    else:
        return False