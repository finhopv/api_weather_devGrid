# Weather Service

## Description

This service collects weather data from the Open Weather API and stores it in a SQLITE3 database. It provides endpoints to start data collection and check progress.

## Functionalities

- **POST /weather/**: Receives a user-defined ID, collects weather data from the Open Weather API and stores:
 - User-defined ID (unique for each request)
 - Date and time of request
 - JSON data with:
 - City ID
 - Temperature in Celsius
 - Moisture
- **GET /weather/{user_id}**: Receives the ID defined by the user, returns the data collection progress.

## Requirements

-Docker
- Docker Compose

## Installation

### Steps

1. Clone the repository:

 ```sh
 git clone <repository-url>
 cd weather_service
 ```

2. Create a `.env` file in the project root directory with the following variables:

 ```env
 SECRET_KEY=your_open_weather_api_key
 ```

3. Build and start Docker containers:

 ```sh
 docker-compose up --build
 ```

## Usage

### Endpoints

#### POST /weather/

Starts collecting weather data for the specified cities.

- **URL**: `/weather/`
- **HTTP Method**: `POST`
- **Request Body**:

 ```json
 {
 "user_id": "unique_user_id",
 "city_ids": [2172797, 5128581]
 }
 ```

- **Response**:

 ```json
 {
 "message": "Weather data collection started."
 }
 ```

#### GET /weather/{user_id}

Checks data collection progress for the specified user.

- **URL**: `/weather/{user_id}`
- **HTTP Method**: `GET`
- **Response**:

 ```json
 {
 "user_id": "unique_user_id",
 "completed_cities": 0
 }
 ```

## Tests

### Test Coverage

The project has more than 90% test coverage. The tests are located in the `tests/` directory.

### Test Execution

To run the tests, follow the steps below:

1. Make sure you have all dependencies installed in a virtual environment:

 ```sh
 pip install -r requirements.txt
 ```

2. Run the tests using `pytest`:

 ```sh
 pytest --maxfail=1 --disable-warnings -v
 ```


## Design Decisions

- **FastAPI**: Chosen for its efficiency and native support for asynchronous operations.
- **SQLAlchemy**: Used for the ORM, facilitating interaction with the PostgreSQL database.
- **Sqlite**: (RDBMS) light, Embeddable, self-sufficient and transactional.
- **httpx**: Asynchronous library for HTTP requests.
- **Docker**: To ensure that the environment is consistent and replicable.

## Docker installation

###Windows

1. Download and install Docker Desktop: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
2. Follow the installation instructions.

### macOS

1. Download and install Docker Desktop: [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)
2. Follow the installation instructions.

###Linux

1. Follow the official Docker installation instructions for your distribution: [Docker Engine - Community](https://docs.docker.com/engine/install/)
2. Install Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## How to Execute

1. Clone the repository and navigate to the project directory:

 ```sh
 git clone <repository-url>
 cd weather_service
 ```

2. Configure the environment variables in the `.env` file.

3. Build and start Docker containers:

 ```sh
 docker-compose up --build
 ```

4. The service will be available at `http://localhost:8000`.

## How to Test

1. Make sure your Docker containers are running.
2. Run the tests with `pytest`:

 ```sh
 pytest --maxfail=1 --disable-warnings -v
 ```

## Contribution

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.
