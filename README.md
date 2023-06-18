# BibliotecaPy

Refatoração do código abaixo, de acordo com as boas práticas aprendidas.
Aqui segue as orientações do professor em relação ao que temo que alterar no código fornecido.

(1) - Analise o código fornecido e identifique problemas de design, violações dos princípios SOLID e falta de clareza no código.
(2) - Faça um relatório detalhando os problemas encontrados em cada classe e método.
(3) - Sugira melhorias para resolver os problemas identificados e tornar o código mais aderente aos princípios GoF, SOLID e Clean Code.
(4) - Escreva um documento explicando as melhorias propostas e por que elas são importantes.
(5) - Faça a refatoração do código, de acordo com as boas práticas aprendidas.

Abaixo temos o código já mencionado, disponibilizado pelo professor.

```class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def obter_titulo(self):
        return self.titulo

    def obter_autor(self):
        return self.autor

    def obter_ano_publicacao(self):
        return self.ano_publicacao

    def esta_disponivel(self):
        return self.disponivel

    def definir_disponibilidade(self, status):
        self.disponivel = status


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def obter_nome(self):
        return self.nome

    def obter_email(self):
        return self.email

    def emprestar_livro(self, livro):
        if livro.esta_disponivel():
            self.livros_emprestados.append(livro)
            livro.definir_disponibilidade(False)
            print(f"Livro '{livro.obter_titulo()}' emprestado para {self.nome}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.definir_disponibilidade(True)
            print(f"Livro '{livro.obter_titulo()}' devolvido por {self.nome}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não foi emprestado por {self.nome}.")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        if livro.esta_disponivel():
            self.livros.append(livro)
            print(f"Livro '{livro.obter_titulo()}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está na biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None

    def adicionar_usuario(self, usuario):
        if usuario.obter_nome() != "":
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca.")
        else:
            print("Nome de usuário inválido.")

    def remover_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.obter_nome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.obter_nome() == nome:
                return usuario
```
