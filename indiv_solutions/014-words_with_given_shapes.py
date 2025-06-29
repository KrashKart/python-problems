def words_with_given_shape(words, shape):
    def has_shape(word, shape):
        if len(word) != len(shape) + 1:
            return False
        for i in range(len(shape)):
            if shape[i] == 0 and ord(word[i]) != ord(word[i+1]):
                return False
            elif shape[i] * ord(word[i]) >= shape[i] * ord(word[i+1]) and shape[i] != 0:
                return False
        return True
    return list(filter(lambda x: has_shape(x, shape), words))
