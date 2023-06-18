class GerenciadorDeUsuario:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        if usuario.get_nome() != "":
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.get_nome()}' adicionado à biblioteca.")

        else:
            print("Nome de usuário inválido.")

    def remover_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.get_nome()}' removido da biblioteca.")
        
        else:
            print(f"Usuário '{usuario.get_nome()}' não está registrado na biblioteca.")


    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.get_nome() == nome:
                return usuario
        return None
