# ProjetoWebScraping

Este README oferece uma visão geral abrangente do projeto, detalhando sua arquitetura, estrutura de diretórios e fornecendo instruções para execução e uso dos comandos de Web Scraping e Pandas.

## Descrição do Projeto

Este projeto é uma solução em Python para monitoramento de preços de tênis de corrida masculino no Mercado Livre. Ele visa fornecer insights sobre estratégias de precificação por meio de uma pipeline ETL que coleta, transforma e carrega dados de produtos até a página 10 do site.

## Arquitetura

A arquitetura do projeto é baseada em uma pipeline ETL (Extração, Transformação e Carga) desenvolvida em Python:

- **Extração:** Utilizamos o [Scrapy](https://scrapy.org/) para realizar o Web Scraping e extrair os dados dos produtos.
- **Transformação:** Os dados extraídos são processados e transformados utilizando o [Pandas](https://pandas.pydata.org/) para análise e limpeza.
- **Carga:** Os dados transformados são armazenados em um banco de dados [SQLite3](https://www.sqlite.org/index.html) e carregados para visualização.
- **Dashboard:** Criamos um painel interativo com o [Streamlit](https://streamlit.io/) para exibir os dados e insights gerados.

## Estrutura de Diretórios

A estrutura de diretórios do projeto é a seguinte:



1- Para rodar o web scraping 

" Bash 
scrapy crawl mercadolivre -o ../../data/data.jsonl
"

2- Para rodar o pandas tem que escrever no terminal na pasta SRC

"bash
 python transformacao/main.py "
