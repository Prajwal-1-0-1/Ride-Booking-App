# Ride Booking Backend

An Uber-like backend system built using Django and PostgreSQL that simulates the core functionalities of a ride-booking platform.

The project focuses on ride creation, automatic driver nearest assignment, ride lifecycle management, concurrency handling, and scalable backend architecture.

The backend is fully deployed on Render and exposes REST-style APIs for ride operations.

---

## Features

- Rider creation and management
- Driver creation and management
- Ride booking using pickup and drop coordinates
- Automatic nearest-driver assignment(using haversine formula and bounding box)
- Ride lifecycle management
  - Create ride
  - Start ride
  - Complete ride
  - Cancel ride
- Multiple ride types
  - Normal rides
  - Luxury rides
- Concurrency-safe ride creation using atomic transactions
- Django Admin integration for database management
- Cloud deployment with PostgreSQL integration
- REST-style backend APIs using Django

---

## Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL
- **Language:** Python
- **ORM:** Django ORM
- **Deployment:** Render

---

## Key Backend Concepts Implemented

- Atomic transactions for concurrency handling
- Database relationship modeling using Foreign Keys
- Ride lifecycle state management
- Driver availability management
- Distance-based nearest driver allocation
- PostgreSQL integration with Django ORM
- Cloud deployment and production debugging


---

## Project Structure

```bash
uber_backend/
│
├── manage.py
├── requirements.txt
│
├── rides/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│
└── uber_backend/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Dinnerbone101/uber-backend.git
cd uber-backend
```

---

### 2. Create virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure PostgreSQL

Update database credentials inside `settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uber_backend',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run the server

```bash
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/create-ride/<rider_id>/` | Create a new ride |
| POST | `/start-ride/<ride_id>/` | Start an assigned ride |
| POST | `/complete-ride/<ride_id>/` | Complete an ongoing ride |
| POST | `/cancel-ride/<ride_id>/` | Cancel a ride |

---

## Example Request

### Create Ride

```http
POST /create-ride/1/
```

```json
{
    "pickup_lat": 12.9716,
    "pickup_lon": 77.5946,
    "drop_lat": 12.9352,
    "drop_lon": 77.6245,
    "ride_type": "LUXURY"
}
```

---

## Admin Panel

Django Admin can be accessed at:

```text
/admin/
```

The admin panel supports:
- Rider management
- Driver management
- Ride monitoring
- Database inspection

---

## Deployment

The project is deployed on Render using:
- Gunicorn
- PostgreSQL
- WhiteNoise for static file serving

---

## Author

**Prajwal Y S**

- GitHub: https://github.com/Dinnerbone101
