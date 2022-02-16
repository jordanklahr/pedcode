from flask import Flask
from flask import request
import random

app = Flask(__name__)


@app.route('/love')
def hello_world():
    numb = random.randint(1,20)
    #dictionary = {0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three' }
    if numb == 20:
        #response = str(random.randrange(0,300) - 100) + '%'
        value = random.randrange(0,300) - 100
        if value > 0 and value <= 100:
            if value < 50:
                return "∞%"
            else:
                return "-∞%"
        else:
            response = str(value) + '%'
            return response
    else:
        response = str(random.randrange(0,100)) + '%'
        return response

    
@app.route('/wakemeupinside')
def jello():
    return " "
    
    
@app.route('/chartest')
def chartest():
    return "This is a test string for the character: ∞"


@app.route('/redoxisstupid')
#this is the redox fucks around with things because they dont understand it section, move along now traveller nothing to see here
def bingus():
    numb = random.randint(1,20)
    login = request.headers['x-fossabot-message-userlogin']
    mods = ['pimpega', 'redoxxed', 'elskeling', 'sycon1', 'overlite', 'boba', 'roseduelistarxsia', 'kirbelle', 'rechampj']
    if(login in mods):
        if numb == 20:
            return "∞%"
        else:
            value = random.randrange(50,300)
            return value + '%'
    else:
        if numb == 20:
            #response = str(random.randrange(0,300) - 100) + '%'
            value = random.randrange(0,300) - 100
            if value > 0 and value <= 100:
                if value < 50:
                    return "∞% bing"
                else:
                    return "-∞% bing"
            else:
                response = str(value) + '% bing'
                return response
        else:
            response = str(random.randrange(0,100)) + '% bing'
            return response

if __name__ == '__main__':
    app.run()
