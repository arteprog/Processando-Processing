
#### Nome
### setup()

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
  comandos
}
            
```
Parâmetros
comandos
quaisquer comandos válidos

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[loop()](loop_)[size()](size_)
