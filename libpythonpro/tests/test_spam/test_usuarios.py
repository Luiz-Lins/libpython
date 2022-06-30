from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Luiz', email='luiz@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)




def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Luiz', email='luiz@gmail.com'),
        Usuario(nome='Henrique', email='luiz@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
