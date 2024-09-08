![logo](docs/assets/banner.png)

> 📝 O material para acompanhamento do workshop está disponível [**neste link**](https://andrematte.github.io/workshop-opencv/).

# Sobre este Workshop
Este workshop explorará, na prática, as ferramentas básicas utilizadas em projetos de Visão Computacional. A compreensão dessas técnicas é crucial para construir uma base sólida em manipulação e processamento de imagens, facilitando a aplicação mais eficaz de algoritmos de Machine Learning em projetos futuros. 

Os conteúdos da aula prática foram implementados no formato de Jupyter Notebooks e estão armazenados no diretório `notebooks`. Já o Projeto Final será implementado em um script Python puro, localizado em `scripts/projetofinal.py`.

# Pré-requisitos
- Conhecimentos básicos de programação na linguagem Python
- Computador pessoal com Python 3.x instalado para a execução dos exercícios
- Ambiente Python configurado e com as seguintes bibliotecas instaladas:
    - NumPy
    - OpenCV
    - MatPlotLib
    - Jupyter (Opcional)

# Configuração do Ambiente

Esta seção contém instruções para a configuração do ambiente de desenvolvimento contendo as dependências necessárias para este workshop.

- NumPy
- OpenCV
- MatPlotLib
- Jupyter (Opcional)

O método recomendado para a configuração do ambiente utiliza o gerenciador de dependências `Poetry`, porém outras ferramentas, como `virtualenv` ou `conda` também podem ser utilizadas.

## Clonando o repositório

```sh
git clone https://github.com/andrematte/workshop-opencv
cd workshop-opencv
```

## Configuração utilizando Poetry

O comando `poetry install` irá criar um ambiente virtual contendo as dependências do projeto, listadas em `pyproject.toml`.

```sh
poetry install
```

## (Opcional) Executar Jupyter Lab

Os conteúdos da aula prática foram implementados no formato de Jupyter Notebooks. Qualquer IDE com suporte a Notebooks pode ser utilizada. Por simplicidade, recomenda-se o Jupyter Lab.

```sh
poetry shell
poetry jupyter lab
```