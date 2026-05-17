<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🎬 Locadora de Filmes</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --cream: #f5f0e8;
    --dark: #1a1208;
    --red: #c8372d;
    --red-light: #e8453a;
    --gold: #d4a847;
    --gold-light: #f0c860;
    --film: #2a1f0e;
    --text: #3a2e1a;
    --muted: #7a6a50;
    --border: #d4c8a8;
    --code-bg: #1a1208;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background-color: var(--cream);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    overflow-x: hidden;
  }

  /* FILM STRIP HEADER */
  .filmstrip {
    background: var(--dark);
    padding: 0;
    display: flex;
    align-items: center;
    overflow: hidden;
    height: 40px;
    position: relative;
  }
  .filmstrip-holes {
    display: flex;
    gap: 0;
    width: 100%;
    justify-content: space-around;
  }
  .hole {
    width: 20px;
    height: 28px;
    background: var(--cream);
    border-radius: 3px;
    opacity: 0.9;
    flex-shrink: 0;
  }

  /* HERO */
  .hero {
    background: var(--dark);
    position: relative;
    padding: 80px 48px 100px;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: 
      radial-gradient(ellipse at 20% 50%, rgba(200, 55, 45, 0.15) 0%, transparent 60%),
      radial-gradient(ellipse at 80% 20%, rgba(212, 168, 71, 0.1) 0%, transparent 50%);
  }
  .hero-grid {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
      linear-gradient(rgba(212, 168, 71, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(212, 168, 71, 0.04) 1px, transparent 1px);
    background-size: 60px 60px;
  }
  .hero-tag {
    display: inline-block;
    background: var(--red);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    padding: 5px 14px;
    text-transform: uppercase;
    margin-bottom: 32px;
    position: relative;
  }
  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 8vw, 96px);
    font-weight: 900;
    color: var(--cream);
    line-height: 0.9;
    position: relative;
    margin-bottom: 8px;
  }
  .hero h1 em {
    font-style: italic;
    color: var(--gold);
  }
  .hero-sub {
    font-family: 'DM Mono', monospace;
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 0.08em;
    margin-top: 28px;
    position: relative;
  }
  .hero-meta {
    display: flex;
    gap: 40px;
    margin-top: 48px;
    position: relative;
  }
  .meta-item {
    border-left: 2px solid var(--red);
    padding-left: 16px;
  }
  .meta-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .meta-value {
    font-size: 14px;
    color: var(--cream);
    font-weight: 400;
  }
  .reel-deco {
    position: absolute;
    right: -20px;
    top: 50%;
    transform: translateY(-50%);
    width: 280px;
    height: 280px;
    opacity: 0.06;
  }
  .reel-deco circle { fill: none; stroke: var(--gold); }
  .hero-badge {
    position: absolute;
    top: 40px;
    right: 48px;
    width: 90px;
    height: 90px;
    border: 2px solid var(--gold);
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: var(--gold);
    font-family: 'DM Mono', monospace;
    text-align: center;
    opacity: 0.7;
  }
  .hero-badge .yr { font-size: 22px; font-weight: 500; line-height: 1; }
  .hero-badge .lbl { font-size: 9px; letter-spacing: 0.1em; opacity: 0.7; }

  /* MAIN CONTENT */
  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 48px 80px;
  }

  /* SECTION */
  .section {
    padding: 64px 0;
    border-bottom: 1px solid var(--border);
  }
  .section:last-child { border-bottom: none; }

  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--red);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
    max-width: 60px;
  }

  .section h2 {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 20px;
    line-height: 1.1;
  }

  .section p {
    font-size: 15px;
    line-height: 1.75;
    color: var(--text);
    max-width: 680px;
  }

  /* ESTRUTURAS DE DADOS */
  .data-structures {
    display: grid;
    gap: 0;
    margin-top: 40px;
  }

  .ds-card {
    display: grid;
    grid-template-columns: 80px 1fr;
    border: 1px solid var(--border);
    border-bottom: none;
    overflow: hidden;
    transition: background 0.2s;
  }
  .ds-card:last-child { border-bottom: 1px solid var(--border); }
  .ds-card:hover { background: rgba(212, 168, 71, 0.04); }

  .ds-number {
    background: var(--dark);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    color: var(--gold);
    font-style: italic;
    border-right: 1px solid var(--border);
  }

  .ds-body {
    padding: 28px 32px;
  }

  .ds-header {
    display: flex;
    align-items: baseline;
    gap: 14px;
    margin-bottom: 10px;
  }

  .ds-title {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--dark);
  }

  .ds-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 3px 10px;
    border-radius: 2px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }
  .badge-fifo { background: rgba(200, 55, 45, 0.1); color: var(--red); border: 1px solid rgba(200, 55, 45, 0.3); }
  .badge-lifo { background: rgba(212, 168, 71, 0.1); color: #a07820; border: 1px solid rgba(212, 168, 71, 0.3); }
  .badge-dict { background: rgba(40, 100, 160, 0.08); color: #3060a0; border: 1px solid rgba(40, 100, 160, 0.2); }
  .badge-col  { background: rgba(60, 140, 80, 0.08); color: #306040; border: 1px solid rgba(60, 140, 80, 0.2); }

  .ds-desc {
    font-size: 14px;
    line-height: 1.65;
    color: var(--muted);
    margin-bottom: 16px;
  }

  /* CODE BLOCKS */
  pre {
    background: var(--code-bg);
    border-left: 3px solid var(--gold);
    padding: 20px 24px;
    overflow-x: auto;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 1.7;
    color: #d4c8a8;
    margin-top: 4px;
  }
  .comment { color: #5a5040; }
  .keyword { color: #c8372d; }
  .string { color: #d4a847; }
  .func { color: #7ab8d4; }
  .attr { color: #a8d870; }

  /* MODULARIZATION TABLE */
  .mod-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 32px;
    font-size: 14px;
  }
  .mod-table th {
    background: var(--dark);
    color: var(--gold);
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 14px 20px;
    text-align: left;
    font-weight: 400;
  }
  .mod-table td {
    padding: 16px 20px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.5;
  }
  .mod-table tr:hover td { background: rgba(212, 168, 71, 0.04); }
  .file-name {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: var(--red);
    white-space: nowrap;
  }
  .file-resp { color: var(--muted); font-size: 13.5px; }

  /* FUNCIONALIDADES */
  .features-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 32px;
  }
  .feature-group {
    border: 1px solid var(--border);
    padding: 28px;
  }
  .feature-group h3 {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .feat-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .dot-green { background: #5aad60; }
  .dot-gold { background: var(--gold); }

  .feature-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 12px;
    font-size: 13.5px;
    line-height: 1.4;
    color: var(--text);
  }
  .feature-item::before {
    content: '✓';
    color: #5aad60;
    font-weight: 700;
    font-size: 13px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  /* HOW TO RUN */
  .run-box {
    margin-top: 32px;
    border: 1px solid var(--border);
    overflow: hidden;
  }
  .run-header {
    background: var(--dark);
    padding: 14px 24px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .run-dot { width: 12px; height: 12px; border-radius: 50%; }
  .r1 { background: #ff5f57; }
  .r2 { background: #febc2e; }
  .r3 { background: #28c840; }
  .run-title {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    margin-left: 8px;
  }
  .run-body {
    background: var(--code-bg);
    padding: 24px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #a0d880;
  }
  .run-body .prompt { color: #5a7040; margin-right: 8px; }

  /* DIFICULDADES */
  .learning-box {
    background: var(--dark);
    padding: 40px;
    margin-top: 32px;
    position: relative;
    overflow: hidden;
  }
  .learning-box::before {
    content: '"';
    position: absolute;
    top: -20px;
    left: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 160px;
    color: var(--gold);
    opacity: 0.08;
    line-height: 1;
  }
  .learning-box p {
    font-size: 15px;
    line-height: 1.8;
    color: #a09080;
    position: relative;
    max-width: 700px;
  }
  .learning-box p strong {
    color: var(--gold);
    font-weight: 500;
  }

  /* TEAM */
  .team-grid {
    display: flex;
    gap: 0;
    margin-top: 32px;
    border: 1px solid var(--border);
    overflow: hidden;
  }
  .team-member {
    flex: 1;
    padding: 28px 24px;
    border-right: 1px solid var(--border);
    text-align: center;
  }
  .team-member:last-child { border-right: none; }
  .member-initial {
    width: 48px;
    height: 48px;
    background: var(--dark);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    color: var(--gold);
    margin: 0 auto 12px;
    font-style: italic;
  }
  .member-name {
    font-size: 12px;
    color: var(--text);
    line-height: 1.4;
    font-weight: 400;
  }

  /* FOOTER */
  .footer-strip { background: var(--dark); }

  /* ANIMATIONS */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .hero > * { animation: fadeUp 0.7s ease forwards; }
  .hero > *:nth-child(2) { animation-delay: 0.1s; }
  .hero > *:nth-child(3) { animation-delay: 0.2s; }
  .hero > *:nth-child(4) { animation-delay: 0.3s; }
</style>
</head>
<body>

<!-- Film strip top -->
<div class="filmstrip">
  <div class="filmstrip-holes">
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
  </div>
</div>

<!-- HERO -->
<div class="hero">
  <div class="hero-grid"></div>
  <svg class="reel-deco" viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg">
    <circle cx="140" cy="140" r="130" stroke-width="2"/>
    <circle cx="140" cy="140" r="100" stroke-width="1"/>
    <circle cx="140" cy="140" r="70" stroke-width="3"/>
    <circle cx="140" cy="140" r="30" stroke-width="2"/>
    <line x1="140" y1="10" x2="140" y2="270" stroke="rgba(212,168,71,0.15)" stroke-width="1"/>
    <line x1="10" y1="140" x2="270" y2="140" stroke="rgba(212,168,71,0.15)" stroke-width="1"/>
    <line x1="42" y1="42" x2="238" y2="238" stroke="rgba(212,168,71,0.1)" stroke-width="1"/>
    <line x1="238" y1="42" x2="42" y2="238" stroke="rgba(212,168,71,0.1)" stroke-width="1"/>
  </svg>

  <div class="hero-badge">
    <span class="yr">2026</span>
    <span class="lbl">PROJETO</span>
  </div>

  <div class="hero-tag">Programação de Computadores · Python</div>
  <h1>Gerenciador<br>de <em>Locadora</em></h1>
  <p class="hero-sub">Sistema em Python · Estruturas de Dados · Modularização</p>

  <div class="hero-meta">
    <div class="meta-item">
      <div class="meta-label">Disciplina</div>
      <div class="meta-value">Programação de Computadores</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Professora</div>
      <div class="meta-value">Profa. Dra. Andrea Ono Sakai</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Período</div>
      <div class="meta-value">Diurno · 2026</div>
    </div>
  </div>
</div>

<!-- Film strip bottom -->
<div class="filmstrip">
  <div class="filmstrip-holes">
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
  </div>
</div>

<div class="container">

  <!-- DESCRIÇÃO -->
  <div class="section">
    <div class="section-label">01 · Descrição</div>
    <h2>O que é o projeto?</h2>
    <p>
      Sistema de gerenciamento de uma locadora de filmes desenvolvido em Python, dividido em múltiplos arquivos. 
      Permite cadastrar filmes, registrar aluguéis e devoluções, buscar títulos e listar o catálogo — 
      aplicando na prática as estruturas de dados: <strong>lista, fila (FIFO), pilha (LIFO), dicionário e tupla</strong>.
    </p>
  </div>

  <!-- ESTRUTURAS DE DADOS -->
  <div class="section">
    <div class="section-label">02 · Conceitos</div>
    <h2>Estruturas de Dados</h2>

    <div class="data-structures">

      <!-- FILA -->
      <div class="ds-card">
        <div class="ds-number">I</div>
        <div class="ds-body">
          <div class="ds-header">
            <span class="ds-title">Fila</span>
            <span class="ds-badge badge-fifo">FIFO · First In, First Out</span>
          </div>
          <p class="ds-desc">
            Funciona como a fila de um caixa de supermercado: quem chega primeiro é atendido primeiro.
            A <code style="font-family:'DM Mono',monospace;font-size:12px;background:rgba(0,0,0,0.06);padding:1px 5px">fila_reservas</code> representa os filmes disponíveis. 
            Novo filme entra no <strong>final</strong>; ao alugar, sai pelo <strong>início</strong>.
          </p>
          <pre><span class="comment"># dados.py</span>
fila_reservas = []

<span class="comment"># cadastrar_filme() — entra no FINAL</span>
dados.fila_reservas.<span class="func">append</span>(filme)

<span class="comment"># registrar_aluguel() — sai pelo INÍCIO</span>
filme_alugado = dados.fila_reservas.<span class="func">pop</span>(0)</pre>
        </div>
      </div>

      <!-- PILHA -->
      <div class="ds-card">
        <div class="ds-number">II</div>
        <div class="ds-body">
          <div class="ds-header">
            <span class="ds-title">Pilha</span>
            <span class="ds-badge badge-lifo">LIFO · Last In, First Out</span>
          </div>
          <p class="ds-desc">
            Como uma pilha de pratos: o último colocado é o primeiro retirado.
            A <code style="font-family:'DM Mono',monospace;font-size:12px;background:rgba(0,0,0,0.06);padding:1px 5px">pilha_devolucoes</code> registra o histórico.
            Usamos <code style="font-family:'DM Mono',monospace;font-size:12px;background:rgba(0,0,0,0.06);padding:1px 5px">reversed()</code> para exibir do topo à base sem alterar a estrutura.
          </p>
          <pre><span class="comment"># dados.py</span>
pilha_devolucoes = []

<span class="comment"># registrar_devolucao() — empilha no TOPO</span>
dados.pilha_devolucoes.<span class="func">append</span>(registro)

<span class="comment"># ver_historico_devolucoes() — lê do topo</span>
<span class="keyword">for</span> reg <span class="keyword">in</span> <span class="func">reversed</span>(dados.pilha_devolucoes):
    <span class="func">print</span>(reg[<span class="string">'filme'</span>], <span class="string">'—'</span>, reg[<span class="string">'cliente'</span>])</pre>
        </div>
      </div>

      <!-- DICIONÁRIO -->
      <div class="ds-card">
        <div class="ds-number">III</div>
        <div class="ds-body">
          <div class="ds-header">
            <span class="ds-title">Dicionário</span>
            <span class="ds-badge badge-dict">Pares Chave–Valor</span>
          </div>
          <p class="ds-desc">
            Cada filme é um dicionário Python — agrupa todos os atributos em uma única variável 
            e permite acessar qualquer campo pelo nome, não pela posição.
          </p>
          <pre>filme = {
    <span class="attr">'id'</span>:          dados.<span class="func">gerar_id</span>(),
    <span class="attr">'titulo'</span>:      titulo,
    <span class="attr">'genero'</span>:      genero,
    <span class="attr">'ano'</span>:         ano,
    <span class="attr">'status'</span>:      dados.STATUS_FILME[0],  <span class="comment"># 'Disponível'</span>
    <span class="attr">'alugado_por'</span>: <span class="keyword">None</span>,
}

<span class="comment"># Atualizar ao alugar:</span>
filme[<span class="attr">'status'</span>]      = dados.STATUS_FILME[1]  <span class="comment"># 'Alugado'</span>
filme[<span class="attr">'alugado_por'</span>] = cliente</pre>
        </div>
      </div>

      <!-- LISTA × TUPLA -->
      <div class="ds-card">
        <div class="ds-number">IV</div>
        <div class="ds-body">
          <div class="ds-header">
            <span class="ds-title">Lista × Tupla</span>
            <span class="ds-badge badge-col">Mutável · Imutável</span>
          </div>
          <p class="ds-desc">
            <strong>Lista</strong> é mutável: filmes são adicionados e removidos dinamicamente.
            <strong>Tupla</strong> é imutável: usada para valores fixos como status e gêneros — garantindo que não sejam alterados acidentalmente.
          </p>
          <pre><span class="comment"># dados.py</span>
STATUS_FILME = (<span class="string">'Disponível'</span>, <span class="string">'Alugado'</span>)   <span class="comment"># tupla</span>
GENEROS      = (<span class="string">'Ação'</span>, <span class="string">'Comédia'</span>, <span class="string">'Drama'</span>, ...)  <span class="comment"># tupla</span>
catalogo     = []   <span class="comment"># lista — mutável</span>

<span class="comment"># Acesso pelo índice:</span>
filme[<span class="attr">'status'</span>] = dados.STATUS_FILME[0]   <span class="comment"># 'Disponível'</span>
filme[<span class="attr">'status'</span>] = dados.STATUS_FILME[1]   <span class="comment"># 'Alugado'</span></pre>
        </div>
      </div>

    </div>
  </div>

  <!-- MODULARIZAÇÃO -->
  <div class="section">
    <div class="section-label">03 · Arquitetura</div>
    <h2>Modularização</h2>
    <p>O projeto é dividido em <strong>4 arquivos</strong>, cada um com responsabilidade específica, evitando dependências circulares.</p>

    <table class="mod-table">
      <thead>
        <tr>
          <th>Arquivo</th>
          <th>Responsabilidade</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="file-name">dados.py</span></td>
          <td class="file-resp">Declara as variáveis globais: lista, fila, pilha, tuplas e gerador de ID</td>
        </tr>
        <tr>
          <td><span class="file-name">filmes.py</span></td>
          <td class="file-resp">Todas as funções de regra de negócio: cadastrar, alugar, devolver, listar, buscar</td>
        </tr>
        <tr>
          <td><span class="file-name">utils.py</span></td>
          <td class="file-resp">Funções auxiliares: exibir título, separador, validações com <code style="font-family:'DM Mono',monospace;font-size:12px">try/except</code></td>
        </tr>
        <tr>
          <td><span class="file-name">main.py</span></td>
          <td class="file-resp">Ponto de entrada: menu principal com <code style="font-family:'DM Mono',monospace;font-size:12px">while True</code> e desvios <code style="font-family:'DM Mono',monospace;font-size:12px">if/elif</code></td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- COMO EXECUTAR -->
  <div class="section">
    <div class="section-label">04 · Execução</div>
    <h2>Como Executar</h2>
    <p>Requisitos: <strong>Python 3.10+</strong>. Nenhuma biblioteca externa necessária.</p>

    <div class="run-box">
      <div class="run-header">
        <div class="run-dot r1"></div>
        <div class="run-dot r2"></div>
        <div class="run-dot r3"></div>
        <span class="run-title">terminal</span>
      </div>
      <div class="run-body">
        <div><span class="prompt">$</span> git clone https://github.com/mariaqzcr/Locadora-de-Filmes</div>
        <div><span class="prompt">$</span> cd Locadora-de-Filmes</div>
        <div><span class="prompt">$</span> python main.py</div>
      </div>
    </div>
  </div>

  <!-- FUNCIONALIDADES -->
  <div class="section">
    <div class="section-label">05 · Funcionalidades</div>
    <h2>O que o sistema faz</h2>

    <div class="features-grid">
      <div class="feature-group">
        <h3><span class="feat-dot dot-green"></span>Obrigatórias</h3>
        <div class="feature-item">Cadastrar filme (título, gênero, ano)</div>
        <div class="feature-item">Listar catálogo completo com status de disponibilidade</div>
        <div class="feature-item">Fila de reservas — FIFO: primeiro a entrar é o primeiro alugado</div>
        <div class="feature-item">Pilha de devoluções — LIFO: última devolução aparece primeiro</div>
        <div class="feature-item">Registrar aluguel (marca como "Alugado", retira da fila)</div>
        <div class="feature-item">Registrar devolução (marca como "Disponível", volta à fila)</div>
      </div>
      <div class="feature-group">
        <h3><span class="feat-dot dot-gold"></span>Bônus</h3>
        <div class="feature-item">Buscar filme por título (parcial, sem distinção maiúsculas/minúsculas)</div>
        <div class="feature-item">Listar filmes disponíveis filtrados por gênero</div>
      </div>
    </div>
  </div>

  <!-- APRENDIZADOS -->
  <div class="section">
    <div class="section-label">06 · Reflexão</div>
    <h2>Dificuldades e Aprendizados</h2>

    <div class="learning-box">
      <p>
        A maior dificuldade foi entender a diferença prática entre fila e pilha — no código ambas são listas Python, 
        mas o que muda é <strong>onde se insere e onde se retira</strong>. Na fila usamos <code style="font-family:'DM Mono',monospace;font-size:12px;color:#d4a847">.pop(0)</code> para retirar do início; 
        na pilha usamos <code style="font-family:'DM Mono',monospace;font-size:12px;color:#d4a847">reversed()</code> para ler do topo sem remover nada.
        <br><br>
        A modularização também foi desafiadora: separar o código em arquivos exige pensar em <strong>quem depende de quem</strong>. 
        Aprendemos que <code style="font-family:'DM Mono',monospace;font-size:12px;color:#d4a847">dados.py</code> não pode importar nenhum outro módulo do projeto para não criar 
        dependências circulares. O projeto mostrou na prática como <strong>estruturas de dados diferentes resolvem problemas diferentes</strong>, 
        mesmo sendo implementadas com a mesma lista do Python.
      </p>
    </div>
  </div>

  <!-- EQUIPE -->
  <div class="section">
    <div class="section-label">07 · Equipe</div>
    <h2>Integrantes</h2>

    <div class="team-grid">
      <div class="team-member">
        <div class="member-initial">F</div>
        <div class="member-name">Felipe Pereira Roberto</div>
      </div>
      <div class="team-member">
        <div class="member-initial">M</div>
        <div class="member-name">Maria Eduarda Queiroz Correa</div>
      </div>
      <div class="team-member">
        <div class="member-initial">O</div>
        <div class="member-name">Omar Alejandro de Jesus Bravo Hernandez</div>
      </div>
    </div>
  </div>

</div>

<!-- FOOTER STRIP -->
<div class="filmstrip footer-strip">
  <div class="filmstrip-holes">
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
    <div class="hole"></div><div class="hole"></div><div class="hole"></div><div class="hole"></div>
  </div>
</div>

</body>
</html>
