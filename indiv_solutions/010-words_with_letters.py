def words_with_letters(words, letters):
    def is_subsequence(word, letters):
        idx = 0
        for i in word:
            if i == letters[idx]:
                idx += 1
                if idx == len(letters):
                    return True
        return False
    
    return list(filter(lambda x: is_subsequence(x, letters), words))