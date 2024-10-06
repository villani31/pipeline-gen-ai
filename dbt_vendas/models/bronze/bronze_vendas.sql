{{ config(materialized="view")}}

SELECT 
    *
FROM
    {{ source("dw_vendas_source", "vendas") }}