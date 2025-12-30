"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    separator = ' :: ' + vocab_words[0]
    return separator.join(vocab_words)


def remove_suffix_ness(word):
    wordToReturn = word[:-4] 
    wordToReturnLen = len(wordToReturn)

    if wordToReturn[wordToReturnLen - 1] == 'i':
        return wordToReturn[:-1] + 'y'
    
    return wordToReturn


def adjective_to_verb(sentence, index):
    word = sentence.split()[index].strip(".,!?")
    return word + "en"

