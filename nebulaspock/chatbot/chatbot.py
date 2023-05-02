import json
import logging
import random
import string

import nltk
import numpy as np
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

logger = logging.getLogger(__name__)


intents_file = open('data.corpus.json', 'rb').read()
data = json.loads(intents_file)
print(data)

nltk.download("punkt")
nltk.download("wordnet")

# initializing lemmatizer to get stem of words
lemmatizer = WordNetLemmatizer()
# Each list to create
words = []
classes = []
doc_X = []
doc_y = []
# Loop through all the intents
# tokenize each pattern and append tokens to words, the patterns and
# the associated tag to their associated list
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        doc_X.append(pattern)
        doc_y.append(intent["tag"])

    # add the tag to the classes if it's not there already
    if intent["tag"] not in classes:
        classes.append(intent["tag"])
# lemmatize all the words in the vocab and convert them to lowercase
# if the words don't appear in punctuation
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]
# sorting the vocab and classes in alphabetical order and taking the # set to ensure no duplicates occur
words = sorted(set(words))
classes = sorted(set(classes))

# list for training data
training = []
out_empty = [0] * len(classes)
# creating the bag of words model
for idx, doc in enumerate(doc_X):
    bow = []
    text = lemmatizer.lemmatize(doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)
    # mark the index of class that the current pattern is associated
    # to
    output_row = list(out_empty)
    output_row[classes.index(doc_y[idx])] = 1
    # add the one hot encoded BoW and associated classes to training
    training.append([bow, output_row])
# shuffle the data and convert it to an array
random.shuffle(training)
training = np.array(training, dtype=object)
# split the features and target labels
train_X = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# defining some parameters
input_shape = (len(train_X[0]),)
output_shape = len(train_y[0])
epochs = 200
# the deep learning model
model = Sequential()
model.add(Dense(128, input_shape=input_shape, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(output_shape, activation="softmax"))
adam = tf.keras.optimizers.Adam(learning_rate=0.01, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=["accuracy"])

model.fit(x=train_X, y=train_y, epochs=200, verbose=1)


def clean_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens


def bag_of_words(text, vocab):
    tokens = clean_text(text)
    bow = [0] * len(vocab)

    for w in tokens:
        for idx, word in enumerate(vocab):
            if word == w:
                bow[idx] = 1
    return {"bow": np.array(bow), "tokens": tokens}


def pred_class(text, vocab, labels):
    bow_results = bag_of_words(text, vocab)
    result = model.predict(np.array([bow_results["bow"]]))[0]
    thresh = 0.2
    y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

    y_pred.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in y_pred:
        return_list.append(labels[r[0]])
    return {"intents": return_list, "tokens": bow_results["tokens"]}


def get_response(intents_list, intents_json):
    tag = intents_list[0]
    list_of_intents = intents_json["intents"]
    response = {}
    for i in list_of_intents:
        if i["tag"] == tag:
            response["response"] = random.choice(i["responses"])
            response["query"] = i["query"]
            response["phrases"] = i["phrases"]
            response["entities"] = i["entities"]
            response["parameters"] = i["parameters"]
            break
    return response


def get_phrases(filtered, data):
    tokens = filtered["tokens"]
    phrases = data["phrases"]
    parameters = data["parameters"]
    print(parameters)
    results = []
    # logger.info("phrases:{phrases},tokens:{tokens}".format(tokens=tokens, phrases=phrases))
    if len(phrases) > 0:
        for phrase in phrases:
            for index, token in enumerate(tokens):
                if phrase.upper() == token.upper():
                    left = 0 if index - 1 == -1 else index - 1
                    right = len(tokens) if index + 1 > len(tokens) else index + 1
                    for param in parameters:
                        for key in param:
                            lexicon = [i for i in param[key].split(",") if i.upper() == phrase.upper()]
                            if len(lexicon) > 0:
                                results.append({'phrase': key, 'left': tokens[left], 'right': tokens[right]})

    data["corpus"] = results


def return_response(message):
    filtered = pred_class(message, words, classes)
    result = get_response(filtered["intents"], data)
    get_phrases(filtered, result)
    logger.info("result:{filtered}".format(filtered=result))
    return result

#   # running the chatbot
# while True:
#     message = input("")
#     intents = pred_class(message, words, classes)
#     result = get_response(intents, data)
#     print(result)
