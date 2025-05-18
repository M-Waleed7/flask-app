# Simple Flask App

This is a simple Flask application that demonstrates the basic structure and functionality of a Flask web application.

## Project Structure

```
simple-flask-app
├── app.py                # Main entry point of the Flask application
├── templates
│   └── index.html       # HTML template for the web application
├── .env                  # Environment variables for the application
├── Dockerfile            # Instructions to build a Docker image
├── docker-compose.yml    # Defines services for the Docker application
├── requirements.txt      # Lists Python dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd simple-flask-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   Create a `.env` file in the root directory and add your configuration settings.

5. **Run the application:**
   ```
   python app.py
   ```

## Docker Instructions

1. **Build the Docker image:**
   ```
   docker build -t simple-flask-app .
   ```

2. **Run the application using Docker Compose:**
   ```
   docker-compose up
   ```

