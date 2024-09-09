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

O uso do Poetry para criação do ambiente virtual isolado e instalação das dependências é recomendado, porém é possível instalar tudo com `pip install opencv-python matplotlib` ou `conda install opencv-python matplotlib`.

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

<div class="grid cards" markdown>
- :arrow_right:  Com o ambiente devidamente configurado, podemos partir para a primeira seção: [**Introdução ao OpenCV**](Conteúdo-do-Workshop/1-Introdução-ao-OpenCV.md).
</div>