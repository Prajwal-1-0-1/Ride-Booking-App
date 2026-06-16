# Ride Booking Backend

A scalable ride-booking backend built using Django and PostgreSQL that simulates the core functionalities of a modern ride-hailing platform.

The project focuses on ride creation, automatic nearest-driver assignment, ride lifecycle management, concurrency handling, and scalable backend architecture.

The backend is fully deployed and exposes REST APIs for ride operations.

---

## Features

* Rider creation and management
* Driver creation and management
* Ride booking using pickup and drop coordinates
* Automatic nearest-driver assignment

  * Haversine Formula
  * Bounding Box Optimization
* Ride lifecycle management

  * Create Ride
  * Start Ride
  * Complete Ride
  * Cancel Ride
* Multiple ride categories

  * Normal Ride
  * Luxury Ride
* Concurrency-safe ride creation using atomic transactions
* Django Admin integration
* PostgreSQL database integration
* Production deployment on Render
* RESTful API architecture

---

## Tech Stack

* **Backend:** Django
* **Database:** PostgreSQL
* **Language:** Python
* **ORM:** Django ORM
* **Deployment:** Render
* **WSGI Server:** Gunicorn

---

## Key Backend Concepts Implemented

* Atomic Transactions
* Database Locking & Concurrency Handling
* Driver Availability Management
* Ride Lifecycle State Management
* Distance-Based Driver Allocation
* Foreign Key Relationship Modeling
* PostgreSQL Integration
* Cloud Deployment & Production Debugging

---

## Project Architecture

```bash
ride_booking_backend/
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
└── ride_booking_backend/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
```

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Dinnerbone101/uber-backend.git
cd uber-backend
```

### Create Virtual Environment

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

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Update database credentials inside `settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ride_booking_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint                    | Description   |
| ------ | --------------------------- | ------------- |
| POST   | `/create-ride/<rider_id>/`  | Create a ride |
| POST   | `/start-ride/<ride_id>/`    | Start ride    |
| POST   | `/complete-ride/<ride_id>/` | Complete ride |
| POST   | `/cancel-ride/<ride_id>/`   | Cancel ride   |

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

## Live Deployment

### API Base URL

```text
https://uber-backend-3-recy.onrender.com/
```

### Example Endpoint

```text
https://uber-backend-3-recy.onrender.com/create-ride/1/
```

### Admin Panel

```text
https://uber-backend-3-recy.onrender.com/admin/
```

---

## Django Admin Features

* Rider Management
* Driver Management
* Ride Monitoring
* Database Inspection
* Driver Availability Tracking

---

## Deployment Stack

* Render
* PostgreSQL
* Gunicorn
* WhiteNoise

---

## Author

### Prajwal Y S

GitHub: https://github.com/Prajwal-1-0-1
