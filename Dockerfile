FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["scrapy", "crawl", "price-watch"]
# slim the image with a multi-stage build
# pin chromium in the Docker image
# slim the image with a multi-stage build
