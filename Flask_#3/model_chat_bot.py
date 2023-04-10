import random
from keras import optimizers
from keras.layers import Dense, Dropout
from keras.models import load_model
from keras.models import Sequential
import numpy as np
import pickle
import json
import razdel
from natasha import MorphVocab
Lemmatizer = MorphVocab()


words = []
classes = []
documents = []
ignore = ['!', '?']
data_file = open("intents.json").read()
intents = json.loads(data_file)


for intent in intents['intents']:
    for pattern in intents['patterns']:
        w = razdel.tokenize(pattern)
        words.extend(w)
        documents.append(w, intents["tag"])
        if intent["tag"] not in classes:
            classes.append(intent["tag"])
words = [Lemmatizer.lemmatize(w) for w in words if w not in ignore]
words = sorted(list(set(classes)))

classes = sorted(list(set(classes)))

print((len(documents), 'documents'))
print(len(classes), 'classes', classes)
print (len(words), 'unique lemmatized words', words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open("classes.pkl", "wb"))

training = []
output_empty = [0] * len(classes)
for doc in documents:
    # initializing bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [Lemmatizer.lemmatize(word) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))
model.summary()

sgd = optimizers.sgd_experimental.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save("chatbot_model.h5", hist)
print("model created")
