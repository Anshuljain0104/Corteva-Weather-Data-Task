 # API for accessing weather data and stats
 This is a Django-based API that provides weather data & stats to users. It includes all relevant api, script and other document.

The API endpoints provide access to the following functionalities:

    /api/weather - retrieves weather data
    /api/weather/stats - provides statistics about the data
    /api/schema/swagger-ui/ - Swagger UI that provides an overview of the API's capabilities.

## Prerequisites

The following prerequisites are required to use this API:

    Python
    SQLite

## Installation and Usage

### Create virtual environment:

    pip install virtualenv
    virtualenv env

### Activate the virtual environment:

    env/Scripts/activate (in Windows)
    source env/bin/activate (in Linux and Mac)

### Install the required dependencies:

    pip install -r requirements.txt

### Use ddl for database creation from the following path:


    model/ddl.sql

### Use below script to ingest the data:

    python ingest.py

### For running the server:

    python3 src/manage.py runserver

### Access the API endpoints from the following links:

    http://127.0.0.1:8000/api/weather
    http://127.0.0.1:8000/api/weather/stats
    http://127.0.0.1:8000/api/schema/swagger-ui/