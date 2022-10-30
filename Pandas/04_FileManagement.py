# 파일 저장 및 열기 (=DataFrame 객체를 excel, csv, txt 등의 형태의 파일로 저장 및 열기)

import pandas as pd

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
df = pd.DataFrame(data, index=['no.1','no.2','no.3','no.4','no.5','no.6','no.7','no.8'])
df.index.name = '지원번호'
print(df)

# 저장

# csv 파일로 저장
df.to_csv('score.csv', encoding='utf-8-sig')
df.to_csv('not_index_score.csv', encoding='utf-8-sig', index=False) # index없이 저장

# txt 파일로 저장
df.to_csv('score.txt', sep='\t') # tab으로 구분된 텍스트파일

# 엑셀 파일로 저장
df.to_excel('score.xlsx')


# 열기

# csv 파일 열기
df = pd.read_csv('score.csv')
print('\n\n[read_csv]\n\n',df)

df = pd.read_csv('score.csv', skiprows=1)
print('\n\n[read_csv] - 첫 번째 줄 무시 출력\n\n',df)

df = pd.read_csv('score.csv', skiprows=[2,4,6])
print('\n\n[read_csv] - 2,4,6 번째 줄 무시 출력\n\n',df)

df = pd.read_csv('score.csv', nrows=2)
print('\n\n[read_csv] - 2번째 줄 까지만 출력\n\n',df)

# txt 파일 열기
df = pd.read_csv('score.txt', sep='\t')
print('\n\n[txt]\n\n',df)

# 엑셀 파일 열기
df = pd.read_excel('score.xlsx')
print('\n\n[excel]\n\n',df)








