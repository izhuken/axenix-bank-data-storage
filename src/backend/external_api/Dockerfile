FROM python:3.12.1-slim-bullseye as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY ./ ./

RUN chmod +x /app/entrypoint.sh

EXPOSE 4001

ENTRYPOINT [ "/app/entrypoint.sh" ]