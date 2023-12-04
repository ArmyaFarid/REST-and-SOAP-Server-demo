# Running Flask and SOAP Server Apps

## Setup

1. Open a terminal or command prompt.
2. Navigate to the directory where your files are located.
3. Create a virtual environment:

    ```bash
    python3 -m env venv
    ```

4. Activate the virtual environment:

    - On macOS and Linux:

      ```bash
      source env/bin/activate
      ```

    - On Windows:

      ```bash
      env\Scripts\activate
      ```

5. Install the required packages from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Flask API REST (app_rest.py)

1. In the terminal, run the following command:

    ```bash
    flask --app app_rest.py --debug run  
    ```

The Flask API REST will start running on the specified host and port.


## Testing with REST Client (rest_client.py)

1. In a new terminal window, navigate to the directory where `rest_client.py` is located.
2. Make sure the virtual environment is activated.
3. Run the following command:

    ```bash
    python rest_client.py
    ```

The REST client will send requests to the Flask API REST and display the responses.


## Running the SOAP Server (app_soap.py)

1. In the terminal, run the following command:

    ```bash
    python app_soap.py
    ```

The SOAP server will start running on the specified host and port.


## Testing with SOAP Client (soap_client.py)

1. In a new terminal window, navigate to the directory where `soap_client.py` is located.
2. Make sure the virtual environment is activated.
3. Run the following command:

    ```bash
    python soap_client.py
    ```

The SOAP client will send requests to the SOAP server and display the responses.


## Running the Advanced SOAP Server (app_soap_advance.py)

1. In the terminal, navigate to the directory where `app_soap_advance.py` is located.
2. Run the following command:

    ```bash
    python app_soap_advance.py
    ```

The advanced SOAP server will start running on the specified host and port.

## Testing with Advanced SOAP Client (soap_advance_client.py)

1. In a new terminal window, navigate to the directory where `soap_advance_client.py` is located.
2. Make sure the virtual environment is activated.
3. Run the following command:

    ```bash
    python soap_advance_client.py
    ```

The advanced SOAP client will send requests to the advanced SOAP server and display the responses.