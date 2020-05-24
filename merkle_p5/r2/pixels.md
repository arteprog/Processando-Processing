
#### Nome
### pixels[]

#### Exemplos
<img border="0" height="100" src="media/pixels.gif" width="100"/>

```pde
color pink = color(255, 102, 204); 
loadPixels(); 
for (int i=0; i<(width*height/2)-width/2; i++) { 
  pixels[i] = pink; 
} 
updatePixels(); 

```

#### Descrição
Array que contém os valores de todos os
pixels da janela de visualização.  Este array
é do tamanha da janela de visualização. Por
exemplo, se a imagem é 100x100, haverão 10000 valores, e
se a janela for 200x300, haverão 60000 valores. O valor de**index **define a posição de um valor neste array. Por exemplo, o comando**color b = pixels[230] ** atribuirá à variável**b **valor
igual ao valor daquela localização no array. Ante de
acessar  este aeeay, seus dados precisam ser carregados
através da função**loadPixels()**. Após o array ser modificado, a função**updatePixels()** precisa ser chamdada para atualizar as mudanças.

#### Sintaxe
```pde
pixels[index]

```
Parâmetros
index
int: não deve exceder o tamanho do array

#### Utilização

	
Web & Applicações

#### Relacionado
[loadPixels()](loadPixels_)[updatePixels()](updatePixels_)[get()](get_)[set()](set_)[PImage](PImage)
