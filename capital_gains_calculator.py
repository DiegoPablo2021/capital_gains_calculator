import json

TAXA_IMPOSTO = 0.20

def calcular_imposto(operacoes, prejuizo_anterior=0):
  total_imposto = 0
  prejuizo_atual = 0
  
  for operacao in operacoes:
    if operacao["operacao"] == "compra":
      valor_compra = round(operacao["valor"], 2)
      nova_media_ponderada = ((operacao["quantidade"] * valor_compra) + (prejuizo_anterior * operacao["quantidade"])) / (operacao["quantidade"] + prejuizo_anterior)
      prejuizo_anterior = 0
    elif operacao["operacao"] == "venda":
      valor_venda = round(operacao["valor"], 2)
      lucro = (valor_venda - nova_media_ponderada) * operacao["quantidade"]
      if lucro > 0:
        imposto = lucro * TAXA_IMPOSTO
        total_imposto += imposto
      else:
        prejuizo_atual += lucro
    else:
      raise ValueError("Operação inválida: {}".format(operacao["operacao"]))

  return total_imposto, prejuizo_atual

def ler_operacoes():
  operacoes = []
  while True:
    linha = input()
    if not linha:
      break
    operacao = json.loads(linha)
    operacoes.append(operacao)
  return operacoes

  
def main():
  casos = [
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 100},
      {"operacao": "venda", "valor": 15.00, "quantidade": 50},
      {"operacao": "venda", "valor": 15.00, "quantidade": 50},
    ],
    
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 10000},
      {"operacao": "venda", "valor": 20.00, "quantidade": 5000},
      {"operacao": "venda", "valor": 5.00, "quantidade": 5000},
    ],
    
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 100},
      {"operacao": "venda", "valor": 12.00, "quantidade": 50},
      {"operacao": "venda", "valor": 11.00, "quantidade": 50},
    ],
    
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 10000},
      {"operacao": "venda", "valor": 5.00, "quantidade": 5000},
      {"operacao": "venda", "valor": 20.00, "quantidade": 3000},
    ],
    
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 10000},
      {"operacao": "venda", "valor": 15.00, "quantidade": 10000},
    ],
    
    [
      {"operacao": "compra", "valor": 20.00, "quantidade": 10000},
      {"operacao": "venda", "valor": 2.00, "quantidade": 5000},
      {"operacao": "venda", "valor": 20.00, "quantidade": 5000},
    ],
    
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 10000},
      {"operacao": "venda", "valor": 12.00, "quantidade": 5000},
      {"operacao": "venda", "valor": 20.00, "quantidade": 5000},
      {"operacao": "venda", "valor": 25.00, "quantidade": 1000},
    ],
    
    [
      {"operacao": "compra", "valor": 10.00, "quantidade": 10000},
      {"operacao": "venda", "valor": 5.00, "quantidade": 5000},
      {"operacao": "venda", "valor": 20.00, "quantidade": 3000},
    ],
    
  ]

  for caso in casos:
    imposto, prejuizo = calcular_imposto(caso)
    print("-" * 20)
    print("Caso:", caso)
    print(f"Imposto: {imposto:.2f}")
    print(f"Prejuízo: {prejuizo:.2f}")


if __name__ == "__main__":
  main()
