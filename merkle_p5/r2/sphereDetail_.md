
#### Nome
### sphereDetail()

#### Exemplos

```pde
void draw() { 
  background(200); 
  stroke(255,50); 
  translate(50,50,0); 
  rotateX(mouseY*0.05); 
  rotateY(mouseX*0.05); 
  fill(mouseX*2,0,160); 
  sphereDetail(mouseX/4); 
  sphere(40); 
} 

```

#### Descrição
Controla o nível de detalhe utilizado para
renderizar uma espera ao ajustar o número de vértices
utilisado na respectiva malha. A resolução padrão
é 30, a qual cria uma definição de espefra
rasoavalmente detalhada com vértices a cada  360/30 = 12
graus. Caso se vá renderizar um grande número de esferas
por  quadro, recomenda-se que se reduza o nível de detalhe
através do uso desta função. O ajuste permanece
ativo ate que**sphereDetail()** seja chamada novamente  com umm novo parâmetod, e portanto, não precisa ser chamada antes de cada comando**sphere()**,
a não ser que se queira esferas com diferentes atributos; por
exemplo, quando se utiliza menores detalhes em esferas menores, ou
quando se distancia da câmara.

#### Sintaxe
```pde
sphereDetail(n);

```
Parâmetros
n
int: número de segmentos (mínimo de 3) utilizados por revolução de um  círculo.

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[sphere()](sphere_)
