
def char_to_unicode(c):
    return rf"\u{ord(c):04x}"

def string_to_unicode(word):
    return ''.join(char_to_unicode(c) for c in word)

def wordlist_to_unicode(words):
    return ' '.join(string_to_unicode(w) for w in words)

