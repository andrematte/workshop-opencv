<div class="grid cards" markdown>
- :ledger: Para acompanhar esta seção, abra o arquivo `notebooks/5-limiarizacao.ipynb`.
</div>

Limiarização é uma técnica fundamental no processamento de imagens utilizada para separar objetos de interesse em uma imagem, com base nos valores de intensidade dos pixels.

Na limiarização, um valor de limiar (threshold) é definido, e cada pixel da imagem é comparado com esse valor. Se o valor do pixel for maior ou igual ao limiar, ele é alterado para um valor máximo (geralmente 255, branco); caso contrário, é alterado para 0 (preto).

Vamos testar as funções de limiarização com o arquivo `media/gradient.jpg`.

---
## Importando as bibliotecas necessárias

Vamos iniciar importando as bibliotecas necessárias para esta seção: `numpy`, `cv2` e `matplotlib.pyplot`.

```python
# Importe as bibliotecas necessarias:
import numpy as np
import cv2
import matplotlib.pyplot as plt
```

---
## Limiarização Simples

Vamos testar as técnicas de limiarização na imagem `media/gradient.jpg`.

```python
# Carregue a imagem 'media/gradient.jpg'
gradiente = cv2.imread("media/gradient.jpg", 0)

# Exiba a imagem
plt.imshow(gradiente, cmap="gray")
```

Aplique a limiarização simples com a função `cv2.threshold()`

```python
# Selecione o valor do Limiar
limiar = 127

# Realize a Limiarização
_, binarizada = cv2.threshold(gradiente, limiar, 255, cv2.THRESH_BINARY)

# Exiba a imagem
plt.imshow(binarizada, cmap="gray")
```

---
## Limiarização Inversa

```python
# Selecione o valor do Limiar
limiar = 127

# Realize a Limiarização Inversa
_, binarizada = cv2.threshold(gradiente, limiar, 255, cv2.THRESH_BINARY_INV)

# Exiba a imagem
plt.imshow(binarizada, cmap="gray")
```

---
## Testando diferentes limiares

Vamos testar diferentes valores de limiar na imagem de exemplo.

```python
# Carregue o arquivo `media/gatogordo.jpg` em escala de cinza
imagem = cv2.imread("media/gatogordo.jpg", 0)

# Exibir a imagem
plt.imshow(imagem, cmap="gray")
```

Aplique diferentes valores de limiar:

```python
# Testar diferentes valores de limiar
limiar = 115

# Testar diferentes tipos de limiarização
_, binarizada = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)

# Exibir a imagem
plt.imshow(binarizada, cmap="gray")
```

## Limiarização Automática Otsu

Existem métodos para detecção automática do limiar que melhor separa os grupos de pixels da imagem. Um desses métodos é o `cv2.THRESH_OTSU`.

```python
# Aplique a operação de thresholding usando a
# combinação de `cv2.THRESH_BINARY` e `cv2.THRESH_OTSU`
otsu_valor, otsu_thresh = cv2.threshold(
    imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Exiba a imagem
plt.imshow(otsu_thresh, cmap="gray")
```

Ao somar as duas flags, você está dizendo ao OpenCV que quer usar a binarização binária `cv2.THRESH_BINARY`, com o valor de limiar calculado automaticamente pelo método de Otsu `cv2.THRESH_OTSU`.

---
## Limizarização + Detecção de Contornos

<div class="grid cards" markdown>
- :archery:  **Mini Projeto:** elaborar uma metodologia de visão computacional para realizar a contagem de moedas na imagem `media/moedas.jpg`.
</div>

Passo-a-passo:

1. Suavizar a imagem para reduzir ruídos
2. Aplicar limiarização para extrair a máscara de segmentação
3. Detectar os contornos
4. Desenhar caixas delimitadora nos objetos detectados

```python
# Carregue o arquivo `media/moedas.jpg` em RGB
imagem = cv2.cvtColor(cv2.imread("media/moedas.jpg"), cv2.COLOR_BGR2RGB)

# Exiba a imagem
plt.imshow(imagem, cmap="gray")
```

### Passo 1: Suavizar a imagem

Vamos converter a imagem para escala de cinza e aplicar filtros de suavização (Blur) para reduzir ruídos.

```python
# Converta para escala de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

# Aplique um filtro de suavização Gaussiano
suavizada = cv2.GaussianBlur(cinza, (15, 15), 0)

# Exiba a Imagem
plt.imshow(suavizada, cmap="gray")
```

### Passo 2: Calcular o Limiar

```python
# Escolha o limiar
limiar = 250

# Aplique Limiarização Inversa
valor, thresh = cv2.threshold(suavizada, limiar, 255, cv2.THRESH_BINARY_INV)

# Exiba a imagem
plt.imshow(thresh)
```

### Passo 3: Detectar Contornos

A função cv2.findContours() no OpenCV é usada para detectar os contornos dos objetos em uma imagem binária. Os contornos são, essencialmente, curvas que conectam pontos contínuos de intensidade similar (como os limites de objetos), sendo muito útil em tarefas de segmentação de objetos, detecção de formas e análise de bordas.

Parâmetros: 

- `image`: A imagem binária onde os contornos serão detectados. Geralmente, é o resultado de uma limiarização (como cv2.threshold()) ou da aplicação de um detector de bordas (como o Canny).
- `mode`: Define como os contornos serão recuperados (explicado abaixo).
- `method`: Define como os pontos dos contornos serão armazenados (explicado abaixo).
- `contours`: É uma lista de contornos detectados, onde cada contorno é um array de coordenadas de pontos (x, y).
- `hierarchy`: Uma matriz que contém informações sobre a relação entre os contornos (por exemplo, se um contorno está dentro de outro).

#### Modos de Recuperação de Contornos:

- `cv2.RETR_EXTERNAL`:
    - Retorna apenas os contornos mais externos. Este modo ignora quaisquer contornos internos, sendo útil quando você só está interessado no objeto principal.
    - Exemplo: Se você tem moedas dentro de uma caixa, ele detectaria apenas a borda da caixa.
- `cv2.RETR_LIST`:
    - Retorna todos os contornos detectados, sem organizar a hierarquia. Não estabelece nenhuma relação de aninhamento entre os contornos.
- `cv2.RETR_CCOMP`:
    - Organiza todos os contornos em uma hierarquia de dois níveis: contornos externos e os contornos dos buracos (objetos internos) detectados.
- `cv2.RETR_TREE`:
    - Recupera todos os contornos e constrói uma hierarquia completa, o que significa que ele armazena as relações de aninhamento entre os contornos (pai-filho, irmão, etc.).

#### Métodos de Aproximação de Contornos

- `cv2.CHAIN_APPROX_NONE`:
	- Armazena todos os pontos do contorno, sem compressão. Se você quer manter todos os pontos ao longo do contorno, use esta opção.
- `cv2.CHAIN_APPROX_SIMPLE`:
	- Comprime segmentos horizontais, verticais e diagonais, mantendo apenas os pontos finais desses segmentos. Isso reduz o número de pontos necessários para representar o contorno, o que economiza memória.

**Vamos detectar os contornos usando o modo `cv2.RETR_EXTERNAL` e o método `cv2.CHAIN_APPROX_SIMPLE`.**

```python
# Detecte os contornos
contornos, _ = cv2.findContours(
    image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE
)

# Verifique quantos contornos foram encontrados
len(contornos)
```

Agora podemos desenhar os contornos dos objetos detectados:

```python
# Faça uma cópia da imagem para desenhar os contornos
imagem_contornos = imagem.copy()

# Desenhe os contornos na imagem
cv2.drawContours(imagem_contornos, contornos, -1, (255, 0, 0), 5)

# Escreva na imagem o número de moedas encontradas
texto = f"Contagem de Moedas: {len(contornos)}"
cv2.putText(
    imagem_contornos,
    texto,
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 0, 0),
    2,
)

# Exiba a imagem
plt.imshow(imagem_contornos)
```

### Passo 4: Desenhando Caixas Delimitadoras

A função cv2.boundingRect(contorno) calcula o retângulo que encapsula o contorno especificado.

```python
# Faça uma cópia da imagem para desenhar as bounding boxes
imagem_bbox = imagem.copy()

# Itere sobre os contornos para inserí-los na imagem
for contorno in contornos:
    (x, y, w, h) = cv2.boundingRect(contorno)
    cv2.rectangle(imagem_bbox, (x, y), (x + w, y + h), (0, 255, 0), 5)

# Exiba a imagem
plt.imshow(imagem_bbox)
```



<div class="grid cards" markdown>
- :arrow_right:  Continua na próxima seção: [**Projeto Final**](../Projeto-Final.md).
</div>