FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /event_management

RUN apt-get update && apt-get install -y \
    libpq-dev gcc postgresql-client netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /event_management/entrypoint.sh

EXPOSE 8000

CMD ["sh", "/event_management/entrypoint.sh"]



