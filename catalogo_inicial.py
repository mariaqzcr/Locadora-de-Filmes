# =============================================================
# catalogo_inicial.py — Filmes pré-cadastrados da Locadora
# Responsabilidade: popular o sistema com um catálogo inicial
# de filmes reais, prontos para uso ao iniciar o programa.
#
# Como usar: importe e chame carregar_catalogo() no main.py
# antes de exibir o menu principal.
#
#   import catalogo_inicial
#   catalogo_inicial.carregar_catalogo()
# =============================================================

import dados


def carregar_catalogo():
    """
    Popula dados.catalogo e dados.fila_reservas com filmes pré-cadastrados.
    Deve ser chamada UMA vez, no início do programa (main.py).
    """

    filmes_iniciais = [

        # ── Ação ────────────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Mad Max: Estrada da Fúria',
            'genero':      'Ação',
            'ano':         2015,
            'status':      dados.STATUS_FILME[0],   # 'Disponível'
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'John Wick',
            'genero':      'Ação',
            'ano':         2014,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Missão Impossível: Acerto de Contas',
            'genero':      'Ação',
            'ano':         2023,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Comédia ─────────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Se Beber, Não Case!',
            'genero':      'Comédia',
            'ano':         2009,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Superbad',
            'genero':      'Comédia',
            'ano':         2007,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'A Grande Aposta',
            'genero':      'Comédia',
            'ano':         2015,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Drama ───────────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'À Espera de um Milagre',
            'genero':      'Drama',
            'ano':         1999,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Clube da Luta',
            'genero':      'Drama',
            'ano':         1999,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Parasita',
            'genero':      'Drama',
            'ano':         2019,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Terror ──────────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Hereditário',
            'genero':      'Terror',
            'ano':         2018,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Corra!',
            'genero':      'Terror',
            'ano':         2017,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'O Iluminado',
            'genero':      'Terror',
            'ano':         1980,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Ficção Científica ────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Interestelar',
            'genero':      'Ficção Científica',
            'ano':         2014,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Matrix',
            'genero':      'Ficção Científica',
            'ano':         1999,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Duna',
            'genero':      'Ficção Científica',
            'ano':         2021,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Animação ─────────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Homem-Aranha no Aranhaverso',
            'genero':      'Animação',
            'ano':         2018,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'A Viagem de Chihiro',
            'genero':      'Animação',
            'ano':         2001,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Up: Altas Aventuras',
            'genero':      'Animação',
            'ano':         2009,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Documentário ─────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Free Solo',
            'genero':      'Documentário',
            'ano':         2018,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'Jiro Dreams of Sushi',
            'genero':      'Documentário',
            'ano':         2011,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },

        # ── Romance ──────────────────────────────────────────────
        {
            'id':          dados.gerar_id(),
            'titulo':      'Antes do Amanhecer',
            'genero':      'Romance',
            'ano':         1995,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
        {
            'id':          dados.gerar_id(),
            'titulo':      'La La Land',
            'genero':      'Romance',
            'ano':         2016,
            'status':      dados.STATUS_FILME[0],
            'alugado_por': None,
        },
    ]

    for filme in filmes_iniciais:
        dados.catalogo.append(filme)
        dados.fila_reservas.append(filme)

    print(f'  ✔  Catálogo carregado com {len(filmes_iniciais)} filmes.\n')
