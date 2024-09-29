import psycopg2
from psycopg2 import sql
from datacontract import Vendas
from dotenv import load_dotenv
import os
import streamlit as st

# carrega variaveis do arquivo .env
load_dotenv()

# config banco de dados postgresql
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def write_data_postgresql(data: Vendas):
    """
    Funcao para salvar no PostgreSQL.

    Args:
        host (string): Hostname do banco de dados
        database (string): Nome da database
        user (string): Usuario do banco de dados
        password (string): Senha do banco de dados
    """

    try:
        con = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

        cursor = con.cursor()

        # insert
        insert_query = sql.SQL(
            "INSET INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            data.email,
            data.data,
            data.valor,
            data.quantidade,
            data.produto
        ))

        # close
        con.commit()
        cursor.close()
        con.close()

        st.success("Dados gravado com sucesso no banco de dados!")

    except Exception as e:
        st.error(f"Erro ao gravar no banco de dados: {e}")

