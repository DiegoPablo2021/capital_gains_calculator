# Cálculo de Ganho de Capital

## Descrição
Este projeto implementa um programa em Python para calcular o imposto a
ser pago sobre lucros ou prejuízos de operações no mercado financeiro de ações, considerando:
1. Prejuízos anteriores
2. Isenção para vendas de até R$20.000 por mês
3. Alíquota de 20% sobre o lucro

## Arquitetura
O código é organizado em duas funções:
1. calcular_imposto: recebe uma lista de operações e calcula o imposto e o prejuízo
2. main: testa a função calcular_imposto com diversos casos de teste

## Decisões Técnicas
1. A biblioteca JSON (JavaScript Object Notation) permite que você trabalhe com dados no formato JSON em seu código.
2. A função f-string é utilizada para formatar a saída com duas casas decimais.

#Compilação e Execução
1. Salve o código em um arquivo Python (.py).
2. Execute o código usando o comando python capital_gains_calculator.py.
