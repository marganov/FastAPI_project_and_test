# FastAPI Authorization Project

Educational project to practice **FastAPI** authentication and **pytest** testing with **Allure** reports.

## 🚀 Features

* User authentication via **signed cookies** (`itsdangerous.TimestampSigner`).
* Simple in-memory user database.
* Session token generation and validation.
* Error handling: expired or invalid signatures.

## 📂 Project structure

```bash
project_authorisation/
│
├── config.py              # Configuration via pydantic-settings
├── routers/               # FastAPI routes (login, profile, user)
├── security/              # Cookie signing & verification
├── models/                # Pydantic models (User)
├── data/                  # Fake in-memory database
├── tests/                 # Tests (pytest + allure)
│   ├── functional/        # Functional tests (login)
│   ├── integration/       # Integration tests (profile)
│   ├── utils/             # Test client & helpers
│   └── conftest.py        # Common fixtures
└── ...
```

## ✅ Testing

* **Positive scenarios**: successful login, profile access with valid cookies.
* **Negative scenarios**: wrong password, missing/invalid/expired cookies.

## 🧪 Run tests

```bash
pytest tests/ --alluredir=allure-results -v
```

## 📊 Allure report

Generate and view the report:

```bash
allure serve allure-results
```

The report provides detailed step-by-step test information:

* Requests & responses
* Input data
* Assertions

---

Окей, Алексей 👍
Судя по всему, у тебя учебный проект на **FastAPI** с авторизацией через куки, защищённые подписью (`itsdangerous`), плюс покрытие **pytest**-тестами (позитивные и негативные сценарии) и интеграция с **Allure** для отчётности.

Вот пример `README.md`-description для репозитория 👇

---

# FastAPI Authorization Project

Учебный проект для изучения **FastAPI** и тестирования с использованием **pytest** и **Allure**.

## 🚀 Функционал

* Авторизация пользователей через **подписанные куки** (itsdangerous `TimestampSigner`).
* Простая имитация базы данных (in-memory).
* Генерация и валидация сессионных токенов.
* Обработка ошибок: истёкшая или некорректная подпись.

## 📂 Структура проекта

```bash
project_authorisation/
│
├── config.py              # Конфигурация через pydantic-settings
├── routers/               # FastAPI роуты (login, profile, user)
├── security/              # Работа с куки и подписью
├── models/                # Pydantic модели (User)
├── data/                  # Фейковая база данных
├── tests/                 # Тесты (pytest + allure)
│   ├── functional/        # Функциональные тесты (login)
│   ├── integration/       # Интеграционные тесты (profile)
│   ├── utils/             # Клиент и вспомогательные функции
│   └── conftest.py        # Общие фикстуры
└── ...
```

## ✅ Тестирование

* **Позитивные сценарии**: успешный логин, доступ к профилю с валидными куки.
* **Негативные сценарии**: неверный пароль, отсутствующие/битые/просроченные куки.

## 🧪 Запуск тестов

```bash
pytest tests/ --alluredir=allure-results -v
```

## 📊 Allure отчет

Генерация и просмотр отчёта:

```bash
allure serve allure-results
```

В отчёте доступна подробная информация о шагах тестов:

* Запросы и ответы
* Переданные данные
* Проверки (asserts)

---
