from docxtpl import DocxTemplate

tpl=DocxTemplate('Forms/Form_to_fill_tpl.docx')

year = '2018'
kvartal = '3'
surname = 'Ivanov'

paper1 = {'label': 'Paper1', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
paper2 = {'label': 'Paper2', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
paper3 = {'label': 'Paper3', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
paper4 = {'label': 'Paper4', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
paper5 = {'label': 'Paper5', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}

papers = [paper1, paper2, paper3, paper4, paper5]

monograph1 = {'label': 'Paper1', 'grif': 'grif', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
monograph2 = {'label': 'Paper2', 'grif': 'grif', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
monograph3 = {'label': 'Paper3', 'grif': 'grif', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}

monographs = [monograph1, monograph2, monograph3]

context = {
    'document_year': year,
    'kvartal': kvartal,
    'surname': surname,

    'papers_tbl_contents': papers,

    'monographs_tbl_contents': monographs,
}

tpl.render(context)
tpl.save(surname+'_PRND_'+kvartal+'-'+year+'.docx')