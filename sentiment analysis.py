from flask import Flask, request, render_template

from textblob import TextBlob

import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

 

app = Flask(__name__)

 

@app.route('/')

def my_form():

    return render_template('form.html', title='Sentiment Analysis')

 

@app.route('/', methods=['POST'])

def my_form_post():

    stop_words = set(stopwords.words('english'))

 

    # Convert to lowercase

    text1 = request.form['text1'].lower()

 

    # Remove stopwords

    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])

 

    # Perform sentiment analysis using TextBlob

    blob = TextBlob(processed_doc1)

    polarity = blob.sentiment.polarity

    subjectivity = blob.sentiment.subjectivity

 

    return render_template('form.html', final=polarity, text1=text1, text2=polarity, text3=subjectivity)

 

if __name__ == "__main__":

    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)

