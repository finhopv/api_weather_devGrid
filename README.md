# Weather Service

## Instalação do Docker

1. Install the Docker from [site oficial](https://docs.docker.com/get-docker/).

## how to run

1. Clone o repositório:
    ```sh
    git clone <URL-DO-REPOSITÓRIO>
    cd weather_service
    ```

2. Buid the Docker image:
    ```sh
    docker build -t weather_service .
    ```

3. run the contêiner:
    ```sh
    docker run -d -p 5000:5000 --name weather_service weather_service
    ```

## how to test

1. into the container:
    ```sh
    docker exec -it weather_service /bin/sh
    ```

2. run the tests:
    ```sh
    pytest --cov=app tests/

      or
    execute the
    run.py
   In Browser you can choose the:
      post /weather/list_city  
      get /weather/user_id
      get /weather_data/id 
    ```
    

## envirorment variables

make sure to confogure the environment variable`OPEN_WEATHER_API_KEY` with your Open Weather API token before build the docker image:
```sh
export OPEN_WEATHER_API_KEY=<YOUR_TOKEN>
