# FastAPI User Authentication with MongoDB

This project demonstrates user authentication (registration and login) using FastAPI and MongoDB. It includes endpoints for user registration, login, and token-based authentication.

## Prerequisites

- Python 3.7+
- MongoDB (running locally or on a remote server)
- FastAPI
- Required Python packages

## Installation

3. **Install Dependencies**

    ```bash
    pip install fastapi uvicorn pymongo pydantic passlib[bcrypt] python-jose
    ```

4. **Set Up MongoDB**

    Make sure MongoDB is running. Update the MongoDB connection string in `main.py` if necessary.

## Usage

1. **Run the Application**

    ```bash
    uvicorn main:app --reload
    ```

2. **API Endpoints**

    - **Register User**

      **Endpoint:** `/auth/register`  
      **Method:** `POST`  
      **Request Body:**
      ```json
      {
        "email":"user@email.com"
        "username": "user1",
        "password": "password123"
      }
      ```
      **Response:**
      ```json
      {
        "message": "User registered successfully"
      }
      ```

    - **Login User**

      **Endpoint:** `/auth/login`  
      **Method:** `POST`  
      **Request Body:**
      ```json
      {
       
        "username": "user1",
        "password": "password123"
      }
      ```
      **Response:**
      ```json
      {
        "access_token": "your_jwt_token",
        "token_type": "bearer"
      }
      ```

## Code Explanation

- **`main.py`**: Contains the FastAPI application instance, user registration, login endpoints, password hashing, and JWT token creation.

- **`models.py`** (if used): Contains MongoDB database models and connection setup.

## Configuration

- Update MongoDB connection details in `main.py` or `models.py`.

## Security

- Passwords are hashed using `passlib` before storage.
- JWT tokens are used for authentication and should be included in the `Authorization` header as `Bearer {token}` for protected endpoints.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- FastAPI for its performance and ease of use.
- MongoDB for its flexible database solution.

## Contact

For any questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).

