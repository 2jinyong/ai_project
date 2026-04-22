const express = require('express');
const multer = require('multer');
const axios = require('axios');
const cors = require('cors');
const path = require('path');
const FormData = require('form-data');
const fs = require('fs');

const app = express();
const PORT = 3000;

// 미들웨어 설정
app.use(cors());
app.use(express.json());
app.use(express.static('public')); // public 폴더의 정적 파일 서비스

// multer 설정: 메모리에 파일을 임시 저장
const upload = multer({ storage: multer.memoryStorage() });

// 분석 요청 처리 API (Proxy)
app.post('/analyze', upload.single('image'), async (req, res) => {
    try {
        const { question } = req.body;
        const imageFile = req.file;

        if (!imageFile) {
            return res.status(400).json({ error: '이미지를 업로드해주세요.' });
        }

        // FastAPI 서버로 전달할 FormData 생성
        const formData = new FormData();
        formData.append('uploadFile', imageFile.buffer, {
            filename: imageFile.originalname,
            contentType: imageFile.mimetype,
        });
        formData.append('userQuestion', question || '이 이미지에 대해 설명해줘.');

        // FastAPI 서버(http://localhost:8000/analyze)로 데이터 전송
        const response = await axios.post('http://localhost:8000/analyze', formData, {
            headers: {
                ...formData.getHeaders(),
            },
        });

        // FastAPI로부터 받은 결과를 클라이언트에 반환
        res.json(response.data);
    } catch (error) {
        console.error('FastAPI 연결 오류:', error.message);
        res.status(500).json({ error: '서버 분석 중 오류가 발생했습니다.' });
    }
});

// 서버 시작
app.listen(PORT, () => {
    console.log(`서버 실행 중: http://localhost:${PORT}`);
});
