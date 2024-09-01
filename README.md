<<<<<<< HEAD
# DATATHON-FIAP
=======
DATATHON-PASSOS-MAGICOS
==============================

## Configuração do banco de dados

1. Subi um container MySQL:
```
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```
2. Executar o notebook 01-lss-carga-dados-banco.ipynb no diretorio notebooks







Organiza do projeto.
------------

    ├── LICENSE
    ├── Makefile           <- Makefile com comandos como `make data` ou `make train`
    ├── README.md          <- O README de nível superior para desenvolvedores que usam este projeto.
    ├── data
    │   ├── external       <- Dados de fontes de terceiros.
    │   ├── interim        <- Dados intermediários que foram transformados.
    │   ├── processed      <- Os conjuntos de dados finais e canônicos para modelagem.
    │   └── raw            <- O despejo de dados original e imutável.
    │
    ├── docs               <- Um projeto padrão do Sphinx; veja sphinx-doc.org para detalhes
    │
    ├── models             <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
    │
    ├── notebooks          <- Notebooks Jupyter. Convenção de nomenclatura é um número (para ordenação),
    │                         as iniciais do criador e uma descrição curta delimitada por `-`, por exemplo,
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    │
    ├── reports            <- Análises geradas como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos e figuras gerados para serem usados em relatórios.
    │
    ├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente de análise, por exemplo,
    │                         gerado com `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Torna o projeto instalável com pip (pip install -e .), para que o src possa ser importado
    ├── src                <- Código-fonte para uso neste projeto.
    │   ├── __init__.py    <- Torna `src` um módulo Python
    │   │
    │   ├── data           <- Scripts para baixar ou gerar dados
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para transformar dados brutos em características para modelagem
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para treinar modelos e depois usar modelos treinados para fazer
    │   │   │                 previsões
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para criar visualizações exploratórias e orientadas a resultados
    │       └── visualize.py
    │
    └── tox.ini            <- Arquivo tox com configurações para rodar tox; veja tox.readthedocs.io



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
>>>>>>> 5974036 (Primeiro commit - estrutura de projeto criada)



