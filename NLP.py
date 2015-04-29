#Problem 0

def unpunctuate(sentence):  
    import re, string
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    return regex.sub('', sentence)

unpunctuate("Hey there! How's it going?")


#Problem 1

def get_bag_of_words_for_single_document(single_document):
    word_array = single_document.split()
    bag_of_words = {}
    for word in word_array:
        bag_of_words[word]=0
    for word in word_array:
        if word == word in bag_of_words:
            bag_of_words[word] += 1
    return bag_of_words

get_bag_of_words_for_single_document("John and John also like to play football")


#Problem 2

def get_bag_of_words(documents):
    word_array=[]
    for doc in documents:
        word_array += doc.split()
    bag_of_words = {}
    for word in word_array:
        bag_of_words[word]=0
    for word in word_array:
        if word == word in bag_of_words:
            bag_of_words[word] += 1
    return bag_of_words
        
get_bag_of_words([
    "John likes to watch movies. Mary likes movies too.",
    "John also likes to watch football games."
])


#Problem 3

def turn_words_into_indices(bag_of_words_data):
    list_of_words = []
    for key, value in bag_of_words_data.iteritems():
        list_of_words.append(key)
    return list_of_words

bag_of_words_data = {
    "John": 1,
    "likes": 2,
    "to": 3,
    "watch": 4,
    "movies": 5,
    "also": 6,
    "football": 7,
    "games": 8,
    "Mary": 9,
    "too": 10
}

turn_words_into_indices(bag_of_words_data)


#Problem 4

def vectorize(document):
    key = ["also", "football", "games", "John", "likes", "Mary", "movies", "to", "too", "watch"]
    word_array = document.split()
    vectorized = []
    for word in word_array:
        if word in key:
            vectorized.append(1)
        else:
            vectorized.append(0)
    return vectorized

vectorize("The sun also rises. Let's go to the movies")
