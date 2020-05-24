
#### Nome
### cos()

#### Exemplos
<img border="0" height="100" src="media/cos_.gif" width="100"/>

```pde
float a = 0.0; 
float inc = TWO_PI/25.0; 
for(int i=0; i<25; i++) { 
  line(i*4, 50, i*4, 50+cos(a)*40.0); 
  a = a + inc; 
} 

```

#### Descrição
Calcula o coseno de um ângulo. Esta função espera que os valores do parâmetro `angulo` correspondam a valores em radianos (valores entre 0 e 2*PI). Valores são retornados no intervalo entre -1.0 e 1.0.

#### Sintaxe
```pde
cos(angulo)

```
Parâmetros
angulo
float: um ângulo em radianos<description>



</description>

#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[sin()](sin_
)
[tan()](tan_
)

