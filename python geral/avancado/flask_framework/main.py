from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html') # pra poder ver o template a ele precisa estar exatamente na pasta templates
    if request.method == 'POST':
        text = request.form.get('textbox')
        return render_template('index.html', output=float(text), user_text = text)


if __name__ == '__main__':
    app.run()