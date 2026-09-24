# VA System

A simple Django web application for entering and viewing Verbal Autopsy (VA)
records. A VA is a method used to estimate the probable cause of death when a
doctor was not present, by interviewing a relative or caregiver about the
deceased's symptoms and circumstances before death. This system provides a
home page, an add-record form, a records list, and the Django admin for data
management. It is a learning project, not a production VA system.

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/123Benaiah/va-system.git
cd va-system
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Open in browser
```
http://127.0.0.1:8000/
```

## Live URL

https://123Benaiah.pythonanywhere.com/

## What I Learned

- What a Verbal Autopsy is, what it is used for, and why it exists.
- How Django operates - models, views, URLs, templates, and how they connect.
- How to deploy a Django project to PythonAnywhere using Git.
- How to use Git branches, meaningful commits, and a `.gitignore`.
- How to define a model with choices and generate migrations.

## Author

Benaiah Lushomo Mung'ambata
