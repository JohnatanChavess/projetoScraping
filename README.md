# ProjetoWebScraping

Este README oferece uma visão geral abrangente do projeto, detalhando sua arquitetura, estrutura de diretórios e fornecendo instruções para execução e uso dos comandos de Web Scraping e Pandas.

## Descrição do Projeto

Este projeto é uma solução em Python para monitoramento de preços de tênis de corrida masculino no Mercado Livre. Ele visa fornecer insights sobre estratégias de precificação por meio de uma pipeline ETL que coleta, transforma e carrega dados de produtos até a página 10 do site.

## Arquitetura

A arquitetura do projeto é baseada em uma pipeline ETL (Extração, Transformação e Carga) desenvolvida em Python:

- **Extração:** Utilizei o [Scrapy](https://scrapy.org/) para realizar o Web Scraping e extrair os dados dos produtos.
- **Transformação:** Os dados extraídos são processados e transformados utilizando o [Pandas](https://pandas.pydata.org/) para análise e limpeza.
- **Carga:** Os dados transformados são armazenados em um banco de dados [SQLite3](https://www.sqlite.org/index.html) e carregados para visualização.
- **Dashboard:** Criei um painel interativo com o [Streamlit](https://streamlit.io/) para exibir os dados e insights gerados.

## Estrutura de Diretórios

A estrutura de diretórios do projeto é a seguinte:

- `projetoScraping/`
  - `src/`
    - `coleta/`
      - `spiders/`
        - `mercadolivre.py`
      - `settings.py`
    - `transformacao/`
      - `main.py`
  - `data/`
    - `data.jsonl`
  - `notebooks/`
    - `exploracao_dados.ipynb`
  - `.gitignore`
  - `README.md`
  - `requirements.txt`



## Como Usar

### 1. Rodar o Web Scraping

Para iniciar o processo de coleta de dados com o Scrapy, utilize o seguinte comando Bash:

scrapy crawl mercadolivre -o ../../data/data.jsonl

Este comando executa o spider do Scrapy e salva os dados extraídos no arquivo data.jsonl localizado na pasta data que está um nível acima da pasta atual.

### 2. Rodar o Pandas

Para processar e transformar os dados coletados, execute o script Python que realiza as operações necessárias com Pandas. Certifique-se de estar no diretório `src` antes de executar o comando:

cd src
python transformacao/main.py

### 3. Visualizar o Dashboard

Para visualizar o dashboard, utilize o Streamlit. Certifique-se de estar no diretório onde o script `app.py` está localizado e execute o comando:

cd src/dashboard
streamlit run app.py



