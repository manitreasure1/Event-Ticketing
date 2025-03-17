FROM python:3.13.1-slim
RUN apt-get update && apt-get install -y --no-install-recommends\
    tk \
    libtk8.6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


