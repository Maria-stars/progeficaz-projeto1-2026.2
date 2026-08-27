import views
from flask import Flask, render_template_string, request, redirect
import sqlite3


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    note_id = (request.form.get('note_id'))
    delete_note(note_id)
    return index()

if __name__ == '__main__':
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE if not exists note (id INTEGER PRIMARY KEY AUTOINCREMENT, title, content) ")
    app.run(debug=True)