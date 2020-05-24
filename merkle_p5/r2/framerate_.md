
#### Nome
### framerate()

#### Exemplos

```pde
void setup() { 
  framerate(4); 
} 
int pos = 0; 
void draw() { 
  background(204); 
  pos++; 
  line(pos, 20, pos, 80); 
  if(pos > width) { 
    pos = 0; 
  } 
} 

```

#### Descrição
Especifica o número de quadros a ser visualizado por segundo. Isto é feito através de chamadas a**delay() **ao final de**draw()**,
de modo a tornar mais lenta a visualização. Se o
processador não for rápido o suficiente para manter uma
taxa de visualização específica, a taxa
especificada não será alcançada. Por exemplo, a
chamada a função**framerate(30) **tentará reatualizar  a tela 30 vezes por segundo. É recomendado configurar*framerate*  em**setup().**

#### Sintaxe
```pde
framerate(fps)

```
Parâmetros
fps
int: number of frames per second

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[delay()](delay_)
