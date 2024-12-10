FROM alpine:latest

RUN apk update && apk upgrade && apk add --update --no-cache python3 py3-pip && \
python3 -m venv /.venv && \
/.venv/bin/pip install --no-cache-dir flask ansible ansible-vault

EXPOSE 8080

COPY templates/ /templates
COPY app.py/ /app.py

WORKDIR /

ENTRYPOINT ["/bin/sh", "-c", "source /.venv/bin/activate && python /app.py"]
