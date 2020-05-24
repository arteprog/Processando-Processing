
#### Nome
### perspective()

#### Exemplos
<img border="0" height="100" src="media/perspective_.gif" width="100"/>

```pde
// Recria a perspectiva padrão
size(100, 100, P3D); 
noFill(); 
float fov = PI/3.0; 
float cameraZ = (height/2.0) / tan(PI * fov / 360.0); 
perspective(fov, float(width)/float(height), 
            cameraZ/10.0, cameraZ*10.0); 
translate(50, 50, 0); 
rotateX(-PI/6); 
rotateY(PI/3); 
box(45); 

```

#### Descrição
Configura a perspecitva padrão ao aplicar encurtamento (n.t. *foreshortening*),
o que faz com que objetos mais distantes aparecem menores que os mais
próximos, Os parâmetros definem um volume de
visualização com a forma de pirâmide truncada.
Objetos próximos a câmera aparecem em seu tamanho real,
enquanto que objetos mais distantes aparecem menores.  Esta
projeção simula a perspectiva do mundo de mod mais
acurado que a perspectiva ortográfica. Sua versão sem
parâmetros configura a perspectiva padrão, e sua
versão com quatro parâmetros especifica a área
precisamente. Os valores padrão equivalem à perspective(PI/3.0, width/height, cameraZ/10.0, cameraZ*10.0) onde cameraZ é ((height/2.0) / tan(PI*60.0/360.0));

#### Sintaxe
```pde
perspective()
perspective(fov, aspecto, zProx, zDist)

```
Parâmetros
fov
float: ângulo do campo de visão  (em radianos) da direção vertical


aspecto
float: taxa entre largura e altura


zProx
float: posição z do plano de recorte mais próximo


zDist
float: posição z do plano de recorte mais distante



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações
