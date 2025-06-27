# Fashion API – Django REST Backend

This project is a RESTful API built using Django and Django REST Framework. It serves as a backend system for accessing and managing fashion product and merchant data.

## Project Overview

The API allows clients to:
- Retrieve all products and merchants
- Filter products by color and rating
- Create new product entries
- View products for a specific merchant
- Load bulk product and merchant data from a CSV file

## Directory Structure

```

fashion\_api/
│
├── fashion/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   └── load\_data.py       # CSV data loading script
│
├── fashion\_api/
│   └── settings.py
│
├── requirements.txt
└── manage.py

````

## Setup Instructions

### 1. Clone the Repository

Extract or clone the project files.

```bash
git clone <repo-url>
cd fashion_api
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Load Initial Dataset

Option A: From Django shell

```bash
python manage.py shell
>>> from fashion.load_data import run
>>> run()
>>> exit()
```

Option B: Run script directly (if structured with `if __name__ == "__main__":`)

```bash
python fashion/load_data.py
```

Make sure the CSV file is located where `load_data.py` expects it.

### 6. (Optional) Create Superuser

```bash
python manage.py createsuperuser
```

Or use the pre-set admin credentials:

* Username: `admin`
* Password: `admin123`

### 7. Run the Development Server

```bash
python manage.py runserver
```

Access the application at:

* API root: `http://127.0.0.1:8000/api/`
* Admin panel: `http://127.0.0.1:8000/admin/`

## Running Unit Tests

Run the tests using Django’s built-in test runner:

```bash
python manage.py test fashion
```

Expected output:

```
Ran 7 tests in ... seconds
OK
```

## REST Endpoints

| Method | URL Pattern                     | Description                      |
| ------ | ------------------------------- | -------------------------------- |
| GET    | `/api/`                         | Welcome message and API metadata |
| GET    | `/api/products/`                | List all products                |
| POST   | `/api/products/create/`         | Create a new product             |
| GET    | `/api/products/color/<color>/`  | Get products filtered by color   |
| GET    | `/api/products/high-rated/`     | Get products with rating ≥ 4.0   |
| GET    | `/api/merchants/`               | List all merchants               |
| GET    | `/api/merchants/<id>/products/` | List all products by merchant ID |

## Tech Stack

* Python 3.10
* Django 5.2.3
* Django REST Framework 3.16.0
* SQLite (default)
* Pandas (for CSV processing)

## Environment

* Operating System: Windows 10 Pro
* Development Tools: Visual Studio Code, Git, CMD

## License

This project was developed for academic purposes as part of the University of London's CM3035 Advanced Web Development module (June 2025).

## Author

Maryam Ibrahim
University of London
CM3035 – Advanced Web Development