import openai

chave_api = 'sk-20dIjcJ4Z8-wVP2ltowVYy4XPHQ1ygxTPxxOfJhpSMT3BlbkFJF4XyCgdCseyAzGgz-6hcsycyJ2YTuv5WVYsmg77CEA'
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
   
    resposta = openai.Completion.create(
        model="gpt-4o-mini",
        messages = lista_mensagens, 
    )
    return resposta["choices"][0]["message"]

lista_mensagem = []
while True:
    texto = input("Escreva aqui sua mensagem:")
    if texto == "sair":
        break
    else:
        reposta = enviar_mensagem(texto, lista_mensagem)
        lista_mensagem.append(resposta)
        print("Chatbot:", reposta["content"])
