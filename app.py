from flask import Flask, request, redirect

app = Flask(__name__)

css = '''
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:Arial,sans-serif; color:#333; line-height:1.6; }
.container{ max-width:800px; margin:auto; padding:1rem; }
header{ background:#222; color:#fff; }
header .container{ display:flex; justify-content:space-between; align-items:center; }
.menu a{ color:#fff; margin-right:1rem; text-decoration:none; }
.menu-btn{ display:none; background:none; border:none; color:#fff; font-size:1.5rem; }
.grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:1rem; margin:1rem 0;}
.card{ border:1px solid #ccc; padding:1rem; border-radius:.5rem;}
footer{ background:#f4f4f4;text-align:center;padding:1rem 0;}
@media(max-width:600px){
  .menu-btn{ display:block; }
  .menu a{ display:none; }
  .menu.open a{ display:block; }
  .grid{ grid-template-columns:1fr; }
}
'''

js = '''
document.querySelector('.menu-btn').addEventListener('click', function(){
  document.querySelector('.menu').classList.toggle('open');
});
'''

def render_page(title, body, show_success=False):
    flash_html = (
        '<p style="background:#e0ffe0;padding:1rem;border-radius:.5rem;">'
        'Mensagem enviada com sucesso!</p>'
    ) if show_success else ''
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title}</title>
  <style>{css}</style>
</head>
<body>
  <header>
    <div class="container">
      <h1>Richard</h1>
      <nav class="menu">
        <a href="/">Home</a>
        <a href="/projects">Projetos</a>
        <a href="/contact">Contato</a>
        <button class="menu-btn">☰</button>
      </nav>
    </div>
  </header>
  <main class="container">
    {flash_html}
    {body}
  </main>
  <footer>
    <div class="container">
      © 2025 • Feito por Seu Nome
    </div>
  </footer>
  <script>{js}</script>
</body>
</html>'''

@app.route('/')
def home():
    body = '''
    <section class="intro">
      <h2>Sobre Mim</h2>
      <p>Desenvolvedor web full-stack, apaixonado por interfaces clean e funcionais.</p>
    </section>'''
    return render_page("Home – Meu Portfólio", body)

@app.route('/projects')
def projects():
    body = '''
    <h2>Meus Projetos</h2>
    <div class="grid">
      <div class="card">
        <h3>Projeto 1</h3>
        <p>Descrição breve.</p>
        <a href="#">Ver repositório</a>
      </div>
    </div>'''
    return render_page("Projetos – Meu Portfólio", body)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return redirect('/contact?sent=1')
    show = request.args.get('sent') == '1'
    form = '''
    <h2>Contato</h2>
    <form method="post">
      <label>Nome:</label><br><input type="text" name="name" required><br><br>
      <label>E-mail:</label><br><input type="email" name="email" required><br><br>
      <label>Mensagem:</label><br><textarea name="message" required></textarea><br><br>
      <button type="submit">Enviar</button>
    </form>'''
    return render_page("Contato – Meu Portfólio", form, show_success=show)

if __name__ == '__main__':
    app.run(debug=True)
