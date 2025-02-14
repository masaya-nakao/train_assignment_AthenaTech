# 🛠️ ビルドステージ
FROM golang:1.20 AS builder

# 作業ディレクトリを作成
WORKDIR /app

# Goのソースコードをコピー
COPY main.go .

# Goアプリケーションをビルド（静的リンクバイナリ）
# RUN go build -o app main.go
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app main.go

# 🚀 実行ステージ（軽量な環境）
FROM alpine:latest

# 作業ディレクトリを作成
WORKDIR /app

# ビルドステージからバイナリをコピー
COPY --from=builder /app/app .

# 実行ポートを指定
EXPOSE 8080

# アプリを実行
CMD ["./app"]
