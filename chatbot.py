import openai

chave_api = 'sk-20dIjcJ4Z8-wVP2ltowVYy4XPHQ1ygxTPxxOfJhpSMT3BlbkFJF4XyCgdCseyAzGgz-6hcsycyJ2YTuv5WVYsmg77CEA'
openai.api_key = chave_api

def enviar_mensagem(mensagem):
    resposta = openai.Completion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": mensagem},
        ]
    )
    return resposta["choices"][0]["message"]

print(enviar_mensagem("Em que ano Roberto Carlos nasceu?"))