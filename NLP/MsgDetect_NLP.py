import re
import nltk

from  nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


#Dataset
messages=[
    "Win Money now!!!",
    "Hello Friend!",
    "Claim your free prize",
    "How are you?????",
    "Free Mobile Offer",
    "Let's meet tommorrow"
]

labels=[
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam"
]

#Lemmatizer Object
lemmatizer = WordNetLemmatizer()

#preprocessing function
def preprocess(text):
    text = text.lower()
    #Remove Symbols
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    #tokenization
    words = word_tokenize(text)

    return " ".join(words)

#apply preprocessing
cleaned_messages = [preprocess(msg) for msg in messages]
# print("Cleaned Messages: ")
# print(cleaned_messages)

#conver tText into Numbers
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(cleaned_messages)

#Create Model
model = MultinomialNB()

#model train
model.fit(x, labels)

#UserInput
user_message = input("Enter Your Message: ")

#process user Input

clean_msg = preprocess(user_message)

#Vectorized user Input

vector_msg = vectorizer.transform([clean_msg])

#prediction
prediction = model.predict(vector_msg)

#Output
print("\n User_Message: ",user_message)
print("Prediction: ",prediction[0])