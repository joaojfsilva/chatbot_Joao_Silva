import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'capital de portugal': "Lisboa",
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'historia de portugal': 'Portugal tem uma rica história...',
        'horas': lambda: f'São: {datetime.now():%H:%M} horas',
        'data': lambda: f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        'qual é a tua cor favorita?': 'Minha cor favorita é azul!',
        'qual é o teu filme favorito?': 'Gosto muito de "Matrix"!',
        'qual é o teu livro favorito?': 'Adoro Os Lusíadas!',
        'gosta de aprender?': 'Sim, adoro aprender coisas novas!',
        'quem achas deste curso?': 'Fantastico, estou a adorar.'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            if callable(resposta):
                return resposta()
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
