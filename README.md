# Flask REST API with Flask-RESTful and Requests

This repository contains a Python application that implements a REST API using Flask and Flask-RESTful. It allows you to perform various CRUD (Create, Read, Update, Delete) operations on resources using HTTP requests. The application also uses the requests library to interact with external APIs.

## Getting Started

1- Python 3.x installed on your system.
2- A virtual environment (optional but recommended).

## Installation

1- Clone the repository to your local machine:

```shell
git clone https://github.com/yourusername/your-repo.git
```

2- Navigate to the project directory:

```shell
cd your-repo
```

3- (Optional) Create and activate a virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

3- Install the required Python packages:

```shell
pip install -r requirements.txt
```

## Usage

1- Run the Flask application:

```shell
python main.py
```

2- The API will be accessible at 'http://127.0.0.1:5000'

### API Endpoints

The following API endpoints are available:

- GET /products: Retrieve a list of all resources.
- GET /products/<id>: Retrieve a specific resource by ID.
- POST /products: Create a new resource.

## Example Usage

### Create a Resource

To create a new resource, send a POST request to http://127.0.0.1:5000/products with a JSON payload containing the resource data.

### Retrieve a Resource

To retrieve a specific resource by ID, send a GET request to http://127.0.0.1:5000/products<id>

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

-Thank you to the Flask and Flask-RESTful communities for creating such fantastic tools for building RESTful APIs in Python.
-Special thanks to the authors and contributors of the requests library for making it easy to work with HTTP requests.
