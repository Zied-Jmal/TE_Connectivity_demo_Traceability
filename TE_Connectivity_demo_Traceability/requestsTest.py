import requests
import json

# Base URL of the API
base_url = "http://localhost:8080/api"
email = "test2@gmail.com"
password = "test2"


# Helper function to make requests
def make_request(method, endpoint, data=None, token=None):
    url = f"{base_url}{endpoint}"
    headers = {
        "Content-Type": "application/ld+json",  # Content type set to application/ld+json
    }

    # If the token is provided, include it in the Authorization header
    if token:
        headers["Authorization"] = f"Bearer {token}"

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=json.dumps(data))
    elif method == "PUT":
        response = requests.put(url, headers=headers, data=json.dumps(data))
    elif method == "DELETE":
        response = requests.delete(url, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    return response


# 1. Register a new user
def test_register_user():
    print("Starting test_register_user...")
    register_data = {"email": email, "password": password}  # User registration data
    response = make_request("POST", "/register", register_data)
    print("Register User Response:", response.json())
    print("test_register_user finished.")


# 2. Login to get the JWT token
def test_login_user():
    print("Starting test_login_user...")
    login_data = {"email": email, "password": password}  # Login credentials
    response = make_request("POST", "/login", login_data)
    print("Login User Response:", response.json())

    # Extract the token from the login response
    if response.status_code == 200:
        token = response.json().get("token")
        print("test_login_user finished.")
        return token
    else:
        print("test_login_user failed.")
        return None


# 3. Create a product
def test_create_product(token):
    print("Starting test_create_product...")
    product_data = {
        "name": "Sample Product",
        "code": "SP001",
        "description": "A sample product for testing.",
    }
    response = make_request("POST", "/products", product_data, token)
    print("Create Product Response:", response.json())
    print("test_create_product finished.")


# 4. Get list of products
def test_get_products(token):
    print("Starting test_get_products...")
    response = make_request("GET", "/products", token=token)
    print("Get Products Response:", response.json())
    print("test_get_products finished.")


# 5. Get a single product
def test_get_product(token):
    print("Starting test_get_product...")
    product_id = 1  # Assuming the product with ID 1 exists
    response = make_request("GET", f"/products/{product_id}", token=token)
    print("Get Single Product Response:", response.json())
    print("test_get_product finished.")


# 6. Create a sensor
def test_create_sensor(token):
    print("Starting test_create_sensor...")
    sensor_data = {"sensor_id": "S1000", "sensor_type": "Temperature", "status": "Active"}
    response = make_request("POST", "/sensors", sensor_data, token)
    print("Create Sensor Response:", response.json())
    print("test_create_sensor finished.")


# 7. Get list of sensors
def test_get_sensors(token):
    print("Starting test_get_sensors...")
    response = make_request("GET", "/sensors", token=token)
    print("Get Sensors Response:", response.json())
    print("test_get_sensors finished.")


# 8. Get a single sensor
def test_get_sensor(token):
    print("Starting test_get_sensor...")
    sensor_id = 1  # Assuming the sensor with ID 1 exists
    response = make_request("GET", f"/sensors/{sensor_id}", token=token)
    print("Get Single Sensor Response:", response.json())
    print("test_get_sensor finished.")


# 9. Create a traceability log
def test_create_traceability_log(token):
    print("Starting test_create_traceability_log...")
    traceability_log_data = {
        "product_id": "/api/products/1",  # Assuming the product ID exists
        "sensor_id": "/api/sensors/1",  # Assuming the sensor ID exists
        "timestamp": "2025-03-13T12:00:00",
        "event_description": "Product temperature recorded by sensor.",
    }
    response = make_request("POST", "/traceability_logs", traceability_log_data, token)
    print("Create Traceability Log Response:", response.json())
    print("test_create_traceability_log finished.")


# 10. Get list of traceability logs
def test_get_traceability_logs(token):
    print("Starting test_get_traceability_logs...")
    response = make_request("GET", "/traceability_logs", token=token)
    print("Get Traceability Logs Response:", response.json())
    print("test_get_traceability_logs finished.")


# 11. Get a single traceability log
def test_get_traceability_log(token):
    print("Starting test_get_traceability_log...")
    log_id = 1  # Assuming the log with ID 1 exists
    response = make_request("GET", f"/traceability_logs/{log_id}", token=token)
    print("Get Single Traceability Log Response:", response.json())
    print("test_get_traceability_log finished.")


if __name__ == "__main__":
    # Step 1: Login to get JWT token
    print("Starting test...")
    token = test_login_user()

    if token:
        # Step 2: Use the token to test other endpoints
        print("JWT Token obtained. Starting other tests...\n")
        test_register_user()
        test_create_product(token)
        test_get_products(token)
        test_get_product(token)
        test_create_sensor(token)
        test_get_sensors(token)
        test_get_sensor(token)
        test_create_traceability_log(token)
        test_get_traceability_logs(token)
        test_get_traceability_log(token)
    else:
        print("Failed to obtain JWT token. Please check your login credentials.")
