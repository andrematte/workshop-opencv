<div class="grid cards" markdown>
- :ledger: Para acompanhar esta seção, abra o arquivo `notebooks/1-introducao.ipynb`.
</div>

O **Open** Source **C**omputer **V**ision Library (OpenCV) é uma biblioteca de código aberto que implementa funções de processamento de imagem, muito utilizadas em projetos de **Visão Computacional**.

![opencv-logo](https://miro.medium.com/v2/resize:fit:1400/0*uN4f5hAwHzHLUagL){ .center}

- Originalmente desenvolvido pela Intel em 1999
- Escrito primariamente na linguagem **C++**, porém também oferece *bindings* para **Python**, **Java** e **Matlab/Octave**

> A documentação do OpenCV está disponível [**neste link**](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html).

Nesta primeira seção do workshop iremos aprender as funções básicas de carregamento de imagens com OpenCV:

1. Representação matricial de imagens digitais
2. Leitura, exibição e armazenamento de imagens
3. Trabalhando com arquivos de vídeo
4. Trabalhando com o *feed* de uma câmera externa

---
## Representação Matricial de Imagens Digitais

A **representação de imagens digitais** no **OpenCV** e **NumPy** é feita por meio de arrays multidimensionais, ou tensores, implementados pela biblioteca **NumPy**. Cada imagem é composta por uma matriz de números, onde cada valor corresponde à intensidade de um pixel.

- A intensidade do pixel varia, por padrão, entre 0 e 255.

### Estrutura da Imagem
Em OpenCV e NumPy, as imagens são representadas por um **array NumPy** de 2 ou 3 dimensões:

- **Imagem em Escala de Cinza**: É representada por uma matriz 2D, onde cada elemento contém um valor de intensidade que vai de **0** (preto) a **255** (branco).

- **Imagem Colorida (RGB)**: É representada por uma matriz 3D com 3 canais (para as cores vermelho, verde e azul).

Em OpenCV, a ordem dos canais padrão é **BGR** (ao contrário do usual RGB). Aqui, cada pixel é um vetor de 3 valores representando as intensidades dos canais **B** (azul), **G** (verde) e **R** (vermelho).

---
## Importando as Bibliotecas Necessárias

Vamos iniciar importando as bibliotecas necessárias para esta seção: `numpy`, `cv2` e `matplotlib.pyplot`.

```python
# Importe as bibliotecas aqui
import cv2  
import numpy as np 
import matplotlib.pyplot as plt 
```

---
## Leitura, Exibição e Armazenamento de Imagens

Vamos carregar a imagem de exemplo `/media/gatogordo.jpg`.

> A função cv2.imread() permite a importação de um arquivo de imagem, retornando um tensor NumPy. As *flags* opcionais podem ser utilizadas. As principais *flags* são:

>- 0: leitura em escala de cinza
>- 1: leitura em BGR
>- -1: leitura no formato original

### Escala de Cinza

```python
# Leia a imagem em escala de cinza e armazene-a em uma variável
imagem_cinza = cv2.imread("media/gatogordo.jpg", 0)
```

Utilize comandos do NumPy para verificar o conteúdo do tensor, o formato do tensor `imagem.shape` e os valores mínimos e máximos das intensidades dos pixels `imagem.min()` e `imagem.max()`. 

Podemos também exibir a imagem para verificar seu conteúdo. O OpenCV conta com a função `cv2.imshow()`, que abre a imagem em uma janela, porém esta função não funciona em Notebooks. Para visualizar a imagem Notebooks, vamos utilizar a função `plt.imshow()` do Matplotlib.

```python
# Plote a imagem com o mapa de cores "gray".
plt.imshow(imagem_cinza, cmap="gray")
```

### Imagem Colorida

Vamos repetir o processo para a imagem colorida (BGR).

```python
# Carregue a imagem colorida (flag 1)
imagem_colorida = cv2.imread("media/gatogordo.jpg", 1)

# Plote a imagem com Matplotlib
plt.imshow(imagem_colorida)
```

> No OpenCV, a ordem das cores é BGR (azul, verde, vermelho), enquanto no Matplotlib a ordem é RGB (vermelho, verde, azul). Portanto, ao exibir imagens carregadas com OpenCV usando Matplotlib, é comum precisar converter a ordem das cores de BGR para RGB.

Podemos converter o espaço de cores de BGR para RGB simplesmente reordenando os canais da imagem.

```python
# Extraia cada banda e armazene-as em variáveis
BLUE = imagem_colorida[:,:,0]
GREEN = imagem_colorida[:,:,1]
RED = imagem_colorida[:,:,2]
```

Cada pixel das três bandas extraídas representa a intensidade de cada cor (azul, verde, vermelho) na imagem.

```python
# Plotar cada banda separadamente com Matplotlib
plt.figure(figsize=(15, 10))
plt.subplot(1, 3, 1)
plt.imshow(RED, cmap="Reds")
plt.subplot(1, 3, 2)
plt.imshow(GREEN, cmap="Greens")
plt.subplot(1, 3, 3)
plt.imshow(GREEN, cmap="Blues")
```

Vamos reordenar as bandas para criar uma imagem RGB.

> A função np.stack() do NumPy permite empilhar matrizes em qualquer dimensão, vamos empilhar as bandas na dimensão 2.

```python
# Montar uma imagem RGB a partir dos canais separados
imagem_rgb = np.stack([RED, GREEN, BLUE], axis=2)
plt.imshow(imagem_rgb)
```

Agora a imagem é mostrada corretamente pelo MatPlotLib!

Vamos salvar a imagem em um arquivo com a função `cv2.imwrite()`.

```python
# Salve a imagem no disco
cv2.imwrite("media/gatogordo_corrigido.jpg")
```

---
## Trabalhando com Arquivos de Vídeo

**Um arquivo de vídeo consiste em uma sequência de imagens**. A função `cv2.VideoCapture` é capaz de ler e iterar sobre um frame de cada vez. Portanto, todas as funcionalidades utilizadas a imagens podem ser aplicadas aos frames de vídeo.

Vamos criar um objeto de captura de vídeo:

```python
# Crie um objeto de captura de vídeo
capture = cv2.VideoCapture("media/gatoburro.mp4")
```

A função `capture.get()` pode ser utilizada com um conjunto de *flags* para capturar informações sobre o arquivo de vídeo.

- `capture.get(cv2.CAP_PROP_FPS)`: retorna a quantidade de frames por segundo (FPS)
- `capture.get(cv2.CAP_PROP_FRAME_COUNT)`: retorna o número total de frames do vídeo
- `capture.get(cv2.CAP_PROP_FRAME_WIDTH)`: retorna a largura do vídeo
- `capture.get(cv2.CAP_PROP_FRAME_HEIGHT)`: retorna a altura do vídeo

A função `capture.read()` itera sobre os frames do vídeo, retornando o próximo frame. Vamos ler os frames do vídeo e plotá-los com Matplotlib:

```python
# Leia o próximo frame do vídeo
ret, frame = capture.read()

# Converta para RGB
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Exiba com matplotlib
plt.imshow(rgb_frame)
```

---
## Trabalhando com o *Feed* de uma Câmera Externa

Muitas vezes precisamos trabalhar com transmissões de vídeo vindas de dispositivos externos, como webcams ou câmeras IP.

No OpenCV, a função `cv2.VideoCapture` também é capaz de receber o *feed* de vídeo de webcams, por exemplo. Basta trocar o caminho do arquivo de vídeo pelo id da webcam.

```python
# Leia o feed de webcam (a webcam padrão tem id=0)
cv2.VideoCapture(0)
```

<div class="grid cards" markdown>
- :arrow_right:  Continua na próxima seção: [**Operações básicas**](2-Operações-Básicas.md).
</div>