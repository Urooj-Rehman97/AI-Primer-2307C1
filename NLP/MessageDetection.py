from sklearn.feature_extraction.text import CountVectorizer #Convert text into count
from sklearn.naive_bayes import MultinomialNB #Algorithm for spam detection

#Dataset
messages=[
    "Win Money now",
    "Hello Friend",
    "Claim your free prize",
    "How are you",
    "Free Mobile Offer",
    "Lets meet tommorrow"
]

labels=[
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam"
]

#Vectorization
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(messages)

#Create Model
model = MultinomialNB()

model.fit(x,labels)

#userInput
# user_input = ["Win Free iPhone"]
# user_input = ["Congratulation! You won iPhone"]
user_input = ["Hello! How are You???"]

user_msg = vectorizer.transform(user_input)
prediction = model.predict(user_msg)
#OutPut
print("Message: ", user_input[0])
print("Prediction: ", prediction[0])

