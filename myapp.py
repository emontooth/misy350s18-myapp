from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    #return "hello Eddie Montooth"

import random


@app.route('/form')
def form():
    return render_template('form.html')




@app.route('/hello')
def hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)

@app.route('/user/<string:name>/')
def get_user_name(name):
    # return "hello " + name
    # return "Hello %s, this is %s" % (name, 'administrator')
    return render_template('user.html', name=name)


if __name__ == '__main__':
        app.run()

        app.run(debug=True)

        app.run(host='0.0.0.0', port=4500)
