import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'luizlins22@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luiz.silva@bancorbras.com.br',
        'Cursos Python Pro',
        'Primeira Turma Aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'luizlins22gmail.com']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'luiz.silva@bancorbras.com.br',
            'Cursos Python Pro',
            'Primeira Turma Aberta.'
    )