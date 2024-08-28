# server.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'qlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if not user:
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.route('/get_data', methods=['GET'])
def get_data():
    # Здесь можно реализовать логику получения данных из базы данных
    return jsonify({'data': 'Данные из базы данных'})

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
