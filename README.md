# Projeto Canvas 2D

Este é um editor gráfico vetorial 2D simples, implementado em Python utilizando a biblioteca PyOpenGL (GLUT). O projeto permite ao utilizador desenhar, selecionar e manipular formas geométricas básicas numa tela (canvas).

## Funcionalidades

* **Desenhar Formas:** Retângulos, círculos e polilinhas.
* **Seleção de Objetos:** Selecione um objetos na tela.
* **Manipulação de Objetos:**
    * **Transladar:** Mover o objetos selecionado.
    * **Escalar:** Aumentar ou diminuir o tamanho dos objetos.
    * **Rotacionar:** Girar o objetos selecionado.
* **Outras Ferramentas:**
    * **Deletar:** Apaguar objeto selecionado.
    * **Consultar:** Imprima a área e o perímetro do objeto selecionado no terminal.
    * **Mudar Cor:** Alterar a cor do objeto selecionado usando um seletor de cores RGB.
    * **Zoom:** Aproximar ou afastar a visualização da tela.

## Instalação

Para executar este projeto, é necessário as seguintes dependências:

* PyOpenGL
* PyOpenGL_accelerate
* Numpy

Pode instalar todas as dependências utilizando o arquivo `requirements.txt` fornecido:

```bash
pip install -r requirements.txt
```
---
## Como Usar
Para abrir o canvas, execute o arquivo main.py a partir da raiz do projeto:

```bash
python3 main.py
```

### Controles
A interação é feita principalmente através do teclado para selecionar ferramentas e do mouse para desenhar e manipular as geometrias

### Teclas Gerais

| Tecla | Ação |
| :--- | :--- |
| `r` | Ativa a ferramenta de Desenhar Retângulo |
| `c` | Ativa a ferramenta de Desenhar Círculo |
| `p` | Ativa a ferramenta de Desenhar Polilinha |
| `s` | Ativa a ferramenta de Seleção |
| `ESC` | Cancela o desenho atual, desmarca a seleção ou fecha o programa |
| `+` | Zoom In (Aproximar) |
| `-` | Zoom Out (Afastar) |

### Ferramenta de Desenho (Teclas `r`, `c`, `p`)

  * **Retângulo (`r`) e Círculo (`c`):**
    1.  Clique com o botão esquerdo e mantenha pressionado para definir o ponto inicial
    2.  Arraste o mouse até ao tamanho desejado
    3.  Solte o botão do mouse para finalizar a forma
  * **Polilinha (`p`):**
    1.  Clique com o botão esquerdo para adicionar um ponto
    2.  Mova o mouse e clique novamente para adicionar mais pontos
    3.  Faça um **clique duplo** para finalizar a polilinha

-----

### Ferramenta de Seleção (Tecla `s`)

  * **Selecionar Objetos:**
      * **Clique:** Seleciona o objeto sob o cursor 
      * **Clique (em área vazia):** Desmarca o objeto
  * **Mudar Cor:**
      * Com um objeto selecionado, clique e arraste os seletores de cor (RGB) que aparecem na tela para alterar a cor do objeto
  * **Transformar Objetos (com seleção ativa):**
      * **Modo Transladar (Tecla `t` - padrão):** Clique e arraste um objeto selecionado para movê-lo
      * **Modo Escalar (Tecla `e`):** Clique e arraste o objeto para alterar a sua escala
      * **Modo Rotacionar (Tecla `o`):** Clique e arraste o objeto (verticalmente) para o rotacionar
      * **Eliminar (Tecla `d`):** Remove permanentemente os objetos selecionados
      * **Consultar (Tecla `x`):** Imprime a área e o perímetro dos objetos selecionados no terminal

```
