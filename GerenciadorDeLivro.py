class GerenciadorDeLivro:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
        print(f"Livro '{livro.get_titulo()}' adicionado à biblioteca.")
            
    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.get_titulo()}' removido da biblioteca.")
        
        else:
            print(f"Livro '{livro.get_titulo()}' não está na biblioteca.")
            
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                return livro    

        return None

    def emprestar_livro(self, usuario, titulo):
        livro = self.buscar_livro(titulo)

        if livro == None:
            print(f"Livro '{titulo}' não cadastrado")

        elif  livro != None and livro.is_disponivel():
            usuario.add_livro_emprestado(livro)
            livro.set_disponivel(False)
            print(f"Livro '{titulo}' emprestado para {usuario.get_nome()}.")
        
        else:
            print(f"Livro '{titulo}' não está disponível.")

    def devolver_livro(self, usuario, titulo):
        livro = self.buscar_livro(titulo)

        if livro == None:
            print(f"Livro '{titulo}' não cadastrado")
        
        elif livro in usuario.get_livros_emprestados():
            usuario.remove_livro_emprestado(livro)
            livro.set_disponivel(True)

            print(f"Livro '{titulo}' devolvido por {usuario.get_nome()}.")
        
        else:
            print(f"Livro '{titulo}' não foi emprestado por {usuario.get_nome()}.")
        
