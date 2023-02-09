from flask import Flask,request, render_template,session

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

    app.run()
