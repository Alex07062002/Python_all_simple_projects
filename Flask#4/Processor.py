import sqlite3
import os
import razdel
import random
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')


class Processor:

    def find_answer(self, question):
        self.question = question
        connection = sqlite3.connect('QA.db')
        cur = connection.cursor()
        result = []
        for row in cur.execute("select answer from QuestionAnswer where question = :question",
                               {"question": self.question}):
            result.append(row[0])
        connection.close()
        if len(result) != 0:
            return random.choice(result)
        else:
            self.article_sentences.append(self.question)
            word_vectorizer = TfidfVectorizer(tokenizer=self.get_processed_text)
            all_word_vectors = word_vectorizer.fit_transform(self.article_sentences)
            similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
            similar_sentence_number = similar_vector_values.argsort()[0][-2]
            matched_vector = similar_vector_values.flatten()
            matched_vector.sort()
            vector_matched = matched_vector[-2]
            if vector_matched == 0:
                return None
            else:
                chatbot_response = self.article_sentences[similar_sentence_number]
            return chatbot_response

    def add_user_answer(self, answer):
        con = sqlite3.connect('QA.db')
        cur = con.cursor()
        cur.execute("select * from QuestionAnswer")
        results = cur.fetchall()
        count = len(results)+1
        cur.execute("insert into QuestionAnswer values (" + str(count) + ",'" + str(self.question) + "', '" + answer + "')")
        con.commit()
        con.close()

    def __init__(self):
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.question = None
        self.article_sentences = [_.text for _ in
                                  razdel.sentenize(open(r'Data_base\390611_litres.txt', encoding='utf-8').read())]
        con = sqlite3.connect('QA.db')
        cur = con.cursor()
        cur.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='QuestionAnswer'")
        if cur.fetchone()[0] == 0:
            cur.execute("create table IF NOT EXISTS QuestionAnswer (id int, question text, answer text)")
            count = 0
            for filename in os.listdir(r"Data_base"):
                if filename.endswith(".bin"):
                    with open(r'Data_base' + '\\' + filename, 'r', encoding='utf-8-sig') as file_parser:
                        for line in file_parser.readlines():
                            if not line:
                                break
                            else:
                                a = line.split('\\')
                                count += 1
                                cur.execute(
                                    "insert into QuestionAnswer values (" + str(count) + ",'" + a[0] + "', '" + a[
                                        1] + "')")
                                con.commit()
        con.close()

    def perform_lemmatization(self, tokens):
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)

    def get_processed_text(self, document):
        return self.perform_lemmatization(
            nltk.word_tokenize(document.lower().translate(self.punctuation_removal)))


