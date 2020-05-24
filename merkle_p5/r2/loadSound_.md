
#### Nome
### loadSound()

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
Carrega um som em uma variável to tipo `PSound. ` Somente
arquivos do tipo .wave podem ser carregados. Para carregar
corretamente, os arquivos de audio devem estar localizados no
diretório data do esboço corrente.

#### Sintaxe
```pde
loadSound(filename)

```
Parâmetros
filename
String: nome do arquivo a carregar; deve ser to tipo .wav.



#### Retorno

	
PSound

#### Utilização

	
Web & Applicações

#### Relacionado
[PSound](PSound
)

