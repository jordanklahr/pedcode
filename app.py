from flask import Flask
import random

app = Flask(__name__)


@app.route('/love')
def hello_world():
    numb = random.randint(1,20)
    #dictionary = {0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three' }
    if numb == 20:
        response = str(random.randrange(0,300) - 100) + '%'
        return response
    else:
        response = str(random.randrange(0,100)) + '%'
        return response

if __name__ == '__main__':
    app.run()
