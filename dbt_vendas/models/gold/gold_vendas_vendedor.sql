{{ config(materialized='view') }}

WITH vendas_vendedor AS (
    SELECT 
        nome AS vendedor, 
        DATE(data) AS data, 
        SUM(valor) AS total_valor, 
        SUM(quantidade) AS total_quantidade, 
        COUNT(*) AS total_vendas
    FROM 
        {{ ref('silver_vendas') }}
    WHERE 
        data >= CURRENT_DATE - INTERVAL '6 days'
    GROUP BY 
        nome, DATE(data)
)

SELECT 
    vendedor, 
    data, 
    total_valor, 
    total_quantidade, 
    total_vendas
FROM 
    vendas_vendedor
ORDER BY 
    data ASC, vendedor ASC
