from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Мы ищем переменную MY_APP_SECRET (или TEST, смотря как назовешь в Dokploy)
    # В коде лучше использовать понятное имя, а в Dokploy связать его с секретом
    secret_value = os.environ.get('SECRET_TEST', 'Секрет не найден в Environment')
    
    return f"""
    <h1>Проверка секретов</h1>
    <p>Значение секрета: <b>{secret_value}</b></p>
    """

if __name__ == "__main__":
    # Dokploy обычно ожидает порт 3000 или 5000, укажем явно
    app.run(host='0.0.0.0', port=5000)
