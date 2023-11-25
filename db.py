import mysql.connector
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# MySQL 연결 정보 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'viewing_history'
}

# # MySQL에 연결
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# try:
#     # 예제 쿼리: 사용자 테이블에서 모든 사용자 가져오기
#     query = "SELECT * FROM history_table"
    
#     # 쿼리 실행
#     cursor.execute(query)
    
#     # 결과 가져오기
#     result = cursor.fetchall()

#     # Pandas를 사용하여 데이터프레임으로 읽기
#     df = pd.read_sql_query(query, conn)

#     # 데이터프레임 출력
#     print(df)
    
#     # 결과 분석 및 처리
#     for row in result:
#         # 각 행의 데이터에 접근
#         channel_name, video_title = row
#         print(f"Channel: {channel_name}, Video: {video_title}")

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     # 연결 종료
#     cursor.close()
#     conn.close()

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

# 가장 많이 나온 단어 및 빈도수 출력
# most_common_word, frequency = word_counts.most_common(1)[0]
# print(f"가장 많이 나온 단어: {most_common_word}, 빈도수: {frequency}")

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

# 시각화: 워드클라우드
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(sorted_word_counts)

# plt.figure(figsize=(10, 6))
# # plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.title('워드클라우드 - 가장 많이 나온 단어')
# plt.show()

# # 연결 종료
# conn.close()

# 연결 종료
conn.close()