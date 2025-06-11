from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///notes.db')
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify([{'id': note.id, 'content': note.content} for note in Note.query.all()])

@app.route('/api/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note = Note(content=data['content'])
    db.session.add(note)
    db.session.commit()
    return jsonify({'id': note.id, 'content': note.content}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
