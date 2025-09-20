# FastAPI MongoDB Application

This project is a simple FastAPI application that connects to a MongoDB database. It provides user-related routes for creating and retrieving user information.

## Project Structure

```
fastapi-mongodb-app
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── db
│   │   └── connection.py # Handles MongoDB connection
│   ├── models
│   │   └── user.py      # Defines the user model
│   ├── routes
│   │   └── user.py      # User-related routes
│   └── schemas
│       └── user.py      # Pydantic schemas for user validation
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-mongodb-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up MongoDB:**
   Ensure you have a MongoDB instance running. You can use a local instance or a cloud service like MongoDB Atlas.

5. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## Usage

- **Create a User:**
  Send a POST request to `/users/` with the user data in JSON format.

- **Get User Information:**
  Send a GET request to `/users/{user_id}` to retrieve user information.

## License

This project is licensed under the MIT License.