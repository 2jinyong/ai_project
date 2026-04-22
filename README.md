# 제마나이 CLI에게 요청한 내용

1.  ModelServing.md 파일을 읽고 내용을 숙지해

2.  코딩 규칙(Python 3.12, camelCase, 명시적 반복문 등)을 엄격히 준수할 것.
    멀티 모델 옵션: .env에서 USE_MODEL = "OLLAMA" 또는 "GPT"로 설정할 수 있게 해줘.
    OLLAMA일 때는 로컬의 gemma4:e2b를 사용하고, GPT일 때는 OpenAI API를 사용하도록 분기 처리해줘.
    이미지 처리: 사용자가 이미지를 업로드하고 질문을 던지면, 선택된 모델을 통해 이미지 속 텍스트를
    추출하고 질문에 답하는 /analyze API를 만들어줘.
    패키지 관리: 파이썬 파일 상단에 pip install fastapi uvicorn ollama openai python-multipart 등 필요한 설치
    명령어를 주석으로 달아줘.
    지금 바로 생성하고 코드를 작성해줘. 분석서버는 ipynb 로 일단 만들어서 내가 구동했다가
    나중에 .py 파일로 만들께

### - gemini가 만든 app.ipynb가 열리지않는 문제 발생하여 해결 요청
3.  app.ipynb노트북파일이 열리지않는 문제가 발생하는데 확인하고 다시 열리도록 작성해줘

### - 오류 해결요청을 하였으나 해결되지않고 계속 노트북파일이 깨지는 문제가 발상해여 직접 코드만 받아서 노트북파일을 수동으로 생성하여 복사붙여넣기하도록 요청
4.  너가 해결할 수 없는 문제인 것 같으니 코드만 나에게 주면 내가 수동으로 노트북파일에 붙여넣기를 할게

5.  pip install이 필요한 라이브러리들을 requirements.txt파일로 따로 빼서 만들어줘 나중에 내가 직접 pip install -r requirements.txt를 사용하여 install해줄거야

6.  simple_web 폴더를 생성하고, 그 안에 server.js, package.json, public/index.html 구조로 프로젝트를
    구성해줘.
    기술스택: Node.js (Express), Axios, HTML5, CSS (미니멀하고 깔끔한 디자인).
    핵심기능:
    이미지업로드: 사용자가브라우저에서이미지파일을선택하면화면에미리보기(Preview) 표시.
    질문입력: 텍스트박스를통해질문입력.
    API 연동: "분석하기" 버튼 클릭 시, Node.js 서버가 FastAPI 서버(http://localhost:8000/analyze)로 데이터를
    전달(Proxy)하고 결과를 받아와 화면에표시.
    디자인가이드:
    다크모드기반의깔끔한UI.
    분석중일때는"AI가분석중입니다..."라는로딩애니메이션표시.
    결과창에는추출된텍스트와답변을가독성있게출력.
    코딩스타일:
    모든주요로직에한국어주석필수.
    npm install에 필요한 패키지(express, multer, axios, cors)를 package.json에 포함하고 상단에 설치 명령어
    주석달아줘.
    실행방식: node server.js 입력 시 바로 http://localhost:3000에서 확인 가능하도록 세팅해줘

7.  데이터베이스 연동해서 질문한내용과 답변을 저장할수있게끔 코드를 수정해줘

# 바이브코딩 이후 테스트
    로컬에서 올라마 gemma4:e2b모델과 chandra ocr2버전 둘다 정상적으로 구동 확인완료
    이후 디비와 연동하여 질문지와 답변을 저장하는 것 까지 확인 완료
