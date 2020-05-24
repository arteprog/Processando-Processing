
#### Nome
### saveFrame()

#### Exemplos

```pde
int x = 0; 
void draw() 
{ 
  background(204); 
  if(x < 100) { 
    line(x, 0, x, 100); 
    // Salva cada quadro como screen-0000.tif, screen-0001, etc. 
    saveFrame(); 
    x = x + 1; 
  } 
} 

```



```pde
int x = 0; 
void draw() 
{ 
  background(204); 
  if(x < 100) { 
    line(x, 0, x, 100); 
    // Salva cada quadro como line-0000.tif, line-0001, etc. 
    saveFrame("line-####.tif"); 
    x = x + 1; 
  } 
} 

```



#### Descrição
Salva uma seqüência numerada de imagens. Caso `saveFrame()`
é chamada sem parâmetros, ela nomeará os arquivos
como screen-0000.tif, screen-0001.tif, etc. IÉ possível
especificar o nome da seqüência de arquivos através
do parâmetro `filename, `e escolhr entre salvar arquivos to tipo TIFF ou TARGA através do parâmetro `ext. ` Estas
seqüências de imagems podems ser carregadas em programas
como o QuickTime da Apple na confecção de filmes. Estes
arquivos são
salvos na pasta de esboços, a qual pode ser aberta ao
selecionar "Show sketch folder" do  menu  Não
é possível utilizar a função `saveFrame()` quando o programa esta executando em um navegador web.

#### Sintaxe
```pde
saveFrame()
saveFrame("filename-####.ext")

```
Parâmetros
filename
String: qualquer seqüência de letras e números entre aspas


ext
um entre  "tif" ou "tga"



#### Retorno

	
Nenhum

#### Utilização

	
Application

#### Relacionado
[save()](save_
)

