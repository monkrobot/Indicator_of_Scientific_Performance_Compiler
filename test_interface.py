#test

from functions.score_calc import score_calc

#scores
paper_scopus_score = 90
paper_rsci_score = 30

#Information about worker
institute = input('institute: ')
director = input('director: ')
year = input('year: ')
kvartal = input('kvartal: ')
surname = input('surname: ')
name = input('name: ')
patronymic = input('patronymic: ')
position = input('position: ')
sector = input('sector: ')

#journal papers
journal_papers = []
paper_scores = 0

while True:
    print('Add new journal paper')
    wtscore = input('1-Scopus / WoS, 2-RSCI, 3-Other')
    if wtscore == '1':
        p_score = paper_scopus_score
    elif wtscore == '2':
        p_score = paper_rsci_score
    elif wtscore == '':
        break
    else:
        p_score = 0

    label = input('Paper name: ')
    if label == '':
        break
    journal = input('journal: ')
    paper_year = input('paper year: ')
    publish = input('paper publisher: ')
    pages = input('pages: ')
    volume = input('volume: ')
    coauthors = []
    while True:
        print('Add coauthor')
        author = input('coauthor: ')
        if author == '':
            break
        else:
            coauthors.append(author)
    score = score_calc(coauthors, p_score)
    paper_scores += score
    paper = {'label': label, 'journal': journal, 'coauthors': ', '.join(coauthors), 'year': paper_year,
             'publish': publish, 'pp': pages, 'volume': volume, 'score': score}
    journal_papers.append(paper)