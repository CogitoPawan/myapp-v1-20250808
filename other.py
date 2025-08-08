notification_service/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── schemas.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── notification.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── notification_service.py
│   ├── utils/
│       ├── __init__.py
│       ├── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── test_notification.py
│
├── .env.example
├── requirements.txt
└── README.md

SECRET_KEY=your_secret_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token

fastapi==0.70.0
uvicorn==0.15.0
python-dotenv==0.19.0
twilio==6.63.0

# Notification Service

## Setup Instructions

1. Clone the repository:

2. Create and activate a virtual environment:

3. Install the required dependencies:

4. Create a `.env` file in the root directory based on the `.env.example` file:

Fill in the required values.

5. Run the FastAPI server:

6. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Running Tests
To run the unit tests:

## API Endpoints

- **POST /api/v1/send-notification**

  Request Body:

Response:

## Logging
Logs are printed to the console with the following format: