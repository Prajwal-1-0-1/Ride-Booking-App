# Ride Booking Backend 

An Uber-like backend system built using Django and PostgreSQL that simulates the core functionalities of a ride-booking platform.  
The project focuses on ride creation, driver allocation, ride lifecycle management, concurrency handling, and scalable backend architecture.

---

## Features

- Rider creation and management
- Driver creation and management
- Ride booking using pickup and drop coordinates
- Ride creation using Rider ID
- Automatic driver assignment
- Ride lifecycle handling
  - Create ride
  - Start ride
  - Complete ride
  - Cancel ride
- Multiple pricing modes
  - Normal pricing
  - Luxury pricing
- Concurrency-safe ride creation using atomic transactions
- Spatial indexing support for efficient location-based queries
- REST-style backend APIs using Django

---

## Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL
- **Language:** Python
- **ORM:** Django ORM

---

## Key Backend Concepts Implemented

- Atomic transactions for concurrency handling
- Spatial indexing for optimized coordinate queries
- Database relationship modeling
- Ride lifecycle state management
- Service-based backend architecture
- PostgreSQL integration with Django ORM

---

## Project Structure

```bash
ride_booking/
│
├── manage.py
├── requirements.txt
│
├── ride_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│   ├── services.py
│
└── ride_booking/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ride-booking-backend.git
cd ride-booking-backend
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
        'NAME': 'ride_booking',
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
python manage.py migrate
```

---

### 6. Start the server

```bash
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/create_ride/` | Create a new ride |
| POST | `/start_ride/<ride_id>/` | Start an assigned ride |
| POST | `/complete_ride/<ride_id>/` | Complete an ongoing ride |
| POST | `/cancel_ride/<ride_id>/` | Cancel a ride |

---

## Example Request

### Create Ride

```http
POST /create_ride/
```

```json
{
    "rider_id": 1,
    "pickup_lat": 12.9,
    "pickup_lon": 77.5,
    "drop_lat": 13.0,
    "drop_lon": 77.6,
    "pricing_mode": "luxury"
}
```

---

## Author

**Prajwal Y S**

- GitHub: https://github.com/Dinnerbone101
