# Integrantes: 
# Carolina Santana Ferraz   RM: 86833
# Melyssa Huang Gonçalves   RM: 558401


# Projeto de Monitoramento Ambiental

Este projeto consiste em um programa em Python completo para coleta, processamento e alerta de dados de sensores ambientais. Ele é útil para monitorar a qualidade da água em um determinado ambiente, fornecendo informações sobre temperatura, pH e turbidez.

# Detalhes do Projeto

O programa utiliza dados simulados de sensores, representados por uma lista de dicionários chamada `medicoes`. Cada dicionário contém informações sobre uma medição, incluindo a data, temperatura, pH e turbidez da água.


# Execução do Programa:

   - Após a execução do programa, ele calculará a média da temperatura, pH e turbidez com base nos dados fornecidos.
   - O programa também verificará se os valores médios estão dentro dos limites aceitáveis e emitirá alertas caso contrário.

# Outras Informações Relevantes

- O programa inclui duas funções principais: `calcular_media` para calcular a média de uma lista de números e `analisar_dados` para processar e analisar os dados de medição.
- Os alertas são acionados se a temperatura média da água estiver acima de 25°C, o pH médio estiver abaixo de 7 ou a turbidez média estiver acima de 25 NTU.
