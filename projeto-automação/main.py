import requests

def obter_clima(cidade, chave_api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    
    print(f"Status code: {resposta.status_code}")
    print(f"Resposta: {resposta.text}")

    if resposta.status_code == 200:
        dados = resposta.json()
        temp = dados["main"]["temp"]
        sensacao = dados["main"]["feels_like"]
        descricao = dados["weather"][0]["description"]
        print(f"\n clima em {cidade.title()}:")
        print(f"temperatura: {temp}°C")
        print(f"sensação térmica: {sensacao}°C")
        print(f"condição: {descricao}")

        # alertas
        if temp > 30:
            print(" alerta: está muito quente, ative o resfriamento!")
        elif "chuva" in descricao:
            print(" cuidado: está chovendo, verifique coberturas!")
    else:
        print(" erro ao obter dados. verifique se digitou corretamente.")

# ---- CONFIG ----
cidade = input("digite o nome da cidade: ")
chave = "d5fbf89bdc9b3504227be6ab8446c56d"  # api
obter_clima(cidade, chave)