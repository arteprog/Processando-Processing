## Material para conversão da referência do Processing em Português 

### [UTFPR, 2005 (Prof. Luiz Ernesto Merkle)](http://www.dainf.ct.utfpr.edu.br/~merkle/processing/reference/ptBR/index.html) --> [Wiki-tradução em Processando Processing](https://github.com/arteprog/Processando-Processing/wiki)

#### Roadmap

1. Identificar páginas 'deprecadas', coisas da v1.0 que não existem mais no Processing v3.0
   - comparando páginas existentes vs ENv3.0
2. Identificar páginas que estão faltando, coisas que tem na v3.0 e que precisam ser traduzidas
   - comparando páginas ENv3.0 vs existentes
3. Identificar páginas a revisar / revisadas da v1.0
4. Melhorar os índices
   - 3 colunas
   - indicar páginas deprecadas
   - indicar páginas que falta traduzir
   - indicar páginas a revisar/revisadas
   
#### dados
- `ptBR` arquivos baixados do site original
    - html
    - imagens
- `r1` html
- `r2` ~markdown~ .md movido pro repositório-wiki
 
#### `cleanup_scripts`
- scripts pra converter o HTML original simplificado (ptBR -> r1)
  - `modify_html_index_first_cleanup.py` 4 arquivos index__ 
  - `modify_html_files_first_cleanup.py` todos os outros
- scripts pra converter o HTML simplifcado em markdown (r1 -> r2)
  - `modify2md_indez.py`4 arquivos index__
  - `moidfy2md_files.py` todos os outros
