#import

#max_score = 30
#coauthors = []
#while True:
#    author = input('coauthors ')
#    if author == '':
#        break
#    else:
#        coauthors.append(author)

def score_calc(coauthors, max_score):
    return max_score / (len(coauthors)+1)

if __name__ == '__main__':
    print(score_calc(coauthors,max_score))
