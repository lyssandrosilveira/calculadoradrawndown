import streamlit as st

def calculate_drawdown(pico, vale):
    dd = (vale - pico) / pico
    return dd

def main():
    st.title("Calculadora de Drawdown")

    pico = st.number_input("Valor do Pico", value=3.54)
    vale = st.number_input("Valor do Vale", value=0.46)

    if st.button("Calcular Drawdown"):
        drawdown = calculate_drawdown(pico, vale)
        drawdown_percentage = round(drawdown * 100, 2)
        st.write("Drawdown: {}%".format(drawdown_percentage))

if __name__ == '__main__':
    main()
