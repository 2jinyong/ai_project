import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class AppConfig:
    # 사용할 모델 설정 (OLLAMA 또는 GPT)
    USE_MODEL = os.getenv("USE_MODEL", "OLLAMA").upper()
    
    # OpenAI 설정
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GPT_MODEL = "gpt-4o"
    
    # Ollama 설정
    OLLAMA_MODEL = "llava:latest"
    
    # 서버 설정
    HOST = "0.0.0.0"
    PORT = 8000
