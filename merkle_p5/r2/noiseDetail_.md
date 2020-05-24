<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### noiseDetail()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
float noiseVal; 
float noiseScale=0.02; 
void draw() { 
  for(int y=0; y<height; y++) { 
    for(int x=0; x<width/2; x++) { 
      noiseDetail(3,0.5); 
      noiseVal=noise( 
        (mouseX+x)*noiseScale, 
        (mouseY+y)*noiseScale 
      ); 
      stroke(noiseVal*255); 
      point(x,y); 
      noiseDetail(8,0.65); 
      noiseVal=noise( 
        (mouseX+x+width/2)*noiseScale, 
        (mouseY+y)*noiseScale 
      ); 
      stroke(noiseVal*255); 
      point(x+width/2,y); 
    } 
  } 
} 

```

#### Descrição
Ajusta o caráter e o nível de detalhe
produzido pela função de ruído de Perlin. De modo
similar a harmônicas em física, o ruído de
Perlin é computado sobre várias oitavas. Oitavas mais
baixas contribuem  mais para o sinal de saida, e como tal definem
a intensidade predominante do ruído, enquanto que oitavas mais
altas criam detalhes mais finos na seqüência de
ruído.  Como padrão, a função noise()
computa sobre 4 oitavas, onde cada uma contribui para exatamente a
metade de sua predecessora, e iniciando em 50% de intensidade para a
primeira oitava.  A declinação (*fallof amount*)
pode ser alterado ao se adicionar um par6ametro adicional à
função.  Por exemplo,  uma
declinação de 0.75 significa que cada oitava terá
75% de impacto (25% a menos) que a próxima menor oitava.
Qualquer valor entre 0.0 e 1.0 é válido.
 Entretanto, notar que valores acima de 0.5 podem resultar em
valores acima de 1.0 retornados por**noise()**.
Ao alterar estes parâmetros, o sinal criado pela função**noise()** pode ser adaptado para se adequar a necessidades e características bem específicas.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
noiseDetail(<font color="#996600">oitavas</font>)
noiseDetail(<font color="#996600">oitavas</font>, <font color="#996600">declinação</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
oitavas
int: número de oitavas a ser utilizada pela função **noise()**.
declinação
float: declinação (n.t. *falloff factor*) para cada oitava
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noise()](noise_)
