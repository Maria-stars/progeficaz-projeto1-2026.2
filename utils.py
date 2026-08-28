import json
import sqlite3
import os

def load_data(banco):
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""SELECT id, title, content, COALESCE(favorite, 0) AS favorite
                      FROM note ORDER BY favorite DESC""")
    
    rows = cursor.fetchall()
    conn.close()
    return rows

def load_template(note_html):
    caminho = os.path.join("static", "template", note_html)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def nova_nota(titulo, detalhes, favorite):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO note (title, content, favorite) VALUES (:titulo, :detalhes, :favorite)",
    {'titulo': titulo, 'detalhes': detalhes, 'favorite':favorite})
    conn.commit()
    cursor.close()
    conn.close()

def delete_note(note_id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM note WHERE id = ?',
        (note_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_note(note_id, nota_titulo, nota_detalhes):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute( 'UPDATE note SET title = ?, content = ? WHERE id = ?', (nota_titulo, nota_detalhes, note_id))
    conn.commit()
    conn.close()


def update_favorite(note_id, favorite):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE note SET favorite = ? WHERE id = ?',
        (favorite, note_id)
    )
    conn.commit()
    conn.close()

