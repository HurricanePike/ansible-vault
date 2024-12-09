FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip && \
python3 -m venv /.venv && \
source /.venv/bin/activate && \
pip install --no-cache flask && \
pip install --no-cache ansible && \
deactivate

EXPOSE 5000

COPY templates/ /templates
COPY app.py/ /app.py

WORKDIR /

CMD [ "/.venv/bin/python", "app.py" ]