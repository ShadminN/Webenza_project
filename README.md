# Travel Booking Management System

A full-stack Django-based travel booking and management system with client registration, admin dashboard, and city/package handling features. Built to manage customer interactions, city packages, and client data efficiently.It ia a web application developed using the Django framework, designed to allow clients to register, browse city packages, and submit booking information. Admins can manage data through a dashboard and update travel packages dynamically using integrated media (images, text).



## Features

- **User Registration with Captcha**: Prevents bot registrations using captcha verification.
- **Login System**: Secure authentication for clients and admins.
- **Dashboard**: 
  - Displays client bookings and package data.  
  - Allows admin to add new cities with images.  
  - Filter and manage client and package information.  
  - Migrate and manage additional client data.
- **Package Selection**: Clients can browse and select available travel packages for different cities.
- **PostgreSQL Integration**: All data is securely stored in the PostgreSQL database.
- **Data Migrations**: Easily migrate additional client and package data.
- **Database**:
  - PostgreSQL used as backend relational database. 
  - Django ORM used for data operations, migrations, and queries.

## Tech Stack

- **Backend:** Python, Django  
- **Database:** PostgreSQL  
- **Frontend:** Django Templates, HTML, CSS, JavaScript
- **Environments:** `webenza_env` virtual environment setup


## How to Run the Project Locally

### 1. Clone the repository 

git clone <your-repo-url>
cd Webenza_project

### 2. Create & activate virtual environment 

python -m venv webenza_env

For Windows:

webenza_env\Scripts\activate


For Linux/Mac:

source webenza_env/bin/activate

### 3. Install dependencies 

pip install -r requirements.txt

### 4. Configure your PostgreSQL database in settings.py 

Update DATABASES in your settings.py with your credentials.

### 5. Run migrations and start the server

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 6. Run the development server

python manage.py runserver

Access the site at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin.

## License
This project is licensed under the MIT License. See LICENSE for details.

