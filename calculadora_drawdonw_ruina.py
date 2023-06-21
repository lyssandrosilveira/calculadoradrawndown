import streamlit as st
from tabulate import tabulate
from colorama import Fore, Back, Style

def calcular_drawdown(saldo_inicial, perdas_consecutivas, perda_percentual):
    saldo_atual = saldo_inicial
    drawdown_maximo = 0
    sequencia_drawdown = 0
    tabela_resultados = []
    
    for i in range(perdas_consecutivas):
        perda = saldo_atual * (perda_percentual / 100)
        saldo_atual = round(saldo_atual - perda, 2)
        
        if saldo_atual < drawdown_maximo:
            drawdown_maximo = saldo_atual
        
        if perda > 0:
            sequencia_drawdown += 1
        else:
            sequencia_drawdown = 0
        
        tabela_resultados.append([i+1, format(saldo_atual, ".2f"), format(perda, ".2f")])
        
        perda_total = saldo_inicial - saldo_atual
        perda_percentual_total = (perda_total / saldo_inicial) * 100
        saldo_final = saldo_atual
        
        if sequencia_drawdown == 10 and perda_percentual_total >= 20:
            break
    
    tabela_cabecalho = ['Período', 'Saldo Atual', 'Perda']
    
    st.write(tabulate(tabela_resultados, headers=tabela_cabecalho, tablefmt='github'))
    
    if saldo_atual <= 0 or (sequencia_drawdown == 10 and perda_percentual_total >= 20):
        risco_ruina = True
        st.error("Risco de Ruína: Sim")
    else:
        risco_ruina = False
        st.success("Risco de Ruína: Não")
    
    tabela_resumo = [[saldo_inicial, format(perda_total, ".2f") + " (" + format(perda_percentual_total, ".2f") + "%)", saldo_final]]
    tabela_cabecalho_resumo = ['Saldo Inicial', 'Perda Total', 'Saldo Final']
    
    st.write(tabulate(tabela_resumo, headers=tabela_cabecalho_resumo, tablefmt='github'))

# Interface do Streamlit
st.title("Calculadora de Drawdown e Risco Ruina")

saldo_inicial = st.number_input("Informe o saldo inicial (banca):")
perdas_consecutivas = st.number_input("Informe o número de perdas consecutivas:", step=1, min_value=0)
perda_percentual = st.number_input("Informe a porcentagem de perda por operação:", step=0.01, format="%.2f")

if st.button("Calcular"):
    calcular_drawdown(saldo_inicial, perdas_consecutivas, perda_percentual)

