# 1. Base image 선택 (Python 3.11 사용)
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 패키지 설치
# pip 최신화 후 requirements.txt 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4. FastAPI 애플리케이션 코드 복사
COPY . .

# 5. 실행 포트 설정
EXPOSE 8000

# 6. FastAPI 서버 실행 명령어
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
