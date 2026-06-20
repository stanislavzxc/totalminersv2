# TotalMiners Backend v2 ⛏️

Бэкенд-часть платформы **totalminers.io** — современного майнинг-отеля. Сервис автоматизирует учет мощностей, управление клиентскими устройствами и финансовые потоки.

## 🛠️ Технологический стек
* **Frameworks:** Python (Flask / FastAPI) — гибридная архитектура для гибкой обработки эндпоинтов и высокопроизводительных асинхронных задач.
* **Database:** PostgreSQL (для надежного хранения данных) + Alembic (для управления миграциями).
* **Containerization:** Docker & Docker Compose (полное окружение в контейнерах).
* **Task Management:** Celery / Асинхронные задачи (скрипты автоматизации).

## 🔌 Интеграции
1. **Headframe API** — синхронизация данных пула, отслеживание хешрейта и статуса воркеров майнинг-отеля в реальном времени.
2. **Bybit API** — автоматизация финансовых шлюзов, отслеживание курсов криптовалют, обработка внутренних транзакций и начислений.

## 🚀 Быстрый запуск (Deployment)

> **⚠️ Важно:** На текущий момент автоматические миграции базы данных могут работать нестабильно. Для корректной инициализации схемы БД используйте процедуру ручного восстановления ниже.

### 1. Подготовка окружения
Создайте файл `.env` в корневой директории по примеру `..env.swp` и заполните необходимые доступы (БД, API ключи Headframe/Bybit).

### 2. Инициализация базы данных и запуск
Разверните контейнер базы данных, принудительно накатите структуру из SQL-дампа, а затем запустите остальные сервисы:

```bash
# 1. Запускаем только контейнер с PostgreSQL
sudo docker compose up -d db

# 2. Импортируем структуру схемы в ручном режиме
psql -U dbuser -h localhost -p 5432 totalminersdb < init_schema.sql

# 3. Поднимаем все остальные сервисы бэкенда (API, Admin, Tasks)
sudo docker compose up -d
```

## 🏗️ Архитектура и компоненты
``text
.
./
├── admin/
│   ├── db/
│   │   ├── base_model.py
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── models/
│   │       ├── balances.py
│   │       ├── billings_buy_requests.py
│   │       ├── billings_payments.py
│   │       ├── billings.py
│   │       ├── buy_request_miner_items.py
│   │       ├── buy_requests.py
│   │       ├── contries.py
│   │       ├── discounts.py
│   │       ├── employees.py
│   │       ├── feedbacks.py
│   │       ├── images.py
│   │       ├── __init__.py
│   │       ├── mail_compaign.py
│   │       ├── mail_templates.py
│   │       ├── markets_carts.py
│   │       ├── messages.py
│   │       ├── miner_items_categories.py
│   │       ├── miner_items.py
│   │       ├── news.py
│   │       ├── payments.py
│   │       ├── payments_sites.py
│   │       ├── purchases_records.py
│   │       ├── resets_passwords_requests.py
│   │       ├── settings.py
│   │       ├── tickets.py
│   │       ├── users.py
│   │       └── workers.py
│   ├── __init__.py
│   ├── modules/
│   │   ├── headframe.py
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── routers/
│   │   ├── billings.py
│   │   ├── buy_requests.py
│   │   ├── discounts.py
│   │   ├── employees.py
│   │   ├── feedbacks.py
│   │   ├── __init__.py
│   │   ├── mail_compaign.py
│   │   ├── mail_templates.py
│   │   ├── main_page.py
│   │   ├── miners_items_categories.py
│   │   ├── miners.py
│   │   ├── news.py
│   │   ├── non_payments.py
│   │   ├── payments.py
│   │   ├── settings.py
│   │   ├── tickets.py
│   │   ├── users.py
│   │   └── worker.py
│   ├── service.py
│   ├── static/
│   │   └── logo.png
│   ├── templates/
│   │   ├── base.html
│   │   ├── billing_page.html
│   │   ├── billings.html
│   │   ├── buy_request_page.html
│   │   ├── buy_requests.html
│   │   ├── discounts.html
│   │   ├── discounts_new.html
│   │   ├── employee_new.html
│   │   ├── employees.html
│   │   ├── feedbacks.html
│   │   ├── login.html
│   │   ├── miner_new.html
│   │   ├── miner_page.html
│   │   ├── miners.html
│   │   ├── miners_items_categories_create.html
│   │   ├── miners_items_categories.html
│   │   ├── miners_items_categories_page.html
│   │   ├── settings.html
│   │   ├── ticket_page.html
│   │   ├── tickets.html
│   │   ├── users.html
│   │   ├── users_page.html
│   │   ├── users_workers.html
│   │   ├── worker_create_boundary.html
│   │   ├── worker_init_real.html
│   │   ├── worker_new.html
│   │   ├── worker_new_real.html
│   │   ├── worker_page.html
│   │   └── workers_delete.html
│   └── utils.py
├── admin.dockerfile
├── admin_init/
│   ├── db/
│   │   ├── base_model.py
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── models/
│   │       ├── balances.py
│   │       ├── billings_buy_requests.py
│   │       ├── billings_payments.py
│   │       ├── billings.py
│   │       ├── buy_request_miner_items.py
│   │       ├── buy_requests.py
│   │       ├── contries.py
│   │       ├── discounts.py
│   │       ├── employees.py
│   │       ├── feedbacks.py
│   │       ├── images.py
│   │       ├── __init__.py
│   │       ├── markets_carts.py
│   │       ├── messages.py
│   │       ├── miner_items_categories.py
│   │       ├── miner_items.py
│   │       ├── payments.py
│   │       ├── payments_sites.py
│   │       ├── purchases_records.py
│   │       ├── resets_passwords_requests.py
│   │       ├── settings.py
│   │       ├── tickets.py
│   │       ├── users.py
│   │       └── workers.py
│   ├── __init__.py
│   ├── modules/
│   │   ├── headframe.py
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── routers/
│   │   ├── billings.py
│   │   ├── buy_requests.py
│   │   ├── discounts.py
│   │   ├── employees.py
│   │   ├── feedbacks.py
│   │   ├── __init__.py
│   │   ├── miners_items_categories.py
│   │   ├── miners.py
│   │   ├── settings.py
│   │   ├── tickets.py
│   │   ├── users.py
│   │   └── worker.py
│   ├── service.py
│   ├── static/
│   │   └── logo.png
│   ├── templates/
│   │   ├── access_forbidden.html
│   │   ├── base.html
│   │   ├── billing_page.html
│   │   ├── billings.html
│   │   ├── buy_request_page.html
│   │   ├── buy_requests.html
│   │   ├── discounts.html
│   │   ├── discounts_new.html
│   │   ├── employee_new.html
│   │   ├── employees.html
│   │   ├── feedbacks.html
│   │   ├── login.html
│   │   ├── miner_new.html
│   │   ├── miner_page.html
│   │   ├── miners.html
│   │   ├── miners_items_categories_create.html
│   │   ├── miners_items_categories.html
│   │   ├── miners_items_categories_page.html
│   │   ├── settings.html
│   │   ├── ticket_page.html
│   │   ├── tickets.html
│   │   ├── users.html
│   │   ├── users_page.html
│   │   ├── users_workers.html
│   │   ├── worker_create_boundary.html
│   │   ├── worker_init_real.html
│   │   ├── worker_new.html
│   │   ├── worker_new_real.html
│   │   ├── worker_page.html
│   │   ├── workers_delete.html
│   │   └── workers.html
│   └── utils.py
├── admin.py
├── alembic.ini
├── api/
│   ├── alembic/
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/
│   │       ├── 467c7ece2b69_added_profit_income_hosting_to_miner_.py
│   │       ├── 5775661d755b_initial.py
│   │       └── 5febce13adbf_add_discounts_table.py
│   ├── db/
│   │   ├── base_model.py
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── models/
│   │       ├── balances.py
│   │       ├── billings_buy_requests.py
│   │       ├── billings_payments.py
│   │       ├── billings.py
│   │       ├── businesses.py
│   │       ├── buy_request_miner_items.py
│   │       ├── buy_requests.py
│   │       ├── contents.py
│   │       ├── contries.py
│   │       ├── discounts.py
│   │       ├── employees.py
│   │       ├── faqs.py
│   │       ├── feedbacks.py
│   │       ├── images.py
│   │       ├── infos.py
│   │       ├── __init__.py
│   │       ├── markets_carts.py
│   │       ├── messages.py
│   │       ├── miner_items_categories.py
│   │       ├── miner_items.py
│   │       ├── payments.py
│   │       ├── payments_sites.py
│   │       ├── purchases_records.py
│   │       ├── resets_passwords_requests.py
│   │       ├── settings.py
│   │       ├── testmode.py
│   │       ├── tickets.py
│   │       ├── users.py
│   │       └── workers.py
│   ├── desktop.ini
│   ├── __init__.py
│   ├── modules/
│   │   ├── bybit.py
│   │   ├── headframe.py
│   │   ├── __init__.py
│   │   └── whattomine.py
│   ├── requirements.txt
│   ├── routers/
│   │   ├── api/
│   │   │   ├── auth/
│   │   │   │   ├── disable_mfa.py
│   │   │   │   ├── enable_mfa.py
│   │   │   │   ├── get_mfa_url.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── login.py
│   │   │   │   ├── register.py
│   │   │   │   ├── validate_user_authorization.py
│   │   │   │   └── veirfy_totp.py
│   │   │   ├── billings/
│   │   │   │   ├── get_all.py
│   │   │   │   ├── get.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── updates/
│   │   │   │       ├── cancel.py
│   │   │   │       ├── complete.py
│   │   │   │       ├── __init__.py
│   │   │   │       └── payment_type.py
│   │   │   ├── discounts/
│   │   │   │   ├── get_for_user.py
│   │   │   │   └── __init__.py
│   │   │   ├── feedbacks/
│   │   │   │   ├── create.py
│   │   │   │   └── __init__.py
│   │   │   ├── images/
│   │   │   │   ├── create.py
│   │   │   │   ├── delete.py
│   │   │   │   ├── get.py
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── market/
│   │   │   │   ├── calculator.py
│   │   │   │   ├── cart/
│   │   │   │   │   ├── buy.py
│   │   │   │   │   ├── get_all.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── set.py
│   │   │   │   └── __init__.py
│   │   │   ├── miners/
│   │   │   │   ├── balance.py
│   │   │   │   ├── business.py
│   │   │   │   ├── categories/
│   │   │   │   │   ├── get_all.py
│   │   │   │   │   ├── get.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── dashboards.py
│   │   │   │   ├── get_all.py
│   │   │   │   ├── get.py
│   │   │   │   ├── get_workers.py
│   │   │   │   ├── information.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── payments.py
│   │   │   │   └── workers.py
│   │   │   ├── settings/
│   │   │   │   ├── content.py
│   │   │   │   ├── faq.py
│   │   │   │   ├── get_all.py
│   │   │   │   ├── get.py
│   │   │   │   ├── info.py
│   │   │   │   └── __init__.py
│   │   │   ├── stats/
│   │   │   │   ├── all.py
│   │   │   │   ├── daily.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── monthly.py
│   │   │   │   └── weekly.py
│   │   │   ├── tickets/
│   │   │   │   ├── close.py
│   │   │   │   ├── create.py
│   │   │   │   ├── get_all.py
│   │   │   │   ├── get.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── messages/
│   │   │   │   │   ├── create.py
│   │   │   │   │   ├── get_all.py
│   │   │   │   │   └── __init__.py
│   │   │   │   └── sort.py
│   │   │   └── users/
│   │   │       ├── delete_wallet.py
│   │   │       ├── get_countries.py
│   │   │       ├── get_user_by_id.py
│   │   │       ├── __init__.py
│   │   │       ├── require_reset_password.py
│   │   │       ├── reset_password.py
│   │   │       ├── set_wallet.py
│   │   │       ├── testmodegetall.py
│   │   │       ├── testmodeget.py
│   │   │       ├── testmode.py
│   │   │       ├── update_image.py
│   │   │       ├── update_lang.py
│   │   │       ├── update_password.py
│   │   │       └── update_profile.py
│   │   └── __init__.py
│   ├── schemas.py
│   ├── services/
│   │   ├── base.py
│   │   ├── billings.py
│   │   ├── business.py
│   │   ├── content.py
│   │   ├── country.py
│   │   ├── discounts.py
│   │   ├── faq.py
│   │   ├── feedbacks.py
│   │   ├── headframe.py
│   │   ├── images.py
│   │   ├── info.py
│   │   ├── __init__.py
│   │   ├── market.py
│   │   ├── messages.py
│   │   ├── miners_categories.py
│   │   ├── miners.py
│   │   ├── payment.py
│   │   ├── settings.py
│   │   ├── stats.py
│   │   ├── testmode.py
│   │   ├── ticket.py
│   │   └── user.py
│   ├── tasks/
│   │   ├── balances/
│   │   │   ├── __init__.py
│   │   │   └── save.py
│   │   ├── billings/
│   │   │   ├── __init__.py
│   │   │   ├── payment_check.py
│   │   │   └── utils.py
│   │   ├── countries/
│   │   │   ├── every_start.py
│   │   │   └── __init__.py
│   │   ├── hostings/
│   │   │   ├── every_day.py
│   │   │   ├── every_month.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── payments/
│   │   │   ├── every_day.py
│   │   │   └── __init__.py
│   │   └── workers/
│   │       ├── check.py
│   │       └── __init__.py
│   └── utils.py
├── api.dockerfile
├── api.py
├── assets/
│   └── images/
│       ├── 182edad09b1ab2c9_202501151908%2E
│       ├── 2b83e1c355cfdd00_202503241548.png
│       ├── 52d32a28533ded8e_202501151907%2E
│       ├── 5539a2ed7f1014c5_202503241548.png
│       ├── b016f86fa398f9c3_202501151907%2E
│       ├── d5752d773e8d3e00_202503241548.png
│       └── f96146dd794c192a_202501151907%2E
├── config.py
├── countries.json
├── docker-compose.yml
├── git
├── init_schema.sql
├── logger.py
├── README.md
├── tasks.dockerfile
└── tasks.py
~~~

P.S. Deploy:
```bash
sudo docker compose up -d db
# We need to do this, cause migrations are broken
psql -U dbuser -h localhost -p 5432 totalminersdb < init_schema.sql
sudo docker compose up -d
```
