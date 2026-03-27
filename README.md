# Playwright Python Automation Framework

A modern, scalable, and maintainable **end‑to‑end automation framework** built with **Playwright (Python)**.  
Designed using industry‑standard architecture patterns including:

- Page Object Model (POM)
- PageFactory pattern
- BasePage abstraction
- Role‑based locator helpers
- Environment configuration via `.env`
- Automated scaffolding scripts
- Linting + formatting integration

---

## Features

### Modern Playwright + Python stack

Fast, reliable browser automation with first‑class sync support.

### Clean Page Object Model

Each page encapsulates its own locators and actions.

### PageFactory for centralized object creation

Ensures consistent wiring and reduces duplication.

### BasePage with shared utilities

Navigation, waits, role helpers, and common behaviors.

### RoleHelper abstraction

Stabilizes Playwright’s `get_by_role()` behavior and reduces flaky selectors.

### Environment‑driven configuration

Credentials, URLs, and environment settings loaded via `.env`.

### Auto‑generation scripts

A bash script creates:

- New Page Objects
- PageFactory entries
- Skeleton test files

Ensures consistency and accelerates development.

### Linting + formatting

Integrated:

- **Black** (auto‑formatter)
- **isort** (import sorting)
- **Pylint** (static analysis)

---

## Project Structure

```
playwright-pom/
│
├── requirements.txt
├── pytest.ini
├── README.md
│
├── tests/
│ ├── test_login.py
│ └── conftest.py
│
├── pages/
│ ├── base_page.py
│ └── login_page.py
│
└── utils/
    └── role_helpers.py
└── create_page.sh
└── create.sh
└── format.sh
└── scaffold_project.sh
```

## Installation

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\Activate.ps1  # Windows
```

### 2. Install required dependencies

```bash
pip install -r requirements.txt
```

### 3. Install playwright

```bash
playwright install
```

## Running Tests

### Run the full suite:

```bash
pytest -vv
```

### Run a single test:

```bash
pytest tests/test_login_dashboard.py
```

### Run test with browser:

```bash
ppytest --headed
```

### Generate html report:

```bash
pytest --html=reports/report.html
```

## Creating New Page Objects (Auto‑Generated)

Use the included scaffolding script

### Run the following command line:

```bash
./create_page.sh
```

You will be prompted for a Page Object name:

```
Enter Page Object name (e.g., DashboardPage):
```

The script automatically:

- Creates pages/<page_name>.py
- Appends a new property to factory/page_factory.py
- Creates tests/test\_<page_name>.py
  This ensures consistent structure across the entire framework.

## Architecture Overview

### BasePage

Provides shared functionality:

- Navigation
- Role‑based helpers
- Common waits
- Page readiness checks

### Page Objects

Encapsulate:

- Locators
- Actions
- Page‑specific helpers
  They do not contain assertions — tests own verification logic.

### PageFactory

Centralized object creation:

```Python
app = PageFactory(page)
app.login.login(...)
app.dashboard.is_loaded()
```

## ProjectLinting & Formatting

### Format code:

```bash
black .
isort .
```

### Run linting:

```bash
pylint pages factory tests
```

### Run linting on entire project:

Use the script format.sh to format entire project.

```bash
./format.sh
```

## Project Directory structure

```bash playwright-pom/
│
├── requirements.txt
├── pytest.ini
├── README.md
│
├── tests/
│ ├── test_login.py
│ └── conftest.py
│
├── pages/
│ ├── base_page.py
│ └── login_page.py
│
└── utils/
└── helpers.py
│


```
