from flask import Flask, render_template, url_for, request, redirect
from flask import flash
from forms import Contato
from flask_mail import Message, Mail

app = Flask(__name__)
mail = Mail()

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'spawnbenzi@gmail.com'
app.config["MAIL_PASSWORD"] = '0ok9ij8uh'

mail.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')
@app.route('/institucional')
def inst():
    return render_template('institucional.html')
@app.route('/contato', methods=['POST','GET'])
def contato():
    form = Contato()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contato.html', form=form)
        else:
            msg = Message(form.assunto.data, sender='spawnbenzi@gmail.com', recipients=['contato@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.mensagem.data)
            mail.send(msg)
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contato.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port = 8000)
