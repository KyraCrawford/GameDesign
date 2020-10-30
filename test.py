import datetime

name = 'KYRA'
date = datetime.datetime.now()
score = 12
def SCORE():
    with open('SCORE_RECORDS.txt') as s:
        records = open('SCORE_RECORDS.txt','a')
        records.write(str(name))
        records.write(' - ')
        records.write(str(score))
        records.write(' words ')
        records.write(date.strftime('%Y/%m/%d %H:%M'))
        records.write('\n')

SCORE()
