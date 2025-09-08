# FastAPI Authentication Project

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/tests-passing-green)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Учебный проект для изучения **FastAPI** с системой аутентификации через защищенные cookies и полным покрытием тестами.

## 🚀 Возможности

- ✅ Аутентификация пользователей через **подписанные cookies** (`itsdangerous.TimestampSigner`)
- ✅ Защищенные cookies с флагами `httponly`, `secure`, `samesite`
- ✅ Генерация и валидация сессионных токенов
- ✅ Обработка ошибок: истекшие или некорректные подписи
- ✅ RESTful API с использованием APIRouter
- ✅ Полное покрытие тестами (pytest + Allure)
- ✅ Pre-commit hooks для контроля качества кода

## 📂 Структура проекта

```bash
FastAPI_project_and_test/
│
├── main.py                # Главная точка входа приложения
├── routers/
│   └── routers.py        # API endpoints (login, profile, user)
├── security/
│   ├── config.py         # Конфигурация через pydantic-settings
│   └── cookies.py        # Работа с подписанными cookies
├── models/
│   └── user_model.py     # Pydantic модели
├── data/
│   ├── data_base.py      # In-memory база данных
│   └── users.py          # Тестовые пользователи
├── tests/
│   ├── functional/       # Функциональные тесты
│   │   ├── test_login_positive.py
│   │   ├── test_login_negative.py
│   │   └── test_session_cookie.py
│   ├── integration/      # Интеграционные тесты
│   │   └── test_profile.py
│   ├── utils/           # Вспомогательные функции
│   │   └── client.py
│   └── conftest.py      # Общие фикстуры pytest
├── .env                 # Переменные окружения
├── requirements.txt     # Зависимости проекта
├── pyproject.toml      # Конфигурация инструментов
├── .flake8             # Конфигурация flake8
└── .pre-commit-config.yaml  # Pre-commit hooks
```

## 🛠 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/marganov/FastAPI_project_and_test.git
cd FastAPI_project_and_test
```

### 2. Создание виртуального окружения

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# или
.venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=your-secret-key-here
SESSION_MAX_AGE=3600  # опционально, время жизни сессии в секундах
```

### 5. Установка pre-commit hooks (опционально)

```bash
pre-commit install
```

## 🚀 Запуск приложения

### Использование uvicorn напрямую

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Или через Python

```bash
python main.py
```

Приложение будет доступно по адресу: http://localhost:8000

## 📡 API Endpoints

### 1. Авторизация

```http
POST /login
Content-Type: application/json

{
  "username": "alexey",
  "password": "password_alex"
}
```

**Ответ:**
```json
{
  "message": "Login successful",
  "user_id": "uuid-here"
}
```

### 2. Получение профиля

```http
GET /profile
Cookie: session_token=signed_token_here
```

**Ответ:**
```json
{
  "message": "Welcome!",
  "user_id": "uuid-here"
}
```

### 3. Получение информации о пользователе

```http
GET /user
Cookie: session_token=signed_token_here
```

**Ответ:**
```json
{
  "session_token": "token_value"
}
```

## 🧪 Тестирование

### Запуск всех тестов

```bash
PYTHONPATH=. pytest tests/ -v
```

### Запуск с генерацией Allure отчета

```bash
PYTHONPATH=. pytest tests/ --alluredir=allure-results -v
```

### Запуск определенной категории тестов

```bash
# Только функциональные тесты
pytest tests/functional/ -v

# Только интеграционные тесты
pytest tests/integration/ -v
```

## 📊 Allure отчеты

### Генерация отчета

```bash
allure generate allure-results -o allure-report --clean
```

### Просмотр отчета

```bash
allure open allure-report
# или
allure serve allure-results
```

## ✅ Статус тестов

| Тест | Статус | Описание |
|------|--------|----------|
| `test_login_success` | ✅ Passing | Успешная авторизация |
| `test_login_fail_wrong_password` | ✅ Passing | Отказ при неверном пароле |
| `test_cookie_behavior[None]` | ✅ Passing | Проверка сессионных cookies |
| `test_cookie_behavior[3600]` | ✅ Passing | Проверка персистентных cookies |
| `test_profile_success` | ✅ Passing | Доступ к профилю с валидным токеном |
| `test_profile_fail_no_cookie` | ✅ Passing | Отказ без cookie |
| `test_profile_fail_invalid_cookie` | ✅ Passing | Отказ с невалидным cookie |

**Общий результат: 7/7 тестов пройдено успешно** 🎉

## 🔧 Инструменты разработки

- **black** - форматирование кода
- **isort** - сортировка импортов
- **flake8** - проверка стиля кода
- **pre-commit** - автоматические проверки перед коммитом

### Форматирование кода

```bash
black .
isort .
flake8 .
```

## 📝 Лицензия

MIT

## 👤 Автор

**Alexey Marganov**

- GitHub: [@marganov](https://github.com/marganov)

## 🤝 Вклад в проект

Приветствуются любые предложения и улучшения! Создавайте Issues и Pull Requests.

---

⭐ Если проект был полезен, поставьте звезду на GitHub!
