import json
import sqlite3
import os

def load_data(banco):
    # conn = sqlite3.connect('banco.db')
    # conn.row_factory = sqlite3.Row
    # cursor = conn.cursor()

    # cursor.execute("""SELECT * from note""")
    
    # rows = cursor.fetchall()
    # conn.close()
    # return rows

    caminho = os.path.join("static", "data", banco)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def load_template(note_html):
    caminho = os.path.join("static", "template", note_html)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

