# Лабораторна робота № 4

**Тема:** Тестування та інтеграція у гнучких технологіях.  
**Студент:** Ребенок Денис Олександрович  
**Група:** Б-F2-25-1-ПІ

## Мета

Ознайомитися з роллю тестування в Agile-проєктах, налаштувати середовище автоматизованого тестування, написати модульні тести та інтегрувати їх у CI/CD.

## Структура проєкту

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_math_module.py
├── math_module.py
├── requirements.txt
└── README.md
```

## Локальний запуск

Потрібен Python 3.12 або сумісна версія.

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## CI/CD через GitHub Actions

Workflow у файлі `.github/workflows/ci.yml` запускає автоматичне тестування після подій `push` і `pull_request`.

Після кожного push GitHub Actions встановлює Python, завантажує залежності та виконує тести PyTest.
