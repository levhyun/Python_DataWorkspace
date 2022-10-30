# 데이터 확인

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

# DataFrame 확인

df.describe()
# 계산 가능한 데이터에 대해 Column 별로 데이터 갯수, 평균, 표주편차, 최소/최댓값 등의 정보를 보여준다.
"""
                키          국어          영어          수학         과학         사회
count    8.000000    8.000000    8.000000    8.000000   8.000000   8.000000
mean   188.000000   62.500000   65.625000   66.250000  70.000000  60.625000
std      9.985704   29.519969   26.917533   30.325614  23.754699  32.120032
min    168.000000   15.000000   20.000000   10.000000  35.000000  10.000000
25%    186.250000   40.000000   53.750000   48.750000  51.250000  32.500000
50%    188.000000   67.500000   70.000000   70.000000  77.500000  77.500000
75%    191.750000   82.500000   85.000000   91.250000  87.500000  81.250000
max    202.000000  100.000000  100.000000  100.000000  95.000000  95.000000
"""

# df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   지원번호    8 non-null      object
 1   이름      8 non-null      object
 2   학교      8 non-null      object
 3   키       8 non-null      int64 
 4   국어      8 non-null      int64 
 5   영어      8 non-null      int64 
 6   수학      8 non-null      int64 
 7   과학      8 non-null      int64 
 8   사회      8 non-null      int64 
 9   SW특기    6 non-null      object
dtypes: int64(6), object(4)
memory usage: 768.0+ bytes
None
"""

df.head() # 처음 기본 갯수(5)개 가져 오기
df.head(7) # 처음 7개 가져 오기
df.tail() # 마지막 기본 갯수(5)개 가져 오기
df.tail(3) # 마지막 3개 가져 오기

# print(df.values)
# 값 보기
"""
[['no.1' '채치수' '북산고' 197 90 85 100 95 85 'Python']
 ['no.2' '정대만' '북산고' 184 40 35 50 55 25 'Java']
 ['no.3' '송태섭' '북산고' 168 80 75 70 80 75 'Javascript']
 ['no.4' '서태웅' '북산고' 187 40 60 70 75 80 nan]
 ['no.5' '강백호' '북산고' 188 15 20 10 35 10 nan]
 ['no.6' '변덕규' '능남고' 202 80 100 95 85 80 'C']
 ['no.7' '황태산' '능남고' 188 55 65 45 40 35 'PYTHON']
 ['no.8' '윤대협' '능남고' 190 100 85 90 95 95 'C#']]
"""

# print(df.index)
# 인덱스 보기

# print(df.columns)
# 칼럼보기
# Index(['지원번호', '이름', '학교', '키', '국어', '영어', '수학', '과학', '사회', 'SW특기'], dtype='object')

# print(df.shape)
# (row, column)
# (8, 10)


# Series 확인

#1번
print('1번\n{0}\n'.format(df['키'].nlargest(3))) # 키 큰 사람 순서대로 3명 데이터
#2번
print('2번\n{0}\n'.format(df['키'].sum())) # 키를 모두 더한 값 출력
#3번
print('3번\n{0}\n'.format(df['SW특기'].count())) # SW특기 카운트 값 출력
#4번
print('4번\n{0}\n'.format(df['학교'].unique())) # 학교 종류 출력
#5번
print('5번\n{0}\n'.format(df['학교'].nunique())) # 학교 종류 갯수 출력





