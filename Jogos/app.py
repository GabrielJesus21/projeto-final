from flask import Flask, request, jsonify, session, render_template
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Dados em memória
users = {
    "admin": "1234",
    "user": "senha"
}
game_lists = {username: [] for username in users}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Nome de usuário e senha são obrigatórios'})
    if username in users:
        return jsonify({'success': False, 'message': 'Nome de usuário já existe'})
    users[username] = password
    game_lists[username] = []
    return jsonify({'success': True, 'message': 'Conta criada com sucesso'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        session['username'] = username
        return jsonify({'success': True, 'username': username})
    return jsonify({'success': False, 'message': 'Nome de usuário ou senha incorretos'})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({'success': True})

@app.route('/api/games', methods=['GET'])
def get_games():
    username = session.get('username')
    if not username:
        return jsonify({'success': False, 'message': 'Você precisa estar logado'}), 401
    return jsonify({'success': True, 'games': game_lists[username]})

@app.route('/api/games', methods=['POST'])
def add_game():
    username = session.get('username')
    if not username:
        return jsonify({'success': False, 'message': 'Você precisa estar logado'}), 401
    data = request.json
    game = data.get('game')
    if game:
        game_lists[username].append(game)
        return jsonify({'success': True, 'message': f"Jogo '{game}' adicionado"})
    return jsonify({'success': False, 'message': 'Nome do jogo não pode ser vazio'})

@app.route('/api/games', methods=['DELETE'])
def remove_game():
    username = session.get('username')
    if not username:
        return jsonify({'success': False, 'message': 'Você precisa estar logado'}), 401
    data = request.json
    game = data.get('game')
    if game in game_lists[username]:
        game_lists[username].remove(game)
        return jsonify({'success': True, 'message': f"Jogo '{game}' removido"})
    return jsonify({'success': False, 'message': 'Jogo não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)