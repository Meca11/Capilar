from flask import Flask, render_template, request

app = Flask(__name__)


# ==================================================
# DEFINIÇÕES DOS TIPOS DE CABELO
# ==================================================

tipos_cabelo = {

    "liso": {
        "nome": "Cabelo Liso",

        "descricao":
            "Cabelo liso é caracterizado por fios retos, "
            "sem formação de ondas ou cachos.",

        "caracteristicas": [
            "Fios predominantemente retos.",
            "Pode apresentar maior distribuição da oleosidade "
            "ao longo do comprimento."
        ],

        "fontes": [
            "Fonte científica será adicionada aqui"
        ]
    },


    "ondulado": {
        "nome": "Cabelo Ondulado",

        "descricao":
            "Cabelo ondulado apresenta curvaturas suaves "
            "ao longo dos fios.",

        "caracteristicas": [
            "Apresenta ondas ao longo do comprimento.",
            "A intensidade das ondulações pode variar."
        ],

        "fontes": [
            "Fonte científica será adicionada aqui"
        ]
    },


    "cacheado": {
        "nome": "Cabelo Cacheado",

        "descricao":
            "Cabelo cacheado apresenta curvaturas mais definidas "
            "ao longo dos fios.",

        "caracteristicas": [
            "Apresenta cachos ou espirais.",
            "O formato e o diâmetro dos cachos podem variar."
        ],

        "fontes": [
            "Fonte científica será adicionada aqui"
        ]
    },


    "crespo": {
        "nome": "Cabelo Crespo",

        "descricao":
            "Cabelo crespo apresenta curvaturas bastante "
            "acentuadas ao longo da fibra.",

        "caracteristicas": [
            "Apresenta curvaturas pequenas e acentuadas.",
            "Pode apresentar diferentes padrões de curvatura."
        ],

        "fontes": [
            "Fonte científica será adicionada aqui"
        ]
    }

}


# ==================================================
# FUNÇÃO 1 - CALCULAR PONTUAÇÕES
# ==================================================

def calcular_pontuacoes(
    ressecamento,
    oleosidade,
    quebra,
    procedimento_quimico,
    quimicas
):

    hidratacao = 0
    nutricao = 0
    reconstrucao = 0


    # REGRAS PROVISÓRIAS
    # Os pesos serão definidos posteriormente
    # com base na pesquisa científica.


    if ressecamento == "alto":
        hidratacao += 3

    elif ressecamento == "medio":
        hidratacao += 2


    if oleosidade == "baixo":
        nutricao += 2


    if quebra == "alto":
        reconstrucao += 2

    elif quebra == "medio":
        reconstrucao += 1


    if procedimento_quimico == "sim":
        reconstrucao += 1


    if "descoloracao" in quimicas:
        reconstrucao += 1


    return {
        "Hidratação": hidratacao,
        "Nutrição": nutricao,
        "Reconstrução": reconstrucao
    }


# ==================================================
# FUNÇÃO 2 - DEFINIR PRIORIDADES
# ==================================================

def definir_prioridades(pontuacoes):

    prioridades = sorted(
        pontuacoes,
        key=pontuacoes.get,
        reverse=True
    )

    return prioridades


# ==================================================
# FUNÇÃO 3 - GERAR CRONOGRAMA
# ==================================================

def gerar_cronograma(prioridades):

    principal = prioridades[0]
    secundario = prioridades[1]
    terceiro = prioridades[2]


    cronograma_gerado = [

        {
            "semana": 1,
            "tratamentos": [
                principal,
                secundario,
                principal
            ]
        },

        {
            "semana": 2,
            "tratamentos": [
                secundario,
                principal,
                terceiro
            ]
        },

        {
            "semana": 3,
            "tratamentos": [
                principal,
                secundario,
                principal
            ]
        },

        {
            "semana": 4,
            "tratamentos": [
                secundario,
                principal,
                terceiro
            ]
        }

    ]

    return cronograma_gerado


# ==================================================
# ROTAS DAS PÁGINAS
# ==================================================

@app.route("/")
def inicio():
    return render_template("lista.html")


@app.route("/cronograma")
def cronograma():
    return render_template("cronograma.html")


@app.route("/entenda")
def entenda():
    return render_template("entenda.html")


@app.route("/emocional")
def emocional():
    return render_template("emocional.html")


# ==================================================
# PÁGINA DINÂMICA DE TIPO DE CABELO
# ==================================================

@app.route("/entenda/<tipo>")
def pagina_tipo_cabelo(tipo):

    dados = tipos_cabelo.get(tipo)

    if dados is None:
        return "Tipo de cabelo não encontrado", 404

    return render_template(
        "tipo_cabelo.html",
        cabelo=dados
    )


# ==================================================
# ANALISAR QUESTIONÁRIO
# ==================================================

@app.route("/analisar", methods=["POST"])
def analisar():

    tipo_cabelo_usuario = request.form.get("tipo_cabelo")
    ressecamento = request.form.get("ressecamento")
    quebra = request.form.get("quebradeza")
    oleosidade = request.form.get("oleosidade")
    espessura = request.form.get("espessura")

    procedimento_quimico = request.form.get(
        "procedimento_quimico"
    )

    quimicas = request.form.getlist("quimicas")


    pontuacoes = calcular_pontuacoes(
        ressecamento,
        oleosidade,
        quebra,
        procedimento_quimico,
        quimicas
    )


    prioridades = definir_prioridades(
        pontuacoes
    )


    cronograma_gerado = gerar_cronograma(
        prioridades
    )


    print("Tipo de cabelo:", tipo_cabelo_usuario)
    print("Espessura:", espessura)
    print("Pontuações:", pontuacoes)
    print("Prioridades:", prioridades)
    print("Cronograma:", cronograma_gerado)


    return render_template(
        "cronograma.html",

        resultado=True,

        pontuacoes=pontuacoes,

        prioridades=prioridades,

        cronograma=cronograma_gerado,

        tipo_cabelo=tipo_cabelo_usuario,

        espessura=espessura
    )


# ==================================================
# INICIAR FLASK
# ==================================================

if __name__ == "__main__":
    app.run(debug=True)