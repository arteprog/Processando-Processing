import os
import re
from bs4 import BeautifulSoup

base = '/home/villares/Documentos/GitHub/Processando-Processing/merkle_p5'
folder = os.path.join(base, 'r1')   # data directory
folder_out = os.path.join(base, 'r2')
if not os.path.isdir(folder_out):
    os.mkdir(folder_out)
file_names = [f for f in os.listdir(folder)
         if f.endswith('.html') and not f.startswith('index')]

def print_c(c):
    sections = ('Nome', 'Relacionado', 'Utilização', 'Retorno', 'Sintaxe', 'Descrição', 'Exemplos')
    result = ''
    if c.name is None:
        c = str(c).rstrip()
        if c: result = "<<"+c+">>"
    elif c.name == 'td':
        if c.contents:
            conts = [str(cont).rstrip() for cont in c.contents]
            s = ''.join(conts).rstrip()
            if s in sections:
                result = str('\n#### {}\n'.format(s))
            elif s and s != '\xa0':
                ss = BeautifulSoup(s, "html.parser")
                if ss.contents and ss.contents[0].name == 'table':
                    result = print_c(ss)
                else:
                    result = '{}\n'.format(s)
    else:
        for child in c.contents:
            line = print_c(child)
            if line:
                result += line    
    return result # + '\n' if result else ''
        

def replace_tag(template, *args, **kwargs):
    for tag_instance in soup.find_all(*args, **kwargs):
            if tag_instance.string:
                tag_instance.replace_with(template.format(tag_instance.string))    
#                 if template == '*{}*': print(str(tag_instance))

for file_name in file_names[:]:   # file_names[:] todos!
    if 'index' in file_name: continue
    print(file_name)
    file_out = file_name.replace('.html', '.md')
    with open(os.path.join(folder, file_name)) as f,\
         open(os.path.join(folder_out, file_out), "w") as g:
        soup = BeautifulSoup(f, "html.parser")
        
        # simple cases
        for br in soup.find_all('br'):
            br.replace_with('\n') # maybe double?

        replace_tag('**{}**', 'b')
        replace_tag('*{}*', 'i')
        replace_tag('### {}\n\n', 'h3') # maybe double?
        replace_tag('{}', 'font')
        replace_tag('**{}**', name='span', style=re.compile("bold"))
        replace_tag('*{}*', name='span', style=re.compile("italic"))
 
        # special cases
        for a_tag in soup.find_all('a'):
            # ATENÇÃO: para a wiki vou tentar.
            href = a_tag['href'].replace('.html', '')  # para Wiki
            a_tag.replace_with('[{}]({})'.format(a_tag.text, href))
#             href = a_tag['href'].replace('.html', '.md')  # para GitHub Pages
#             a_tag.replace_with('[{}]({})'.format(a_tag.text, href))
        for pre in soup.find_all('pre'):
            pre_content = ''.join(map(str, pre.contents))
            pre_content = pre_content.replace('<br/>', '\n')
#             print(pre_content)
            pre.replace_with('```pde\n{}\n```'.format(pre_content))
            
        for img in soup.find_all('img'):
            if '1pix.gif'in img['src']:
                img.decompose()
            
        # these soups start with a table
        for cont in soup.contents:  
            if cont.name is not None:
                line = print_c(cont)
                if line:
                    pass
#                     print(line)
                    g.write(str(line))

