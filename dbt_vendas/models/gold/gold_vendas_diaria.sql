{{ config(materialized='view') }}

WITH vendas_diaria AS (
    SELECT 
        nome AS vendedor,
        data, 
        produto, 
        SUM(valor) AS total_valor, 
        SUM(quantidade) AS total_quantidade, 
        COUNT(*) AS total_vendas
    FROM 
        {{ ref('silver_vendas') }}
    WHERE 
        to_char(data, 'YYYY-MM-DD') = to_char(current_date, 'YYYY-MM-DD')
    GROUP BY 
        nome, data, produto
)

SELECT 
    vendedor,
    data, 
    produto, 
    total_valor, 
    total_quantidade, 
    total_vendas
FROM 
    vendas_diaria
ORDER BY 
    data ASC
    