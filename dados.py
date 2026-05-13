# =============================================================
# dados.py — Variáveis globais do Gerenciador de Locadora
# Responsabilidade: declarar e centralizar todas as estruturas
#                   de dados usadas pelos demais módulos.
# =============================================================

# ── Tuplas (imutáveis) ───────────────────────────────────────
# Usamos tupla para valores fixos que não devem mudar durante
# a execução. Acessados pelo índice: STATUS_FILME[0] = 'Disponível'
STATUS_FILME = ('Disponível', 'Alugado')
GENEROS      = ('Ação', 'Comédia', 'Drama', 'Terror',
                'Ficção Científica', 'Animação', 'Documentário', 'Romance')

# ── Lista principal ──────────────────────────────────────────
# Armazena TODOS os filmes cadastrados (cada um é um dicionário).
# Mutável: filmes entram com .append() e saem com .remove().
catalogo = []

# ── Fila de reservas — FIFO (First In, First Out) ────────────
# Filmes disponíveis ficam aqui aguardando aluguel.
# Quem entra primeiro sai primeiro.
#   .append(filme)  →  insere no FINAL da fila
#   .pop(0)         →  retira do INÍCIO da fila
fila_reservas = []

# ── Pilha de devoluções — LIFO (Last In, First Out) ──────────
# Registra o histórico de devoluções realizadas.
# A devolução mais recente fica no topo.
#   .append(registro)  →  empilha no TOPO
#   reversed(pilha)    →  lê do TOPO para a base, sem remover
pilha_devolucoes = []

# Contador interno para IDs únicos
_proximo_id = [1]


def gerar_id():
    """Gera e retorna um ID único, incrementando o contador a cada chamada."""
    novo_id = _proximo_id[0]
    _proximo_id[0] += 1
    return novo_id
