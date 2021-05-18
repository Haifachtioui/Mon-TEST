from flask import Flask , render_template, request
from forms import SignUpForm

app = Flask(__name__)

app.config ['SECRET_KEY'] = 'HEYPHA'
#retenir le resultat dans la page user.html dans un tableau 
@app.route('/signup', methods = ['GET' , 'POST'])
def signup(): 
    form = SignUpForm()
    if form.is_submitted():
        result= request.form
        return render_template ('user.html' , result=result )
    return render_template ('signup.html' , form=form )

#retenir le nom de l'utilisateur et le rédiriger vers la page index.html pour faire le calcul + message bienvenue
@app.route("/index",methods=['POST'])
def index():
    result= request.form
    n=result['nom']
    p=result['prénom']
    return render_template('index.html',nom=n, prénom=p)


if  __name__ =="__main__":
    app.run()