import os
import re
from bs4 import BeautifulSoup

folder = '/home/villares/Documentos/merkle_p5/r1'   # your directory
file_names = [f for f in os.listdir(folder)
         if f.endswith('.html')]

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
        

for file_name in file_names[:]:   # file_names[:] todos!
    if 'index' not in file_name: continue
    print(file_name)
    file_out = file_name.replace('.html', '.md')
    with open(os.path.join(folder, file_name)) as f,\
         open(os.path.join(folder[:-3] + "/r2", file_out), "w") as g:
        soup = BeautifulSoup(f, "html.parser")
        for b_span in soup.find_all(name='span', style=re.compile("bold")):
            if b_span.string:
                b_span.replace_with('**{}**'.format(b_span.string))
        for b_tag in soup.find_all('b'):
            if b_tag.string:
                b_tag.replace_with('**{}**'.format(b_tag.string))
        for i_span in soup.find_all(name='span', style=re.compile("italic")):
            if i_span.string:#<span style="font-weight: bold;">
                i_span.replace_with('*{}*'.format(i_span.string))
        for i_tag in soup.find_all('i'):
            if i_tag.string:
                i_tag.replace_with('*{}*'.format(i_tag.string))
        for a_tag in soup.find_all('a'):
            href = a_tag['href'].replace('.html', '.md')
            a_tag.replace_with('[{}]({})'.format(a_tag.text, href))
        for pre in soup.find_all('pre'):
            pre_content = ''.join(map(str, pre.contents))
            pre_content = pre_content.replace('<br/>', '\n')
#             print(pre_content)
            pre.replace_with('```pde\n{}```'.format(pre_content))
        for br in soup.find_all('br'):
            br.replace_with('\n') # maybe double?
        for h3 in soup.find_all('h3'):
            h3.replace_with('### {}\n\n'.format(h3.string)) # maybe double?
        # these soups start with a table
        for cont in soup.contents[0]:  
            if cont.name is not None:
                line = print_c(cont)
                if line:
#                     print(line)
                    g.write(str(line))

