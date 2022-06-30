from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


#class EnviadorMock(Enviador):

 #   def __init__(self):
  #      super().__init__()
   #     self.qtd_email_enviados = 0
    #    self.parametros_de_envio = None

#    def enviar(self, remetente, destinatario, assunto, corpo):
#        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
#        self.qtd_email_enviados += 1

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Luiz', email='luiz@gmail.com'),
            Usuario(nome='Henrique', email='luiz@gmail.com')
        ],
        [
            Usuario(nome='Luiz', email='luiz@gmail.com')
        ]
     ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luizlins22@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count #enviador.qtd_email_enviados





def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Luiz', email='luiz@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'henrique@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    #assert enviador.parametros_de_envio == (
    enviador.enviar.assert_called_once_with(
        'henrique@gmail.com',
        'luiz@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
