# ベースイメージとして python:3.9-slim を使用
FROM python:3.9-slim

# FastAPI を動かすために必要なライブラリをインストール
RUN pip install fastapi uvicorn

# 作業ディレクトリを指定
WORKDIR /app

# ローカルの FastAPI アプリをコンテナにコピー
COPY main.py .

# FastAPI サーバーを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
