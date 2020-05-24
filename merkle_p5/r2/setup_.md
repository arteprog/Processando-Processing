<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### setup()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  size(200, 200); 
  background(0); 
  noStroke(); 
  fill(102); 
} 
 
int a = 0; 
 
void draw() { 
  rect(a++%width, 10, 2, 80); 
} 

```

#### Descrição
Chamada quando um programa inicia sua
execução. É utilizada para definir as propriedades
iniciais do ambiente, como tamanho da tela de
visualização, cor de fundo, imagens a carregar, e outras,
ande que**draw() **comece a ser executada.  Variáveis declaradas no escopo de**setup() **nao podem ser acessadas do corpo de outras funções, incluindo**draw(). **É permitido apenas uma função**setup() **para cada programa, e esta não deve ser chamada novamente após o início de sua execução.

#### Sintaxe
```pde
void setup() {
  <font color="#996600">comandos</font>
}
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
comandos
quaisquer comandos válidos
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loop()](loop_)[size()](size_)
