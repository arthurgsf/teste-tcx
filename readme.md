## Questão 1: Manipulação de Imagens em Python

A imagem utilizada nesta questão é a $images/test.jpg$.
Foi definida uma função $preprocessing$ que realizar as operações descritas na questão.
A imagem é lida e passada como input para a função definida.
Em seguida são exibidas duas janelas, contendo a imagem original e a pre-processada, respectivamente.
O programa aguarda até que alguma tecla seja apertada para fechar as janelas e se encerra.

## Questão 2: Detecção de Objetos com OpenCV
A imagem utilizada nesta questão é a $images/pcb.png$.
Foi imaginado um cenário de inspeção dos terminais de solda.
A imagem é lida e passa por um processo de *quantização de cores* através da clusterização (agrupamento) dos pixels, onde pixels similares e próximos, serão agrupados em uma mesma categoria, que será a sua nova cor.
Em seguida, a imagem quantizada passa pelo algoritmo Canny, que é um detector de bordas.
O resultado é então apresentado sobre uma cópia da imagem original em forma de bounding boxes.
As bounding boxes devem delimitar as áreas onde há pontos de solda.
O programa aguarda até que alguma tecla seja apertada para fechar as janelas e se encerra.

## Questão 3 (teórica) : Estruturas de Dados em OpenCV
>Explique as principais estruturas de dados utilizadas pelo OpenCV para representar
>imagens e vídeos. Destaque as diferenças entre essas estruturas, como por
>exemplo, quando e por que escolher usar uma matriz NumPy ou uma estrutura
>específica do OpenCV. Além disso, discuta a importância de compreender essas
>estruturas ao trabalhar com algoritmos de visão computacional.

- *cv::Mat*: é uma estrutura de dados otimizada para os algoritmos disponíveis na biblioteca opencv,
contendo lógicas próprias (internas) de acesso à dados e organização em memória, o que pode levar a melhor desempenho.

- *NumPy Array (np.ndarray)* : é uma estrutura de array de elementos altamente compatível com muitas bibliotecas disponíveis em python,
mas que não possui otimizações de acesso e gerenciamento de memória específicas para processamento de imagens.

- *Utilização* : Devemos utilizar np.array quando houver necessidade de garantir a compatibilidade e a interoperabilidade entre diferentes bibliotecas python, pois é uma estrutura de dados amplamente utilizada no ecossistema da linguagem. Já as matrizes opencv (cv::Mat) podem ser
utilizadas para extrair maior performance do algoritmo em casos onde esta é indispensável e mais importante que a compatibilidade com outras bibliotecas.

## Questão 4 (teórica) : Transformações Geométricas em OpenCV
>Descreva as transformações geométricas disponíveis no OpenCV e forneça
>exemplos práticos de situações em que cada uma delas seria aplicada. Aborde
>conceitos como translação, rotação, redimensionamento e perspectiva. Além disso,
>explique como as matrizes de transformação são utilizadas para representar essas
>operações e como aplicá-las em imagens.


- *Translação* : desloca a imagem ao longo do eixo x ou y. Pode ser aplicada em um contexto onde a imagem precisa ser alinhada em relação a outra, mas encontra-se deslocada no eixo x ou y.

- *Rotação* : Gira a imagem em torno de um ponto. Pode ser utilizada para corrigir a orientação de uma captura, por exemplo.

- *Resize* : Diminui ou aumenta o tamanho da imagem. É aplicada em contextos onde é necessária uma imagem de tamanho específico, ou mesmo diminuir a resolução da imagem para obter um processamento mais rápido (já que serão processados menos pixels).

- *Perspectiva* : Altera a imagem de maneira que parece ter sido capturada de um ângulo diferente. Utilizada em registro de imagems, para corrigir distorções de perspectiva em relação a uma imagem de referência, por exemplo.