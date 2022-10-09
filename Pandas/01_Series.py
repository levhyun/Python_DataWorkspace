# pandas 데이터 분석 라이브러리

import pandas as pd

# Series 1차원 데이터 ( 정수, 실수, 문자열 등 )

temp = pd.Series([-20, -10, 10, 20])
print(temp)

print("\nindex:0의 데이터 값 =",temp[0])

temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print("\nindex값 지정")
print(temp)

print("\nindex:'Feb'의 데이터 값 =",temp['Feb'])









