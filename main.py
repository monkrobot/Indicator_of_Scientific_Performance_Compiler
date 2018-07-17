from docxtpl import DocxTemplate
import test_interface

tpl=DocxTemplate('Forms/Form_to_fill_tpl.docx')

#year = '2018'
#kvartal = '3'
#surname = 'Ivanov'
#
#paper1 = {'label': 'Paper1', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#paper2 = {'label': 'Paper2', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#paper3 = {'label': 'Paper3', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#paper4 = {'label': 'Paper4', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#paper5 = {'label': 'Paper5', 'journal': 'Journal', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#
#papers = [paper1, paper2, paper3, paper4, paper5]
#
#monograph1 = {'label': 'Paper1', 'grif': 'grif', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#monograph2 = {'label': 'Paper2', 'grif': 'grif', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#monograph3 = {'label': 'Paper3', 'grif': 'grif', 'coauthors': 'Smironov', 'year': '2018', 'publish': 'Russia', 'pp': '-', 'volume': '34', 'score': '12'}
#
#monographs = [monograph1, monograph2, monograph3]
#
#conf1 = {'label': 'conf1', 'authors': 'Ivanov', 'conf_status': 'Internationsl', 'conf': 'IEEE', 'place_time': 'Russia, may 2018', 'score': '4'}
#conf2 = {'label': 'conf2', 'authors': 'Ivanov', 'conf_status': 'Internationsl', 'conf': 'IEEE', 'place_time': 'Russia, may 2018', 'score': '4'}
#
#conferences = [conf1, conf2]

context = {
    'institute': test_interface.institute,
    'director': test_interface.director,
    'document_year': test_interface.year,
    'kvartal': test_interface.kvartal,
    'surname': test_interface.surname,
    'name': test_interface.name,
    'patronymic': test_interface.patronymic,
    'position': test_interface.position,
    'sector': test_interface.sector,

    'papers_tbl_contents': test_interface.journal_papers,
    'paper_scores': test_interface.paper_scores,

    #'monographs_tbl_contents': monographs,
#
    #'conf_tbl_contents': conferences,
}

tpl.render(context)
tpl.save(test_interface.surname+'_PRND_'+test_interface.kvartal+'-'+test_interface.year+'.docx')