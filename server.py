from flask import Flask, render_template, session, redirect, request

import random
import datetime



app = Flask(__name__)
app.secret_key = 'denvernuggets'

@app.route('/')
def index():
    if session['gold'] == None and session['goldlog'] == None:
        session['gold'] = 0
        session['goldlog'] = []
    return render_template('index.html', gold = session['gold'], goldlog = session['goldlog'])
    
@app.route('/process_money', methods=['POST', 'GET'])
def processGold():
    pcolor = "gold"
    now = datetime.datetime.now()
    place = request.form.get("building", False)
    if place == "farm":
        goldamount = random.randrange(10, 21)
        session['gold'] += goldamount
        session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
    elif place == "cave":
        goldamount = random.randrange(5, 11)
        session['gold'] += goldamount
        session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
    elif place == "house":
        goldamount = random.randrange(2, 6)
        session['gold'] += goldamount
        session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
    elif place == "casino":
        goldamount = random.randrange(-50, 51)
        session['gold'] += goldamount
        if goldamount > 0:
            session['goldlog'].append(" Earned " + str(goldamount) + " golds from the " + place + "! (" + now.strftime("%Y-%m-%d %H:%M") + ")")
        else: 
            session['goldlog'].append(" Entered a casino and lost " + str(goldamount) + " golds... Ouch...! (" + now.strftime("%Y-%m-%d %H:%M") + ")")

    return redirect('/')

#clears the session and then redirects to the root route
@app.route('/clear', methods=['POST'])
def clear():
    session['gold'] = None
    session['goldlog'] = None
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)