import sys
import string

file_source = open("/Users/kadeempalacios/Desktop/python/ThePictureOfDorianGray.txt", "r")
content = file_source.read()
content_stripped = content.translate(None, string.punctuation)
content_split = content_stripped.split()
unique_word_dict = dict()



def histogram(source_text):

    for index in range(0, len(source_text)):
        current_word = source_text[index]
        if current_word not in unique_word_dict:
            unique_word_dict.update({current_word: 1})
        elif current_word in unique_word_dict:
            unique_word_dict[current_word] += 1
    
    return unique_word_dict


def unique_words(histogram_source):
    print  len(histogram_source)
    return len(histogram_source)


histogram(content_split)
unique_words(unique_word_dict)

def frequency(word, histogram):
    print histogram[word]
    return histogram[word]

frequency("mirror",unique_word_dict)
