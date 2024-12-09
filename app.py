import os
import time
from flask import Flask, request, render_template
from random import randrange


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    # Получение данных из JSON
    data = request.get_json()
    print(data)
    # Вы можете получить значения из данных
    input_text = data.get('text', '')
    input_password = data.get('password', '')


    timestamp=randrange(100000)

    os.system(f"touch {timestamp}_password & touch {timestamp}_text")

    savePass = os.system(f'echo {input_password} > {timestamp}_password')

    with open(f'{timestamp}_text', 'w', encoding='utf-8') as file:
        file.write(input_text)

    command = os.system(
        f'cat {timestamp}_text | ansible-vault encrypt --vault-password-file {timestamp}_password > {timestamp}_secret')

    with open(f'{timestamp}_secret', 'r', encoding='utf-8') as secret:
        output = str(secret.read())

    os.system(f'rm -f {timestamp}*')

    response_message = f'{output}'

    return response_message, 200  # 200 - HTTP статус "OK"


@app.route('/decrypt', methods=['POST'])
def decrypt():
    # Получение данных из JSON
    data = request.get_json()
    print(data)
    # Вы можете получить значения из данных
    input_text = data.get('text', '')
    input_password = data.get('password', '')

    timestamp=randrange(100000)

    os.system(f"touch {timestamp}_password & touch {timestamp}_text")

    savePass = os.system(f'echo {input_password} > {timestamp}_password')

    with open(f'{timestamp}_text', 'w', encoding='utf-8') as file:
        file.write(input_text)

    command = os.system(
        f'ansible-vault decrypt {timestamp}_text --vault-password-file {timestamp}_password')

    with open(f'{timestamp}_text', 'r', encoding='utf-8') as secret:
        output = str(secret.read())

    os.system(f'rm -f {timestamp}*')

    response_message = f'{output}'

    response_message = f'{output}'
    return response_message, 200  # 200 - HTTP статус "OK"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port="8080")
