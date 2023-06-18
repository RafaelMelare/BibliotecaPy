class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_ano_publicacao(self):
        return self.ano_publicacao

    def is_disponivel(self):
        return self.disponivel

    def set_disponivel(self, disponivel):
        self.disponivel = disponivel