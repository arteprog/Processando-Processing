
#### Nome
### lightFalloff()

#### Exemplos

```pde
Em breve... 
 

```

#### Descrição
Especifica o fator*falloff *(n.t.*fallof rate*; decaimento; o como a intensidade de uma fonte de luz diminiu em função da distância)
para luzes pontuais, luzes spot, e luz ambiente. Os parâmetros
são utilizados para determinar o decaimento
através da seguinte equação:

falloff = 1 / (CONSTANTE + d * LINEAR + (d*d) * QUADRATICO))

onde d = distância entre a posição da luz e a posição do vértice.

Como com a função**fill(), ** a função**lightFalloff()**
afeta apenas os elementos que forem criados após sua chamada no
código.  O valor  padrão equivale à**lightFalloff(1.0, 0.0, 0.0). **Pensar
a luz ambiente com decamimento pode exigir certos truques.
 É utilizada, por exemplo, quando se quer que uma
região de um cena seja iluminada por luz ambiente de uma cor e
outra região por outra. Para isto se utilizam a
posição e a taxa de falloff, ou decaimento.  Pode-se
concebê-la como uma luz pontual que não  se importa
com que direção uma superfície está
orientada.

#### Sintaxe
```pde
lightFalloff(constante, linear, quadratico)

```
Parâmetros
constante
int ou float: valor constante para determinação do decaimento
linear
int ou float: valor constante linear para determinação do decaimento
quadratico
int ou float: valor constante quadrático para determinação do decaimento

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[lights()](lights_)[ambientLight()](ambientLight_)[pointLight()](pointLight_)[spotLight()](spotLight_)[lightSpecular()](lightSpecular_)
