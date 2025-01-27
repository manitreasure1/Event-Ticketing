FROM python:3.13.1-slim
RUN apt-get update && apt-get install -y \
    tk \
    libtk8.6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

