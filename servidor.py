import views
from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3
from utils import delete_note, update_note, load_template


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

@app.route('/edicao', methods=['POST'])
def edicao():
    id_nota = request.form.get('note_id')
    title_nota = request.form.get('titulo')
    detalhes_nota = request.form.get('detalhes')
    update_note(id_nota, title_nota, detalhes_nota)
    return redirect(url_for('index'))

@app.route('/edicao/<int:nota_id>', methods=['GET'])
def edicao_tela(nota_id):
    conn = sqlite3.connect("banco.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM note WHERE id = ?', (nota_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return redirect(url_for('index'))
    
    note =  {
        'id' : row['id'],
        'titulo' : row['title'],      
        'detalhes' : row['content'],   
        'favorite': row['favorite']
    }

    template = load_template('components/edit.html').format(titulo=note['titulo'], detalhes=note['detalhes'], id=note['id'], favorite=note['favorite'])
    return render_template_string(template)

if __name__ == '__main__':
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE if not exists note (id INTEGER PRIMARY KEY AUTOINCREMENT, title, content) ")
    app.run(debug=True)