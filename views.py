from utils import load_data, load_template, nova_nota

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            id=dados['id'],
            title=dados['title'],
            details=dados['content'],
            favorite_value=dados['favorite'],
            favorite='Desfavoritar' if dados['favorite'] else 'Favoritar'
        )
        for dados in load_data('notes.js')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    nova_nota(titulo, detalhes)