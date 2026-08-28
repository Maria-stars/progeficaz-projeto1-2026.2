from utils import load_data, load_template, nova_nota

def index():
    note_template = load_template('components/note.html')
    dados = load_data('banco.db')

    notes_li = []
    for nota in dados:
        notes_li.append(
            note_template.format(
                id=nota['id'],
                title=nota['title'],
                details=nota['content'],
                favorite='★' if nota['favorite'] == 1 else '☆',
                favorite_value=nota['favorite']
            )
        )

    notes = '\n'.join(notes_li)
    html = load_template('index.html').format(notes=notes)
    print(html)
    return load_template('index.html').format(notes=notes)


def submit(titulo, detalhes, favorite):
    nova_nota(titulo, detalhes, favorite)