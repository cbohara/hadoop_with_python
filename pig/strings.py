from pig_util import outputSchema

@outputSchema('length:int')
def num_chars(word):
    return len(word)
