from flask import Flask, render_template, request

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letter')
def show_letter():
    return render_template('letter.html')

if __name__ == '__main__':
    app.run(debug=True)

