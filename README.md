Airport API

This project is a Django REST Framework based API for managing flights, tickets, and orders.
Users can create and manage their flight tickets with a simple and secure API.

Features

	•	User authentication (Token-based)
	•	Flight listing and management
	•	Ticket creation and management
	•	Unique order numbers for better tracking
	•	Personal dashboard (only your tickets and orders visible)
	•	Admin permissions for managing flights and orders
	•	Swagger documentation

Tech Stack

	•	Python 3.9
	•	Django 4.2
	•	Django REST Framework
	•	drf-yasg (for Swagger API documentation)

How to use this API

1.	Clone the repository:
git clone https://github.com/IllyaKovaliuk/airport_api.git
2. Navigate to the project directory:
cd airport_api
3. Create venv and activate it
python -m venv venv
source venv/bin/activate
4. Install all libraries
pip install -r requirements.txt
5. Run server
python manage.py runserver

Contact

If you have any questions, feel free to open an issue or contact me!