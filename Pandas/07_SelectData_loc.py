# 데이터 선택 (loc)

import pandas as pd

df = pd.read_excel('score.xlsx')

print(df.loc[0])
# 0 index번호의 전체 데이터 출력
"""
[result]
지원번호      no.1
이름         채치수
학교         북산고
키          197
국어          90
영어          85
수학         100
과학          95
사회          85
SW특기    Python
"""

