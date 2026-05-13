# =============================================================
# main.py — Ponto de entrada do Gerenciador de Locadora
# Responsabilidade: exibir o menu principal e direcionar
#                   as escolhas do usuário para as funções
#                   dos módulos correspondentes.
# =============================================================

from filmes import (cadastrar_filme, listar_catalogo,
                    registrar_aluguel, registrar_devolucao,
                    ver_historico_devolucoes, buscar_por_titulo,
                    listar_disponiveis_por_genero)


def exibir_menu():
    """Imprime as opções do menu principal na tela."""
    print()
    print('╔══════════════════════════════════════╗')
    print('║     LOCADORA DE FILMES — MENU        ║')
    print('╠══════════════════════════════════════╣')
    print('║  1. Cadastrar filme                  ║')
    print('║  2. Ver catálogo completo            ║')
    print('║  3. Registrar aluguel (fila FIFO)    ║')
    print('║  4. Registrar devolução              ║')
    print('║  5. Histórico de devoluções (LIFO)   ║')
    print('║  6. Buscar filme por título  [bônus] ║')
    print('║  7. Disponíveis por gênero   [bônus] ║')
    print('║  0. Sair                             ║')
    print('╚══════════════════════════════════════╝')


def main():
    """
    Função principal: loop while True que mantém o programa rodando.
    Lê a opção do usuário e chama a função correspondente via if/elif.
    O loop encerra com break quando o usuário digita 0.
    """
    print('\n  Bem-vindo ao Gerenciador de Locadora de Filmes!')

    while True:
        exibir_menu()

        try:
            opcao = int(input('  Escolha uma opção: '))
        except ValueError:
            print('  ✗ Digite apenas o número da opção.')
            continue

        if opcao == 1:
            cadastrar_filme()
        elif opcao == 2:
            listar_catalogo()
        elif opcao == 3:
            registrar_aluguel()
        elif opcao == 4:
            registrar_devolucao()
        elif opcao == 5:
            ver_historico_devolucoes()
        elif opcao == 6:
            buscar_por_titulo()
        elif opcao == 7:
            listar_disponiveis_por_genero()
        elif opcao == 0:
            print('\n  Encerrando o sistema. Até logo!\n')
            break   # encerra o loop while True
        else:
            print('  ✗ Opção inválida. Escolha entre 0 e 7.')


# Garante que main() só é chamado quando o arquivo é executado diretamente
if __name__ == '__main__':
    main()
