# =============================================================
# utils.py — Funções auxiliares do Gerenciador de Locadora
# Responsabilidade: exibição visual, validações de entrada
#                   e helpers reutilizáveis pelos outros módulos.
# =============================================================

from dados import GENEROS


def exibir_titulo(texto):
    """Exibe um cabeçalho destacado para cada seção do menu."""
    print()
    print('=' * 52)
    print(f'  {texto.upper()}')
    print('=' * 52)


def separador():
    """Exibe uma linha divisória simples."""
    print('-' * 52)


def pausar():
    """Pausa a execução e aguarda o usuário pressionar Enter."""
    input('\nPressione Enter para continuar...')


def ler_texto_obrigatorio(mensagem):
    """
    Solicita uma string não vazia ao usuário.
    Repete o pedido enquanto o campo estiver em branco.
    Retorna a string digitada (sem espaços nas bordas).
    """
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print('  ✗ Campo obrigatório. Tente novamente.')


def ler_ano():
    """
    Solicita o ano de lançamento do filme.
    Usa try/except para capturar entradas não numéricas (ex.: letras, símbolos).
    Repete até receber um ano válido entre 1888 e 2100.
    Retorna o ano como inteiro.
    """
    while True:
        try:
            ano = int(input('Ano de lançamento: '))
            if 1888 <= ano <= 2100:
                return ano
            print('  ✗ Ano inválido. Digite um valor entre 1888 e 2100.')
        except ValueError:
            print('  ✗ Entrada inválida. Digite apenas números.')


def escolher_genero():
    """
    Exibe os gêneros disponíveis (da tupla GENEROS) e pede uma escolha.
    Usa try/except para capturar entradas não numéricas.
    Retorna a string do gênero escolhido.
    """
    print('\n  Gêneros disponíveis:')
    for i, genero in enumerate(GENEROS, start=1):
        print(f'    {i}. {genero}')

    while True:
        try:
            opcao = int(input('  Número do gênero: '))
            if 1 <= opcao <= len(GENEROS):
                return GENEROS[opcao - 1]   # acessa a tupla pelo índice
            print(f'  ✗ Escolha entre 1 e {len(GENEROS)}.')
        except ValueError:
            print('  ✗ Digite apenas o número da opção.')


def escolher_filme_por_id(lista):
    """
    Exibe os filmes de uma lista e pede que o usuário informe o ID.
    Usa try/except para capturar entradas inválidas.
    Retorna o dicionário do filme encontrado, ou None se não existir.
    """
    if not lista:
        print('  Nenhum filme disponível para seleção.')
        return None

    for filme in lista:
        print(f'    [ID {filme["id"]}] {filme["titulo"]} ({filme["ano"]}) '
              f'— {filme["genero"]} — {filme["status"]}')

    while True:
        try:
            id_buscado = int(input('  Informe o ID do filme: '))
            for filme in lista:
                if filme['id'] == id_buscado:
                    return filme
            print('  ✗ ID não encontrado. Tente novamente.')
        except ValueError:
            print('  ✗ Digite apenas números.')
