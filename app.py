from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    with open('mesaj.txt', 'r', encoding='utf-8') as file:
        mesaj = file.read()
    return render_template('index.html', mesaj=mesaj)

if __name__ == '__main__':
    app.run(debug=True) 