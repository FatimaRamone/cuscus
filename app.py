from flask import Flask, render_template , request , session

import time
import datetime
import random
import json


app = Flask(__name__)

app.config["SECRET_KEY"] = "-FCKQV8YGQF1xFX6Qf_TVw"

# pipUn viejo dicho ruso lo advirtió: "El futuro es brillante, pero el pasado es impredecible"

words = json.load(open ('words.json'))


@app.route('/')
def lobby():
  return render_template('lobby.html')
@app.route('/index')
def index():
  selected = random.choice(words["words"]) 
  session["english"] = selected["english"]
  session["spanish"] = selected["spanish"]
  
  return render_template ('index.html' , palabra= session["spanish"])

for i in range(10):
    print(i)
time.sleep(1)


@app.route('/index', methods=['POST'])
def respuesta():
  respuesta = request.form['respuesta']

  if respuesta == session["english"]: 
      return render_template('right1.html', palabra= session["spanish"]) 
  else:
      return render_template('wrong1.html', palabra= session["english"])


@app.route('/')
def frontcard():
  session["start"] = time.time()
  selected = random.choice(words["words"]) 
  session["english"] = selected["english"]
  session["spanish"] = selected["spanish"]
  
  return render_template ('frontcard.html' , palabra= session["spanish"])

@app.route('/frontcard')
def frontcard2():
  selected = random.choice(words["words"]) 
  session["english"] = selected["english"]
  session["spanish"] = selected["spanish"]
  
  return render_template ('frontcard.html' , palabra= session["spanish"])




@app.route('/backcard', methods=['POST' ,'GET'])
def backcard():
  return render_template ('backcard.html' , palabraZ= session["english"])

@app.route('/right', methods=['POST' ,'GET'])
def right():
  return render_template ('right.html' )

@app.route('/wrong', methods=['POST' ,'GET'])
def error():
  # guess =  str(frontcard()) ??? guesses taken , number of times the app has run
  

  now = datetime.datetime.now()
  year = '{:02d}'.format(now.year)
  month = '{:02d}'.format(now.month)
  day = '{:02d}'.format(now.day)
  hour = '{:02d}'.format(now.hour)
  minute = '{:02d}'.format(now.minute)
  day_month_year = '{}-{}-{}'.format(year, month, day)

  print('day_month_year: ' + day_month_year)

  # 2019-03-26
  #if session["english"] is None
   # session["english"] = 0

    
  session['error'] = 1
  english= session["english"]
  spanish = session["spanish"] 
  session["english"] = + 1
  error =  session["english"] + 1
  session["end"] = time.time()
  # session["total"] = session["total"] + (session["end"] -session["start"])
  #analytics = session["analytics"]


  #analytics["day_month_year"] = session["end"] -session["start"]

  
  #session["english"] = puntos + 1
  return render_template ('wrong.html' , error = session["english"] , total =  session["end"] - session["start"])  #guess =  str(frontcard()) )




 
   
 # spanish = session['spanish'] 
  #puntos = ;

  #if puntos == null:
  #  puntos = 0

  # english: space
  # spanish: espacio
  # espacio: 0

  #if correct:
   # session[spanish] = puntos + 0
  #else:
   # session[spanish] = puntos + 1


 # if click right 
#   + 0 
 # else:
  #  + 1

     

#if __name__ == '__main__':
    #flask app.run(debug=True)

  


      

#if __name__ == '__main__':
    #flask app.run(debug=True)

  






