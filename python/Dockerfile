FROM python:alpine
WORKDIR /app
COPY requirements/backend.in .
RUN apk --no-cache add musl-dev linux-headers g++
RUN pip install --no-cache-dir -r backend.in
COPY . .
CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
