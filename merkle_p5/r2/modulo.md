
#### Nome
### % (módulo ou resto)

#### Exemplos

```pde
int a = 20%100;         // Atribui 20  à a
int b = 20%100;         // Atribui 20 à b
float c = 75.0%100.0;   // Atribui 75.0 à c
float d = 275.0%100.0;  // Atribui 75.0 à d

```



```pde
float a = 0.0; 
void draw() { 
  background(204); 
  a = (a + 0.5)%width; 
  line(a, 0, a, height); 
} 

```



#### Descrição
Clacula o resto de uma divisão de um
número por outro.  É extremamente útil para
manter números dentro de um limite, como no caso de manter uma
forma na tela.

#### Sintaxe
```pde
value1%valor2
            
```
Parâmetros
valor1
int ou float


valor2
int ou float



#### Retorno

	
int ou float

#### Utilização

	
Web & Applicações

#### Relacionado
[/ (divisão)](divide
)

