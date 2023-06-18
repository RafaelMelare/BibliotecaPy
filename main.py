from gerenciador_livro import GerenciadorDeLivro
from gerenciador_usuario import GerenciadorDeUsuario
from livro import Livro
from usuario import Usuario

def main():
    gerenciador_livro = GerenciadorDeLivro()
    gerenciador_usuario = GerenciadorDeUsuario()

    # Criando livros
    livro1 = Livro("Livro 1", "Autor 1", 2020)
    livro2 = Livro("Livro 2", "Autor 2", 2018)
    livro3 = Livro("Livro 3", "Autor 3", 2021)

    # Adicionando livros ao gerenciador de livros
    gerenciador_livro.adicionar_livro(livro1)
    gerenciador_livro.adicionar_livro(livro2)
    gerenciador_livro.adicionar_livro(livro3)

    # Criando usuários
    usuario1 = Usuario("Usuário 1", "usuario1@examplo.com")
    usuario2 = Usuario("Usuário 2", "usuario2@examplo.com")

    # Adicionando usuários ao gerenciador de usuários
    gerenciador_usuario.adicionar_usuario(usuario1)
    gerenciador_usuario.adicionar_usuario(usuario2)

    # Empréstimo de livros
    gerenciador_livro.emprestar_livro(usuario1, "Livro 1")
    gerenciador_livro.emprestar_livro(usuario2, "Livro 2")

    # Devolução de livros
    gerenciador_livro.devolver_livro(usuario1, "Livro 1")
    gerenciador_livro.devolver_livro(usuario2, "Livro 3")

    # Removendo usuários
    gerenciador_usuario.remover_usuario(usuario1)
    gerenciador_usuario.remover_usuario(usuario2)

if __name__ == "__main__":
    main()
