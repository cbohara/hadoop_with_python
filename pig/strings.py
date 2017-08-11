from pig_util import outputSchema

@outputSchema('word:chararray')
def reverse(word):
    return word[::-1]

@outputSchema('length:int')
def num_chars(word):
    return len(word)
