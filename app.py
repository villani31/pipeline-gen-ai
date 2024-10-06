import streamlit as st
from datacontract import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import write_data_postgresql

def main():
    """
    Funcao main() para chamado do App Streamlit.
    """

    st.title("Sistema - Vendas de produtos")
    nome = st.text_input("Nome completo do vendedor:")
    email = st.text_input("Digite o email do vendedor:")
    data = st.date_input("Data da venda:", datetime.now())
    hora = st.time_input("Hora da venda:", value=time(9, 0))
    valor = st.number_input("Valor da venda:", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos vendido:", min_value=1, step=1)
    produto = st.selectbox("Produto vendido:",
                           options=["Produto 01",
                                    "Produto 02",
                                    "Produto 03"])

    if (st.button("Salvar venda")):
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                nome = nome,
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            # print na tela
            st.write("Dados que serão gravado no Banco de dados:")
            st.write(venda)

            # gravar no banco de dados
            write_data_postgresql(venda)

        except ValidationError as e:
            st.error(f"Erro na validado dos dados: {e}")
        
if __name__ == "__main__":
    main()
