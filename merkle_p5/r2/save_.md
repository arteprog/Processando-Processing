
#### Nome
### save()

#### Exemplos

```pde
line(20, 20, 80, 80); 
// Salva um arquivo TIFF chamado "diagonal.tif" 
save("diagonal.tif"); 
// Salva um arquivo TARGA chamado "cross.tga" 
line(80, 20, 20, 80); 
save("cross.tga"); 

```



#### Descrição
Faz uma imagem da janela de
visualização. Imagens são salvas no formato TIFF
ou TARGA dependendo da extensão do parâmetro `filename`. Se nenhuma estensão é incluída em filename, a imagem será salva com TIFF, e `.tif`  será adicionada ao nome. Este arquivo é
salvo na pasta de esboços, a qual pode ser aberta ao
selecionar "Show sketch folder" do  menu  "Sketch". Não
é possível utilizar a função `save()` quando o programa esta executando em um navegador web.

#### Sintaxe
```pde
save(filename)

```
Parâmetros
filename
String: qualquer seqüência de letras e números entre aspas



#### Retorno

	
Nenhum

#### Utilização

	
Application

#### Relacionado
[saveFrame()](saveFrame_
)

