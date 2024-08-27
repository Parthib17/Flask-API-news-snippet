
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the summary function
import nltk
nltk.download('punkt')
def summary(url):

    from newspaper import Article

    # Download the punkt tokenizer


    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
    except Exception as e:
        return f"An error occurred: {e}"

# Load the pickled model
@app.route('/')
def home():
    return "hello world"

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form.get('url')
    result = { 'summary': summary(url)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
