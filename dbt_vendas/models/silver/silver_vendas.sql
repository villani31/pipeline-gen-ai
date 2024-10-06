{{ config(materialized="view") }}

with cleaned_data as (
    SELECT
        nome, 
        email,
        DATE(data) as data,
        valor,
        quantidade,
        produto
    FROM
        {{ ref("bronze_vendas") }}
    WHERE
        valor > 0
        AND valor < 10000
        -- AND data <= CURRENT_DATE
)

SELECT * FROM cleaned_data
