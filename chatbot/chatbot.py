##instalar a biblioteca 
##abrir cmd --> pip install transformers torch
## em caso de erro de permissão, utilizar o seguinte comando no terminal: pip install --user transformers torch
from transformers import pipeline

def main():
    chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

    print("conversa iniciada :)  digite 'sair' para encerrar.\n")

    while True:
        entrada = input("eu: ")
        if entrada.lower() == "sair":
            print("encerrando conversa... ")
            break

      
        prompot = (f"{entrada}")
        resposta = chatbot(prompot, max_new_tokens=30)
        print("bot:", resposta[0]['generated_text'])

if __name__ == "__main__":
    main()
