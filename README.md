# Subscription Proyect API

This is a simple FastAPI project that simulates a subscription services.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10**: You can download it from [python.org](https://www.python.org/).
- **pip**: Python package installer, which typically comes with Python.

## Tests

To run the tests, execute the following command:

```bash
pytest
```

## Installation (locally)

Follow these steps to get the project running locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/elbeto87/gila-software.git
    cd gila-software
    ```
   
2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
   
## Running the Server

1. **Start the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```
   
2. **Access the API documentation**:
    Open your browser and go to:
    ```bash
    http://127.0.0.1:8000/docs
    ```
    This will open the interactive Swagger UI where you can test the API endpoints.

## Installation (Docker)

1. **Build the Docker image**:
    ```bash
    docker build -t gila-software .
    ```
   
2. **Run the Docker container**:
    ```bash
    docker run -d -p 8000:8000 gila-software
    ```
   
3. **Stop the Docker container**:
    ```bash
    docker stop <container_id>
    ```
   
## Usage

The API has the following endpoints:

### 1. Get all users
**GET /users**

Retrieve a list of all registered users.

### 2. Get all categories
**GET /categories**

Fetch all available categories.

### 3. Get all messages sent
**GET /messages**

Get a list of all messages sent to users.

### 4. Create a new user
**POST /create_user**

Add a new user to the system.

### 5. Create a new category
**POST /create_category**

Add a new category to the system.

### 6. Delete a user
**DELETE /delete_user/{user_id}**

Remove a user by ID.

### 7. Delete a category
**DELETE /delete_category/{category_id}**

Remove a category by ID.

### 8. Send a message
**POST /send_message**

Send a message to a user.

### 9. Revert to default data
**POST /default_data**

Reset the data to the default values.
   
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.