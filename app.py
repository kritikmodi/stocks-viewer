from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    text = request.form['text']
    return render_template('results.html', text=text)

if __name__ == '__main__':
    app.run()
