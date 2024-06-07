# Programa para coleta, processamento e alerta de dados de sensores

# Dados simulados de sensores
medicoes = [
    {"data": "2024-06-01", "temperatura": 23.5, "ph": 8.1, "turbidez": 15},
    {"data": "2024-06-02", "temperatura": 24.0, "ph": 7.9, "turbidez": 20},
    {"data": "2024-06-03", "temperatura": 26.0, "ph": 7.8, "turbidez": 30},
]

# Função para calcular a média de uma lista de números
def calcular_media(valores):
    total = sum(valores)
    media = total / len(valores)
    return media

# Função para analisar dados de medições
def analisar_dados(medicoes):
    temperaturas = [medicao['temperatura'] for medicao in medicoes]
    phs = [medicao['ph'] for medicao in medicoes]
    turbidez = [medicao['turbidez'] for medicao in medicoes]

    media_temp = calcular_media(temperaturas)
    media_ph = calcular_media(phs)
    media_turb = calcular_media(turbidez)

    print(f"Média da Temperatura: {media_temp}°C")
    print(f"Média do pH: {media_ph}")
    print(f"Média da Turbidez: {media_turb} NTU")

    # Verificação de alertas
    if media_temp > 25:
        print("Alerta: Temperatura da água média alta!")
    if media_ph < 7:
        print("Alerta: pH médio abaixo do normal!")
    if media_turb > 25:
        print("Alerta: Turbidez média alta!")

# Chamada da função com dados de exemplo
analisar_dados(medicoes)

