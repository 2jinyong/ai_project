# %%
# pip install fastapi uvicorn ollama openai python-multipart python-dotenv Pillow

import io
import base64
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import ollama
from openai import OpenAI
from config import AppConfig  # config.py에서 설정 불러오기

# %%
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# %%
def convertImageToBase64(imageBytes: bytes) -> str:
    """이미지 데이터를 Base64로 변환"""
    return base64.b64encode(imageBytes).decode("utf-8")

async def analyzeWithOllama(imageBytes: bytes, question: str) -> str:
    """Ollama 모델 분석"""
    try:
        response = ollama.generate(
            model=AppConfig.OLLAMA_MODEL,
            prompt=question,
            images=[imageBytes]
        )
        return response.get("response", "분석 결과 없음")
    except Exception as e:
        return f"Ollama 에러: {str(e)}"

async def analyzeWithGpt(imageBytes: bytes, question: str) -> str:
    """GPT 모델 분석"""
    try:
        client = OpenAI(api_key=AppConfig.OPENAI_API_KEY)
        imageBase64 = convertImageToBase64(imageBytes)
        
        response = client.chat.completions.create(
            model=AppConfig.GPT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": question},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imageBase64}"}}
                    ]
                }
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"GPT 에러: {str(e)}"

# %%
@app.post("/analyze")
async def processAnalyze(uploadFile: UploadFile = File(...), userQuestion: str = Form(...)):
    """분석 API 엔드포인트"""
    try:
        imageContent = await uploadFile.read()
        
        # config.py의 설정에 따라 모델 분기
        if AppConfig.USE_MODEL == "GPT":
            resultText = await analyzeWithGpt(imageContent, userQuestion)
        else:
            resultText = await analyzeWithOllama(imageContent, userQuestion)

        # 결과 텍스트 라인별 처리 (명시적 반복문)
        lines = resultText.split("\n")
        finalOutput = []
        for i in range(0, len(lines)):
            finalOutput.append(lines[i])

        return {
            "status": "success",
            "model": AppConfig.USE_MODEL,
            "answer": "\n".join(finalOutput)
        }
    except Exception as globalError:
        return {"status": "error", "message": str(globalError)}

# %%
if __name__ == "__main__":
    import uvicorn
    # config.py의 HOST, PORT 설정 사용
    uvicorn.run(app, host=AppConfig.HOST, port=AppConfig.PORT)


