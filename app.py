from flask import Flask, request, redirect

app = Flask(__name__)

# ----- Dados dos projetos inline -----
projects_data = [
    {
        "title": "Chatbot Flask",
        "description": "Um chatbot simples em Flask que recebe perguntas e responde via IA.",
        "link": "https://github.com/richielmartillo/chatbot-flask"
    },
    {
        "title": "Lista de Tarefas",
        "description": "To-do list com interface responsiva e persistência em JSON.",
        "link": "https://github.com/richielmartillo/todo-json"
    },
    {
        "title": "Blog Estático",
        "description": "Blog gerado pelo Python lendo markdown e gerando HTML estático.",
        "link": "https://github.com/richielmartillo/static-blog"
    }
]

# ----- CSS e JS embutidos -----
css = ''' … '''  # use o mesmo bloco de CSS do seu código anterior
js  = ''' … '''  # use o mesmo bloco de JS do seu código anterior

def render_page(title, body, show_success=False):
    flash_html = '<p class="flash">Mensagem enviada com sucesso!</p>' if show_success else ''
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head> … </head>
<body>
  <header> … </header>
  <main class="container">
    {flash_html}
    {body}
  </main>
  <footer> … </footer>
  <script>{js}</script>
</body>
</html>'''

@app.route('/')
def home():
    body = ''' … '''  # idem
    return render_page("Home – Meu Portfólio", body)

@app.route('/projects')
def projects():
    body = '<h2>Meus Projetos</h2><div class="grid">'
    for p in projects_data:
        body += f'''
        <div class="card">
          <h3>{p["title"]}</h3>
          <p>{p["description"]}</p>
          <a href="{p["link"]}" target="_blank">Ver repositório</a>
        </div>'''
    body += '</div>'
    return render_page("Projetos – Meu Portfólio", body)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return redirect('/contact?sent=1')
    show = request.args.get('sent') == '1'
    form = ''' … '''  # idem
    return render_page("Contato – Meu Portfólio", form, show_success=show)

if __name__ == '__main__':
    app.run(debug=True)
