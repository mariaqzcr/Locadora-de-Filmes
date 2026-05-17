<div align="center">

# 🎬 Gerenciador de Locadora de Filmes

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=flat-square)
![Disciplina](https://img.shields.io/badge/Disciplina-Programação%20de%20Computadores-c8372d?style=flat-square)

**Sistema de gerenciamento de locadora desenvolvido em Python com estruturas de dados e modularização**

</div>

---

## 📋 Informações do Projeto

| Campo | Detalhe |
|---|---|
| **Tema** | Locadora de Filmes (Básico) |
| **Disciplina** | Programação de Computadores |
| **Professora** | Profa. Dra. Andrea Ono Sakai |
| **Integrantes** | Felipe Pereira Roberto · Maria Eduarda Queiroz Correa · Omar Alejandro de Jesus Bravo Hernandez |
| **Período/Turma** | Diurno |
| **Ano** | 2026 |

---

## 1. Descrição do Projeto

Sistema de gerenciamento de uma locadora de filmes desenvolvido em Python, dividido em múltiplos arquivos. O sistema permite cadastrar filmes, registrar aluguéis e devoluções, buscar títulos e listar o catálogo. Aplica as seguintes estruturas de dados: **lista, fila (FIFO), pilha (LIFO), dicionário e tupla**.

---

## 2. Explicação Conceitual

### 🔷 Fila — FIFO (First In, First Out)

Uma fila funciona como a fila de um caixa de supermercado: quem chega primeiro é atendido primeiro. No Python, usamos uma lista comum com `.append()` para inserir no final e `.pop(0)` para retirar do início.

No nosso sistema, a `fila_reservas` representa os filmes disponíveis aguardando aluguel. Um novo filme cadastrado entra no **final** da fila; quando um cliente aluga, o filme do **início** (o que está há mais tempo disponível) é retirado primeiro.

```python
# dados.py
fila_reservas = []

# cadastrar_filme() — entra no FINAL da fila
dados.fila_reservas.append(filme)

# registrar_aluguel() — sai pelo INÍCIO — FIFO
filme_alugado = dados.fila_reservas.pop(0)
```

---

### 🔷 Pilha — LIFO (Last In, First Out)

Uma pilha funciona como uma pilha de pratos: o último prato colocado é o primeiro a ser retirado. No Python, usamos `.append()` para empilhar e `reversed()` para exibir do topo à base sem alterar a estrutura.

No nosso sistema, a `pilha_devolucoes` registra o histórico de devoluções. Cada devolução registrada vai para o **topo** da pilha. Ao exibir o histórico, usamos `reversed()` para que a devolução mais recente apareça primeiro.

```python
# dados.py
pilha_devolucoes = []

# registrar_devolucao() — empilha no TOPO — LIFO
dados.pilha_devolucoes.append(registro)

# ver_historico_devolucoes() — lê do topo à base
for registro in reversed(dados.pilha_devolucoes):
    print(registro['filme'], '—', registro['cliente'])
```

---

### 🔷 Dicionário

Cada filme do sistema é armazenado como um dicionário Python — uma estrutura de pares chave-valor. Isso permite agrupar todos os atributos de um filme em uma única variável e acessar qualquer campo pelo nome, não pela posição.

```python
# cadastrar_filme()
filme = {
    'id':          dados.gerar_id(),
    'titulo':      titulo,
    'genero':      genero,
    'ano':         ano,
    'status':      dados.STATUS_FILME[0],   # 'Disponível'
    'alugado_por': None,
}

# Atualizar o status ao alugar:
filme['status']      = dados.STATUS_FILME[1]   # 'Alugado'
filme['alugado_por'] = cliente
```

---

### 🔷 Lista × Tupla

**Lista** (`catalogo = []`) é mutável: filmes são adicionados com `.append()` e podem ser removidos. Usamos lista onde o conteúdo precisa mudar durante a execução.

**Tupla** (`STATUS_FILME`, `GENEROS`) é imutável: os valores são fixos e não podem ser alterados acidentalmente. Usamos tupla para categorias que devem permanecer constantes durante toda a execução.

```python
# dados.py
STATUS_FILME = ('Disponível', 'Alugado')          # tupla — imutável
GENEROS      = ('Ação', 'Comédia', 'Drama', ...)  # tupla — imutável
catalogo     = []                                  # lista — mutável

# Acesso à tupla pelo índice:
filme['status'] = dados.STATUS_FILME[0]   # 'Disponível'
filme['status'] = dados.STATUS_FILME[1]   # 'Alugado'
```

---

### 🔷 Modularização

O projeto foi dividido em **4 arquivos `.py`**, cada um com uma responsabilidade específica:

| Arquivo | Responsabilidade |
|---|---|
| `dados.py` | Declara as variáveis globais: lista, fila, pilha, tuplas e gerador de ID |
| `filmes.py` | Contém todas as funções de regra de negócio: cadastrar, alugar, devolver, listar, buscar |
| `utils.py` | Funções auxiliares: exibir título, separador, validações de entrada com `try/except` |
| `main.py` | Ponto de entrada: menu principal com `while True` e desvios `if/elif` |

Cada módulo importa apenas o que precisa:

```python
# main.py importa funções de filmes.py
from filmes import cadastrar_filme, listar_catalogo, registrar_aluguel, ...

# filmes.py importa dados e utils
import dados
from utils import escolher_genero, ler_ano, ...
```

---

## 3. Como Executar o Projeto

**Requisitos:** Python 3.10 ou superior. Nenhuma biblioteca externa necessária.

```bash
# Clone ou baixe o repositório, entre na pasta e execute:
git clone https://github.com/mariaqzcr/Locadora-de-Filmes
cd Locadora-de-Filmes
python main.py
```

---

## 4. Funcionalidades Implementadas

### Obrigatórias ✅

- [x] Cadastrar filme (título, gênero, ano)
- [x] Listar catálogo completo com status de disponibilidade
- [x] Fila de reservas — FIFO: primeiro a entrar é o primeiro a ser alugado
- [x] Pilha de devoluções — LIFO: última devolução aparece primeiro no histórico
- [x] Registrar aluguel (marca filme como "Alugado" e retira da fila)
- [x] Registrar devolução (marca filme como "Disponível" e volta à fila)

### Bônus ✅

- [x] Buscar filme por título (busca parcial, sem distinção maiúsculas/minúsculas)
- [x] Listar filmes disponíveis filtrados por gênero

---

## 5. Dificuldades e Aprendizados

A maior dificuldade foi entender a diferença prática entre fila e pilha — no código ambas são listas Python, mas o que muda é **onde** se insere e **onde** se retira. Na fila usamos `.pop(0)` para retirar do início, enquanto na pilha usamos `reversed()` para ler do topo sem remover nada.

Outro ponto desafiador foi a modularização: separar o código em arquivos exige pensar em quem depende de quem, e aprendemos que `dados.py` não pode importar nenhum outro módulo do projeto para não criar dependências circulares. O tratamento de erros com `try/except` também foi importante — sem ele, digitar uma letra onde se espera um número derruba o programa inteiro.

No geral, o projeto mostrou na prática como estruturas de dados diferentes resolvem problemas diferentes, mesmo sendo implementadas com a mesma lista do Python.
