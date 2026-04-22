import mysql.connector
from config import AppConfig

def getDbConnection():
    """MySQL 데이터베이스 연결 생성"""
    try:
        conn = mysql.connector.connect(
            host=AppConfig.DB_HOST,
            port=AppConfig.DB_PORT,
            user=AppConfig.DB_USER,
            password=AppConfig.DB_PASSWORD,
            database=AppConfig.DB_NAME
        )
        return conn
    except Exception as e:
        print(f"DB 연결 에러: {e}")
        return None

def saveAnalysisResult(modelName, question, answer):
    """분석 결과를 MySQL 테이블에 저장"""
    print(f"[DB] 저장 시도 중... (Model: {modelName})")
    conn = getDbConnection()
    if conn is None:
        print("[DB] 연결 실패로 저장할 수 없습니다.")
        return False
    
    try:
        cursor = conn.cursor()
        
        # 테이블이 없는 경우 생성
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
        
        # 데이터 삽입
        insertSql = "INSERT INTO analysis_logs (model_name, question, answer) VALUES (%s, %s, %s)"
        cursor.execute(insertSql, (modelName, question, answer))
        
        conn.commit()
        print(f"[DB] 저장 성공: {cursor.rowcount}행 삽입됨.")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"[DB] 저장 중 예외 발생: {e}")
        if conn:
            conn.close()
        return False
