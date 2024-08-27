from flask import Flask, request, jsonify
import nltk
from newspaper import Article

app = Flask(__name__)

# Download the punkt tokenizer
nltk.download('punkt')

# Define the summary function
def summary(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form.get('url')
    result = {'summary': summary(url)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
