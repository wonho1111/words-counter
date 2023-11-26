import mysql.connector

import pandas as pd
from collections import Counter
import re

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# MySQL 연결 정보 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'viewing_history'
}

# MySQL에 연결
conn = mysql.connector.connect(**db_config)

# 예제 쿼리: 특정 테이블과 열을 지정하여 데이터 가져오기
query = "SELECT video_title FROM history_table"

# Pandas를 사용하여 데이터프레임으로 읽기
df = pd.read_sql_query(query, conn)

# 데이터프레임에서 특정 열의 데이터 가져오기
text_data = df['video_title'].str.lower().str.cat(sep=' ')

# 정규 표현식을 사용하여 단어 추출
words = re.findall(r'\b\w+\b', text_data)

# Counter를 사용하여 단어 빈도수 계산
word_counts = Counter(words)

# 가장 많이 나온 단어 순서대로 정렬
sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

# 시각화: 막대 그래프
plt.figure(figsize=(10, 6))
plt.bar(sorted_word_counts.keys(), sorted_word_counts.values())
plt.xlabel('단어')
plt.ylabel('빈도수')
plt.title('가장 많이 나온 단어 순위')
plt.xticks(rotation=45, ha='right')  # X 축 레이블 회전
plt.tight_layout()
plt.show()

# 연결 종료
conn.close()
# import mysql.connector

# # MySQL 연결 정보 설정
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',
#     'database': 'viewing_history'
# }

# # MySQL에 연결
# conn = mysql.connector.connect(**db_config)

# keyword = "playlist"

# try:
#     # 예제 쿼리: 특정 테이블과 열을 지정하여 데이터 가져오기
#     query = "SELECT COUNT(*) AS word_count FROM history_table WHERE LOWER(video_title) LIKE '%{keyword}%'"

#     # 쿼리 실행
#     cursor = conn.cursor()
#     cursor.execute(query)

#     # 결과 가져오기
#     result = cursor.fetchone()

#     # 출력
#     if result:
#         word_count = result[0]
#         print(f'The word "rnb" appears {word_count} times in the video_title column.')

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     # 연결 종료
#     conn.close()