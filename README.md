## Travel Booking Management System
## Tech Stack: Python · Django · PostgreSQL


## Overview 

  - TravelTrack is a web-based travel management system developed using Django and PostgreSQL.
  - The platform allows clients to register, login, and book travel packages based on available cities.
  - Admins can manage client data, travel packages, and city information from a centralized dashboard.


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


## How to Run the Project Locally

1. **Clone the repository**

git clone <your-repo-url>
cd Webenza_project

2. **Create & activate virtual environment**
   
python -m venv webenza_env
# For Windows:
webenza_env\Scripts\activate
# For Linux/Mac:
source webenza_env/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Configure your PostgreSQL database in settings.py**
Update DATABASES in your settings.py with your credentials.

5. **Run migrations and start the server**

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

