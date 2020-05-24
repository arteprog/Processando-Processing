
#### Nome
### fill()

#### Exemplos
<img border="0" height="100" src="media/fill_.gif" width="100"/>

```pde
fill(153); 
rect(30, 20, 55, 55); 

```
<img border="0" height="100" src="media/fill_2.gif" width="100"/>

```pde
fill(204, 102, 0); 
rect(30, 20, 55, 55); 

```

#### Descrição
Atribui cor para ser usada no preenchimento de formas. Por exemplo, ao chamar `fill(204,102,0) ` e
desenhar um ret6angulo, este e todas as fomras subsequentes,
serão preenchidas com um tom de laranja. Esta cor pode ser
especificada nos termos dos modelos RGB ou HSB, dependendo do modo
corrente especificado através de `colorMode() `( o espaço de cor padrão é o RGB, como cada valor variando de 0 a 255).<span style="font-style: italic;">Nota: o valor do parâmetro "cinza"deve ser menor ou igual ao máximo valor corrente especificado por  `colorMode()` . O valor padrão máximo é 255. </span><i></i>

#### Sintaxe
```pde
fill(cinza)
fill(cinza, alpha)
fill(cor)
fill(valor1, valor2, valor3)
fill(valor1, valor2, valor3, alpha)

```
Parâmetros
cinza
int ou float: número que especifica valor entre preto e branco


alpha
int ou float: opacidade do preenchimento


cor
color: qualquer valor do tipo de dados color


valor1
int ou float: valor de vermelho ou de matiz  (dependendo do atual modo de cor)


valor2
int ou float: valor de verde ou de saturação  (dependendo do atual modo de cor)


valor3
int ou float: valor de azul o de brilho  (dependendo do atual modo de cor)



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[noFill()](noFill_
)
[colorMode()](colorMode_
)

