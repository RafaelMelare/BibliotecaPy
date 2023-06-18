class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_livros_emprestados(self):
        return self.livros_emprestados
    
    def add_livro_emprestado(self,livro):
        self.livros_emprestados.append(livro)
    
    def remove_livro_emprestado(self,livro):
        self.livros_emprestados.remove(livro)