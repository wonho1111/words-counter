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

# 정규 표현식을 사용하여 단어 추출 (여러 단어로 이루어진 패턴 선택)
genre_patterns = ['r&b', 'hiphop', 'jazz', '락']  # Add more genres as needed
pattern = '|'.join(rf'\b{genre}\b' for genre in genre_patterns)

selected_words = re.findall(pattern, text_data)

# Counter를 사용하여 단어 빈도수 계산
word_counts = Counter(selected_words)

# 시각화: 막대 그래프
plt.figure(figsize=(8, 6))
plt.bar(word_counts.keys(), word_counts.values())
plt.xlabel('장르')
plt.ylabel('빈도수')
plt.title('장르별 빈도수')
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