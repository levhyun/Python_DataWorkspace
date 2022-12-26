# 데이터 선택(기본)

import pandas as pd

df = pd.read_excel('score.xlsx')
""" * [score.xlsx]File_Data

   지원번호   이름   학교    키   국어   영어   수학  과학  사회        SW특기
0  no.1  채치수  북산고  197   90   85  100  95  85      Python
1  no.2  정대만  북산고  184   40   35   50  55  25        Java
2  no.3  송태섭  북산고  168   80   75   70  80  75  Javascript
3  no.4  서태웅  북산고  187   40   60   70  75  80         NaN
4  no.5  강백호  북산고  188   15   20   10  35  10         NaN
5  no.6  변덕규  능남고  202   80  100   95  85  80           C
6  no.7  황태산  능남고  188   55   65   45  40  35      PYTHON
7  no.8  윤대협  능남고  190  100   85   90  95  95          C#
"""

# Column 선택 (index)

print(df.columns[1])
# index 1번 데이터 출력 

print(df[df.columns[1]])
# df.columns[1] = 이름
# df[이름]
"""
[result]
  이름
 채치수
 정대만
 송태섭
 서태웅
 강백호
 변덕규
 황태산
 윤대협
"""

# 슬라이싱

print(df['영어'][0:5])
# 0~4 인덱스 번호의 영어칼럼의 데이터 출력

print(df[3:])
# 3~last 인덱스 번호의 모든 칼럼의 데이터 출력