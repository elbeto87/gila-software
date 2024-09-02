# Subscription Proyect API

This is a simple FastAPI project that simulates a subscription services.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10**: You can download it from [python.org](https://www.python.org/).
- **pip**: Python package installer, which typically comes with Python.

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

TBD