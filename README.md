# library_system

A library management system built with Django and Django REST Framework.

## Features

- Create, read, update, and delete books
- Search for books by title, author, or publication date
- Filter books by genre
- Archive old books

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Muazzeem/library_system.git
```

2. Navigate to the project directory:

```bash
cd library_system
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
It will install Django, Django REST Framework, and other required packages.

4. Run migrations:

```bash
python manage.py migrate
```

5.Run the server:

```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000/api/` to access the API documentation.
