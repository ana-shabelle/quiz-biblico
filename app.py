from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Lista de perguntas difíceis (com 'versiculo' adicionado para cada uma)
perguntas = [
    {
        'pergunta': 'Quantos capítulos tem o livro de Isaías?',
        'opcoes': ['66', '72', '40', '50'],
        'resposta': '66',
        'versiculo': 'Isaías 1:1; 66:24'
    },
    {
        'pergunta': 'Qual profeta teve uma visão de ossos secos que reviveram?',
        'opcoes': ['Jeremias', 'Ezequiel', 'Isaías', 'Daniel'],
        'resposta': 'Ezequiel',
        'versiculo': 'Ezequiel 37'
    },
    {
        'pergunta': 'Qual era o nome do servo que Paulo encontrou em Filipos e que depois se tornou pastor?',
        'opcoes': ['Timóteo', 'Tito', 'Onésimo', 'Filemom'],
        'resposta': 'Timóteo',
        'versiculo': 'Atos 16:1-3'
    },
    {
        'pergunta': 'Quantas vezes aparece o nome “Jerusalém” na Bíblia (aproximadamente)?',
        'opcoes': ['250', '500', '800', '1000'],
        'resposta': '800',
        'versiculo': 'Aproximadamente 800 vezes em toda a Bíblia'
    },
    {
        'pergunta': 'Quem escreveu o Salmo 90?',
        'opcoes': ['Davi', 'Salomão', 'Moisés', 'Asafe'],
        'resposta': 'Moisés',
        'versiculo': 'Salmos 90:1'
    },
    {
        'pergunta': 'O que significa “Ebenezer”?',
        'opcoes': ['O Senhor proverá', 'Deus conosco', 'Paz de Deus', 'Até aqui nos ajudou o Senhor'],
        'resposta': 'Até aqui nos ajudou o Senhor',
        'versiculo': '1 Samuel 7:12'
    },
    {
        'pergunta': 'Qual era o nome da esposa de Oséias?',
        'opcoes': ['Noemi', 'Gômer', 'Débora', 'Rute'],
        'resposta': 'Gômer',
        'versiculo': 'Oséias 1:3'
    },
    {
        'pergunta': 'Quem foi o profeta que fez um machado flutuar na água?',
        'opcoes': ['Elias', 'Eliseu', 'Isaías', 'Jeremias'],
        'resposta': 'Eliseu',
        'versiculo': '2 Reis 6:1-7'
    },
    {
        'pergunta': 'Quantos capítulos têm o livro de Salmos?',
        'opcoes': ['100', '119', '150', '200'],
        'resposta': '150',
        'versiculo': 'Livro de Salmos'
    },
    {
        'pergunta': 'Qual foi o nome do sacerdote que criou um ídolo para Mica?',
        'opcoes': ['Abiatar', 'Jônatas', 'Nadabe', 'Fineias'],
        'resposta': 'Jônatas',
        'versiculo': 'Juízes 18:30'
    },
    {
        'pergunta': 'Qual o único livro da Bíblia que não menciona o nome de Deus?',
        'opcoes': ['Ester', 'Cantares de Salomão', 'Eclesiastes', 'Filemom'],
        'resposta': 'Ester',
        'versiculo': 'Livro de Ester'
    },
    {
        'pergunta': 'Qual rei ficou leproso por querer queimar incenso no templo, algo que era função dos sacerdotes?',
        'opcoes': ['Ezequias', 'Saul', 'Uzias', 'Roboão'],
        'resposta': 'Uzias',
        'versiculo': '2 Crônicas 26:16-21'
    }
]

# Página inicial
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Página para mostrar botão iniciar após preencher dados
@app.route('/quiz', methods=['POST'])
def quiz():
    nome = request.form['nome']
    email = request.form['email']
    idade = request.form['idade']
    return render_template('quiz.html', nome=nome, email=email, idade=idade, perguntas=perguntas)

# Mostra novamente o quiz (caso queira reiniciar diretamente)
@app.route('/quiz/iniciar', methods=['POST'])
def iniciar_quiz():
    nome = request.form['nome']
    return render_template('quiz.html', nome=nome, perguntas=perguntas)

# Finaliza o quiz e mostra o resultado
@app.route('/quiz/finalizar', methods=['POST'])
def finalizar_quiz():
    respostas_usuario = request.form
    nome = respostas_usuario.get('nome', 'Usuário')
    score = 0
    respostas = []

    for i, pergunta in enumerate(perguntas, start=1):
        resposta_certa = pergunta['resposta']
        resposta_usuario = respostas_usuario.get(f'pergunta_{i}')
        
        if resposta_usuario == resposta_certa:
            score += 1
            resposta_status = 'Correta'
        else:
            resposta_status = 'Errada'
        
        respostas.append({
            'pergunta': pergunta['pergunta'],
            'resposta_usuario': resposta_usuario,
            'resposta_certa': resposta_certa,
            'status': resposta_status,
            'versiculo': pergunta['versiculo']
        })

    total = len(perguntas)
    percentual = round((score / total) * 100)

    versiculos = [
        "“Sede fortes e corajosos, não temais.” — Deuteronômio 31:6"
    ]
    versiculo = random.choice(versiculos)

    return render_template(
        'resultado.html',
        nome=nome,
        score=score,
        total=total,
        percentual=percentual,
        respostas=respostas,
        versiculo=versiculo
    )

if __name__ == '__main__':
    app.run(debug=True)




