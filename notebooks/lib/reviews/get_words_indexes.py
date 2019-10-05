def get_words_indexes(words_indexes_dictionary, review):
    words = review.split(' ')
    words_indexes = set()
    
    for word in words:
        if word in words_indexes_dictionary:
            word_index = words_indexes_dictionary[word]
            words_indexes.add(word_index)
            
    return words_indexes