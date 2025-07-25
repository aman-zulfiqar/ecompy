🛍️ Flask Full-Stack E-Commerce API
A robust and extensible full-stack e-commerce API built with Flask. Designed using clean architecture principles, modular code structure, and production-grade best practices.

📌 Key Features
Modular blueprint-based API routing (/v1/shop)

Full-stack tech: Python, HTML, CSS, JavaScript, Mako

ORM integration using SQLAlchemy

Database migrations with Flask-Migrate (Alembic)

Session management via Flask-Login

Centralized configuration management (config.py)

Docker-ready setup for easy deployment

🧱 Tech Stack
🔹 Core
Python 3.11+

Flask

🔹 Backend
Flask-Migrate

SQLAlchemy

Flask-Login

🔹 Frontend (Minimal UI Support)
HTML / CSS

JavaScript

Mako Templates

1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/flask-ecommerce-api.git
cd flask-ecommerce-api
2. Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Configuration
Edit config.py or set environment variables:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
SECRET_KEY = 'your_secret_key'
5. Initialize Database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
6. Run the Application
bash
Copy
Edit
python app.py
The API will be accessible at:
👉 http://127.0.0.1:5000/v1/shop

🐳 Docker Usage (Optional)
Build and run the containerized app:

bash
Copy
Edit
docker build -t flask-ecommerce-api .
docker run -p 5000:5000 flask-ecommerce-api
🧪 Testing
Unit tests and integration tests can be added using pytest.
Example test file path: tests/test_routes.py

📄 License
This project is licensed under the MIT License.