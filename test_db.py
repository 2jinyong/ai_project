import mysql.connector
from config import AppConfig
import sys

# Unicode 출력 설정
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

def testDatabase():
    print(f"--- DB 상세 테스트 시작 ---")
    print(f"설정 정보: {AppConfig.DB_HOST}:{AppConfig.DB_PORT} / User: {AppConfig.DB_USER} / DB: {AppConfig.DB_NAME}")
    
    conn = None
    try:
        conn = mysql.connector.connect(
            host=AppConfig.DB_HOST,
            port=AppConfig.DB_PORT,
            user=AppConfig.DB_USER,
            password=AppConfig.DB_PASSWORD,
            database=AppConfig.DB_NAME
        )
        cursor = conn.cursor()
        
        # 1. 테이블 존재 여부 확인 및 생성
        createTableSql = """
        CREATE TABLE IF NOT EXISTS analysis_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            model_name VARCHAR(50),
            question TEXT,
            answer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(createTableSql)
        print("1. 'analysis_logs' 테이블 확인/생성 완료.")
        
        # 2. 테스트 데이터 삽입
        insertSql = "INSERT INTO analysis_logs (model_name, question, answer) VALUES (%s, %s, %s)"
        test_data = ("TEST_MODEL", "테스트 질문입니다.", "테스트 답변입니다.")
        cursor.execute(insertSql, test_data)
        conn.commit()
        print("2. 테스트 데이터 삽입 완료.")
        
        # 3. 데이터 확인
        cursor.execute("SELECT id, model_name, question, created_at FROM analysis_logs ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        if row:
            print(f"3. 최신 데이터 확인 성공: ID={row[0]}, Model={row[1]}, Time={row[3]}")
        
        cursor.close()
        return True
        
    except mysql.connector.Error as err:
        print(f"실패: MySQL 에러 발생 -> {err}")
    except Exception as e:
        print(f"실패: 일반 에러 발생 -> {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("DB 연결 종료.")

if __name__ == "__main__":
    testDatabase()
