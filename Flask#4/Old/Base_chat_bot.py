import razdel
import random
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')


article_sentences = [_.text for _ in
                     razdel.sentenize(open(r'C:\Users\Алексей\Downloads\390611_litres.txt', encoding='utf-8').read())]

greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]


def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)


def generate_response(user_input):
    tennisrobo_response = ''
    article_sentences.append(user_input)
    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text)
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]
    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]
    if vector_matched == 0:
        tennisrobo_response = tennisrobo_response + "I am sorry, I could not understand you"
        return tennisrobo_response
    else:
        tennisrobo_response = tennisrobo_response + article_sentences[similar_sentence_number]
        return tennisrobo_response


def perform_lemmatization(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]


punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)


def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(punctuation_removal)))


if __name__ == '__main__':
    continue_dialogue = True
print("Hello, I am your friend TennisRobo. You can ask me any question regarding tennis:")
while (True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
            continue_dialogue = False
            print("TennisRobo: Most welcome")
        else:
            if generate_greeting_response(human_text) != None:
                print("TennisRobo: " + generate_greeting_response(human_text))
            else:
                print("TennisRobo: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("TennisRobo: Good bye and take care of yourself...")
