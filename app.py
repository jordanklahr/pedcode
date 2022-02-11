from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    numb = random.randrange(1,20)
    dictionary = {0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three' }
    if numb = 20:
        response = str(random.randrange(0,300) - 100) + '%'
        return response
    else
        return str(random.randrange(0,100)) + '%'

if __name__ == '__main__':
    app.run()
