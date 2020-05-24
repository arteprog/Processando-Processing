<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loadSound()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
PSound soundA; 
 
void setup() { 
  soundA = loadSound("clong.wav"); 
  soundA.loop(); 
} 
 
void draw() { 
  // Uma draw() vazia é necessária para permitir que o som seja tocado.
} 

```

#### Descrição
Carrega um som em uma variável to tipo**PSound. ** Somente
arquivos do tipo .wave podem ser carregados. Para carregar
corretamente, os arquivos de audio devem estar localizados no
diretório data do esboço corrente.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loadSound(<font color="#996600">filename</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
filename
String: nome do arquivo a carregar; deve ser to tipo .wav.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
PSound
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[PSound](PSound)
