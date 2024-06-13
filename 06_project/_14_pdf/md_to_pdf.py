# pip3 install mdcx
# pip3 install markdown
import markdown

def md2html(md_file, html_file):
    '''
    垃圾，不大好用，对表格支持的不够好
    :param md_file:
    :param html_file:
    :return:
    '''
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(html_file, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    md_file = 'D:/ws-ssdd2jetcollect/Markdown-Resume/Resume3.md'
    docx_file = "D:/ws-ssdd2jetcollect/Markdown-Resume/Resume3.md.docx"
    pdf_file = "D:/ws-ssdd2jetcollect/Markdown-Resume/Resume3.md.pdf"
    html_file = 'D:/ws-ssdd2jetcollect/Markdown-Resume/Resume3.md.html'

    md2html(md_file, html_file)

