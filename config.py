import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class AppConfig:
    # 사용할 모델 설정 (OLLAMA, GPT, CHANDRA)
    USE_MODEL = os.getenv("USE_MODEL", "CHANDRA").upper()
    
    # OpenAI 설정
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GPT_MODEL = "gpt-4o"
    
    # Ollama 설정
    OLLAMA_MODEL = "gemma4:e2b"

    # Chandra OCR 설정
    CHANDRA_METHOD = "hf"  # "hf" (HuggingFace) 또는 "vllm"
    
    # 데이터베이스 설정 (MySQL)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
    DB_NAME = os.getenv("DB_NAME", "ai_db")
    
    # 서버 설정
    HOST = "0.0.0.0"
    PORT = 8000
