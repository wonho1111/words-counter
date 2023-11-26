import mysql.connector

def analyze_word_occurrences(database, table, column, word_array):
    # MySQL 연결 설정
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=database
    )

    cursor = connection.cursor()
    counts = []

    try:
        # 특정 테이블의 열에서 데이터 가져오기
        query = f"SELECT {column} FROM {table}"
        cursor.execute(query)
        rows = cursor.fetchall()

        counts = []

        # 데이터 분석
        total_occurrences = 0
        for word in word_array:
            for row in rows:
                if word in row[0]:
                    total_occurrences += 1
            counts.append(total_occurrences)
            total_occurrences = 0

#        print(f"Total occurrences of words in '{column}': {total_occurrences}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # 연결 종료
        cursor.close()
        connection.close()

# 사용 예시
database_name = "viewing_history"
table_name = "history_table"
column_name = "video_title"
words_to_analyze = ["R&B", "팝", "힙합"]

analyze_word_occurrences(database_name, table_name, column_name, words_to_analyze)