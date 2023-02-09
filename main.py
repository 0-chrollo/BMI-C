<<<<<<< HEAD
from flask import Flask,request, render_template,session
import os

port=int(os.environ.get('PORT', 500))


template_file = 'templates/index.html'
with open(template_file, "w") as f:
    f.write("""<!doctype html>
<html>

<head>

<title>Lucas BMI</title>

<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
     <link rel="stylesheet"  href="{{ url_for('static', filename= 'style.css')}}">
</head>



<body>
<div id="background-image">
    <div class="content" style="background-color: rgb(245,245,245,0.4); height: 100%;">

<h1 align="center"><u>BMI Calculator</u></h1>


<div align="center" >
    <form class="pure-form" method="POST" action="/luca">
        <br>
        <label for="weight">Enter Weight in (Kg)</label><br>
        <input type="text" id='weight' name="weight" value="{{ weight}}"placeholder="eg:56"><br>
        <br>
        <label for="height">Enter Height in (cm)</label><br>
        <input type="text" id='height' name="height" value="{{ height }}" placeholder="eg:126" ><br>

        <br><button type="submit" class="pure-button pure-button-primary" value="Submit">Submit</button><br>


         <br><button type="submit" name="reset" value="Reset" class="pure-button pure-button-primary" >Reset</button><br>

</form>




</div>
<div border="auto"><br>
  <div class="answer-box">
    {% if bmi %}
      <p align="center">Your BMI is <b> {{ bmi }}</b></p><br>
      {% if bmi > 40:  %}
        <p align="center"><u>you are morbidly obese, consider losing weight</u></p><br>
      {% endif %}
    {% endif %}
  </div>
</div>
<footer class="footer">
    <p align="center">Copyright &copy; 2023 Lucas BMI</p>
</footer>
</div>

</div>


</body>

</html>
""")

style_file="static/style.css"
with open(style_file,"w") as f:
    f.write("""
    
    
    
    #background-image {
  background-image: url('bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  filter: brightness(40%);
  height: 100vh;
  width: 100%;
  position: absolute;
}

body {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.answer-box {
  background-color: lightgray;
  border: 1px solid gray;
  border-radius: 10px;
  padding: 20px;
  width: 50%;
  margin: 20px auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  text-align: center;
  padding: 10px;
}
    
""")

app = Flask(__name__)
app.secret_key = 'secret_key'



@app.route('/luca', methods=["GET", "POST"])

def bmi():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:

        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc(weight, height)
        session['weight']= weight
        session['height']= height
    else:
        weight = session.get('weight', '')
        height = session.get('height', '')
        bmi = session.get('bmi','')
    if request.form.get('reset'):
        session.pop('weight', None)
        session.pop('height',None)
        weight = ''
        height=''
        bmi = ''

    session['bmi'] = bmi
    return render_template("index.html",
                           weight=weight,
                           height=height,
                           bmi=bmi)

def calc(weight,height):
    return round(( weight / ((height/100) ** 2)), 2)

if __name__== "__main__":

    app.run(host='0.0.0.0',port=port)

=======
from flask import Flask,request, render_template,session
import os

port=int(os.environ.get('PORT', 500))


template_file = 'templates/index.html'
with open(template_file, "w") as f:
    f.write("""<!doctype html>
<html>

<head>

<title>Lucas BMI</title>

<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
     <link rel="stylesheet"  href="{{ url_for('static', filename= 'style.css')}}">
</head>



<body>
<div id="background-image">
    <div class="content" style="background-color: rgb(245,245,245,0.4); height: 100%;">

<h1 align="center"><u>BMI Calculator</u></h1>


<div align="center" >
    <form class="pure-form" method="POST" action="/luca">
        <br>
        <label for="weight">Enter Weight in (Kg)</label><br>
        <input type="text" id='weight' name="weight" value="{{ weight}}"placeholder="eg:56"><br>
        <br>
        <label for="height">Enter Height in (cm)</label><br>
        <input type="text" id='height' name="height" value="{{ height }}" placeholder="eg:126" ><br>

        <br><button type="submit" class="pure-button pure-button-primary" value="Submit">Submit</button><br>


         <br><button type="submit" name="reset" value="Reset" class="pure-button pure-button-primary" >Reset</button><br>

</form>




</div>
<div border="auto"><br>
  <div class="answer-box">
    {% if bmi %}
      <p align="center">Your BMI is <b> {{ bmi }}</b></p><br>
      {% if bmi > 40:  %}
        <p align="center"><u>you are morbidly obese, consider losing weight</u></p><br>
      {% endif %}
    {% endif %}
  </div>
</div>
<footer class="footer">
    <p align="center">Copyright &copy; 2023 Lucas BMI</p>
</footer>
</div>

</div>


</body>

</html>
""")

style_file="static/style.css"
with open(style_file,"w") as f:
    f.write("""
    
    
    
    #background-image {
  background-image: url('bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  filter: brightness(40%);
  height: 100vh;
  width: 100%;
  position: absolute;
}

body {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.answer-box {
  background-color: lightgray;
  border: 1px solid gray;
  border-radius: 10px;
  padding: 20px;
  width: 50%;
  margin: 20px auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  text-align: center;
  padding: 10px;
}
    
""")

app = Flask(__name__)
app.secret_key = 'secret_key'



@app.route('/luca', methods=["GET", "POST"])

def bmi():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:

        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc(weight, height)
        session['weight']= weight
        session['height']= height
    else:
        weight = session.get('weight', '')
        height = session.get('height', '')
        bmi = session.get('bmi','')
    if request.form.get('reset'):
        session.pop('weight', None)
        session.pop('height',None)
        weight = ''
        height=''
        bmi = ''

    session['bmi'] = bmi
    return render_template("index.html",
                           weight=weight,
                           height=height,
                           bmi=bmi)

def calc(weight,height):
    return round(( weight / ((height/100) ** 2)), 2)

if __name__== "__main__":

    app.run(host='0.0.0.0',port=port)

>>>>>>> 9940113cba47d7135d19faf0f62ecd4fc9c3e294
