import streamlit as st

def calcular_drawdown(saldo_inicial, perdas_consecutivas, perda_percentual):
    saldo_atual = saldo_inicial
    drawdown_maximo = 0
    sequencia_drawdown = 0
    
    st.markdown("### Resultados")
    
    tabela_resultados = []
    tabela_resultados.append(["Período", "Saldo Atual", "Perda"])
    
    for i in range(perdas_consecutivas):
        perda = saldo_atual * (perda_percentual / 100)
        saldo_atual = round(saldo_atual - perda, 2)
        
        if saldo_atual < drawdown_maximo:
            drawdown_maximo = saldo_atual
        
        if perda > 0:
            sequencia_drawdown += 1
        else:
            sequencia_drawdown = 0
        
        tabela_resultados.append([i+1, saldo_atual, perda])
        
        perda_total = saldo_inicial - saldo_atual
        perda_percentual_total = (perda_total / saldo_inicial) * 100
        saldo_final = saldo_atual
        
        if sequencia_drawdown == 10 and perda_percentual_total >= 20:
            break
    
    st.table(tabela_resultados)
    
    st.markdown("### Resumo")
    
    if saldo_atual <= 0 or (sequencia_drawdown == 10 and perda_percentual_total >= 20):
        risco_ruina = True
        st.error("Risco de Ruína: Sim")
    else:
        risco_ruina = False
        st.success("Risco de Ruína: Não")
    
    tabela_resumo = []
    tabela_resumo.append(["Saldo Inicial", "Perda Total", "Saldo Final"])
    tabela_resumo.append([saldo_inicial, perda_total, saldo_final])
    
    st.table(tabela_resumo)

# Interface do Streamlit
st.title("Calculadora de Drawdown e Risco Ruína")

saldo_inicial = st.number_input("Informe o saldo inicial (banca):")
perdas_consecutivas = st.number_input("Informe o número de perdas consecutivas:", step=1, min_value=0)
perda_percentual = st.number_input("Informe a porcentagem de perda por operação:", step=0.01, format="%.2f")

if st.button("Calcular"):
    calcular_drawdown(saldo_inicial, perdas_consecutivas, perda_percentual)
