from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Utilizador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.string(100), nullable=False)
    email = db.Column(db.string(200), nullabe=False)
    
    def __repr__(self):
        return f"<Utilizador {self.nome}>"
    
with app.app_context():
    db.create_all()

@app.route('/adicionar/<nome>/<email>')
def adicionar(nome,email):
    novo = Utilizador(nome=nome, email=email)
    db.session.add(novo)
    db.session.commit()
    return f"Utilizador {nome} adicionado."

@app.route('/listar')
def listar():
    utilizadores = Utilizador.query.all()
    return render_template('listar.html' , lista=utilizadores)

if __name__ == "__main__":
    app.run(debug=True)