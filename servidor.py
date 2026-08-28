import views
from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3
from utils import delete_note, update_note, load_template, update_favorite


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
    favorite = request.form.get('favorite', 0)  
    if not favorite:
        favorite = 0
    else:
        favorite = int(favorite)
    views.submit(titulo, detalhes, favorite)
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

@app.route('/favorite/<int:nota_id>', methods=['POST'])
def favorito(nota_id):
    current_favorite = int(request.form.get('current_favorite') or 0)

    new_favorite = 0 if current_favorite == 1 else 1

    update_favorite(nota_id, new_favorite)
    return redirect(url_for('index'))

if __name__ == '__main__':
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS note (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title,
        content,
        favorite INTEGER NOT NULL DEFAULT 0
    )""")
    app.run(debug=True)