# =============================================================
# filmes.py — Regras de negócio do Gerenciador de Locadora
# Responsabilidade: funções de cadastro, listagem, busca,
#                   aluguel e devolução de filmes.
# =============================================================

import dados
from utils import (exibir_titulo, separador, pausar,
                   escolher_genero, ler_ano,
                   ler_texto_obrigatorio, escolher_filme_por_id)


# ── CADASTRAR FILME ──────────────────────────────────────────

def cadastrar_filme():
    """
    Coleta os dados do novo filme via input, monta um dicionário
    e o registra:
      • no catálogo geral (lista principal)
      • na fila de reservas (FIFO), pois começa como 'Disponível'
    """
    exibir_titulo('Cadastrar Filme')

    titulo = ler_texto_obrigatorio('Título do filme: ')
    genero = escolher_genero()
    ano    = ler_ano()

    # Cada filme é representado por um dicionário com seus atributos
    filme = {
        'id':          dados.gerar_id(),
        'titulo':      titulo,
        'genero':      genero,
        'ano':         ano,
        'status':      dados.STATUS_FILME[0],   # STATUS_FILME[0] = 'Disponível'
        'alugado_por': None,
    }

    # Adiciona à lista geral (mutável)
    dados.catalogo.append(filme)

    # Filmes disponíveis entram no FINAL da fila de reservas — FIFO
    dados.fila_reservas.append(filme)

    print(f'\n  ✔ "{titulo}" cadastrado com sucesso! (ID: {filme["id"]})')
    pausar()


# ── LISTAR CATÁLOGO COMPLETO ─────────────────────────────────

def listar_catalogo():
    """Exibe todos os filmes cadastrados com status de disponibilidade."""
    exibir_titulo('Catálogo Completo')

    if not dados.catalogo:
        print('  Nenhum filme cadastrado ainda.')
        pausar()
        return

    for filme in dados.catalogo:
        _linha_filme(filme)

    print(f'\n  Total no catálogo: {len(dados.catalogo)} filme(s).')
    pausar()


# ── REGISTRAR ALUGUEL ────────────────────────────────────────

def registrar_aluguel():
    """
    Aluga o próximo filme disponível da fila de reservas (FIFO).
    O cliente informa seu nome; o filme do INÍCIO da fila é retirado
    com .pop(0) e marcado como 'Alugado'.

    FIFO em ação: quem entrou primeiro na fila é atendido primeiro.
    """
    exibir_titulo('Registrar Aluguel')

    # Filtra apenas os disponíveis que ainda estão na fila
    disponiveis = [f for f in dados.fila_reservas
                   if f['status'] == dados.STATUS_FILME[0]]

    if not disponiveis:
        print('  Nenhum filme disponível para aluguel no momento.')
        pausar()
        return

    print('\n  Filmes na fila de reservas (ordem de chegada):')
    for pos, f in enumerate(disponiveis, start=1):
        print(f'    {pos}º  [ID {f["id"]}] {f["titulo"]} ({f["ano"]}) — {f["genero"]}')

    cliente = ler_texto_obrigatorio('\n  Nome do cliente: ')

    # Retira o PRIMEIRO da fila — comportamento FIFO
    filme_alugado = dados.fila_reservas.pop(0)

    # Atualiza os atributos do dicionário do filme
    filme_alugado['status']      = dados.STATUS_FILME[1]   # 'Alugado'
    filme_alugado['alugado_por'] = cliente

    print(f'\n  ✔ "{filme_alugado["titulo"]}" alugado para {cliente}!')
    pausar()


# ── REGISTRAR DEVOLUÇÃO ──────────────────────────────────────

def registrar_devolucao():
    """
    Recebe a devolução de um filme atualmente alugado.
    O filme é marcado como 'Disponível', volta para a fila de reservas
    e um registro é empilhado na pilha de devoluções (LIFO).

    LIFO em ação: a devolução mais recente ficará no topo da pilha.
    """
    exibir_titulo('Registrar Devolução')

    alugados = [f for f in dados.catalogo
                if f['status'] == dados.STATUS_FILME[1]]

    if not alugados:
        print('  Nenhum filme alugado no momento.')
        pausar()
        return

    print('\n  Filmes atualmente alugados:')
    filme = escolher_filme_por_id(alugados)
    if not filme:
        pausar()
        return

    cliente_anterior = filme['alugado_por']

    # Atualiza o dicionário do filme
    filme['status']      = dados.STATUS_FILME[0]   # volta a 'Disponível'
    filme['alugado_por'] = None

    # Filme devolvido volta ao FINAL da fila de reservas — FIFO
    dados.fila_reservas.append(filme)

    # Registro de devolução empilhado no TOPO da pilha — LIFO
    registro = {
        'filme':   filme['titulo'],
        'cliente': cliente_anterior,
    }
    dados.pilha_devolucoes.append(registro)   # .append() empilha no topo

    print(f'\n  ✔ "{filme["titulo"]}" devolvido com sucesso!')
    pausar()


# ── HISTÓRICO DE DEVOLUÇÕES ──────────────────────────────────

def ver_historico_devolucoes():
    """
    Exibe o histórico de devoluções do mais recente ao mais antigo.
    Usa reversed() para ler a pilha de baixo para cima (LIFO),
    sem modificar a estrutura original.
    """
    exibir_titulo('Histórico de Devoluções')

    if not dados.pilha_devolucoes:
        print('  Nenhuma devolução registrada ainda.')
        pausar()
        return

    print('  (mais recente → mais antigo)\n')
    for i, registro in enumerate(reversed(dados.pilha_devolucoes), start=1):
        print(f'  {i}. "{registro["filme"]}" — devolvido por {registro["cliente"]}')

    pausar()


# ── BUSCAR POR TÍTULO (bônus) ────────────────────────────────

def buscar_por_titulo():
    """
    Busca filmes cujo título contenha o termo digitado
    (sem distinção entre maiúsculas e minúsculas).
    Funcionalidade bônus.
    """
    exibir_titulo('Buscar por Título')

    termo = ler_texto_obrigatorio('Digite parte do título: ').lower()
    encontrados = [f for f in dados.catalogo if termo in f['titulo'].lower()]

    if not encontrados:
        print('  Nenhum filme encontrado com esse título.')
    else:
        print(f'  {len(encontrados)} resultado(s):\n')
        for f in encontrados:
            _linha_filme(f)

    pausar()


# ── FILMES DISPONÍVEIS POR GÊNERO (bônus) ───────────────────

def listar_disponiveis_por_genero():
    """
    Exibe apenas os filmes com status 'Disponível' dentro do gênero
    escolhido pelo usuário. Funcionalidade bônus.
    """
    exibir_titulo('Disponíveis por Gênero')

    genero = escolher_genero()
    encontrados = [
        f for f in dados.catalogo
        if f['genero'] == genero and f['status'] == dados.STATUS_FILME[0]
    ]

    if not encontrados:
        print(f'\n  Nenhum filme disponível no gênero "{genero}".')
    else:
        print(f'\n  Filmes disponíveis — {genero}:\n')
        for f in encontrados:
            _linha_filme(f)

    pausar()


# ── HELPER INTERNO ───────────────────────────────────────────

def _linha_filme(filme):
    """Exibe uma linha formatada com os dados de um filme."""
    separador()
    alugado_info = f'  → Alugado por: {filme["alugado_por"]}' \
                   if filme['alugado_por'] else ''
    print(f'  [ID {filme["id"]}] {filme["titulo"]} ({filme["ano"]})')
    print(f'  Gênero: {filme["genero"]}  |  Status: {filme["status"]}{alugado_info}')


def separador():
    """Linha divisória entre filmes."""
    print('  ' + '-' * 48)
