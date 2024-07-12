# Guruda-Backend


## Development Guide
1. Clone project  
   ```
   git clone https://github.com/MKM-EAI/backend.git
   ```  
2. create and run the virtual environment
   ```
   python virtualenv venv
   source venv/bin/activate
   ```  
4. Install libraries  
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` on root with the following format:
   ```shell
   PG_NAME=
   PG_USER=
   PG_PASSWORD=
   PG_HOST=
   PG_PORT=
   ```
6. Create Migrations  
   ```
   python ./manage.py makemigrations
   python ./manage.py migrate
   ``` 
7. Run the local server 
   ```
   python ./manage.py runserver
   ```  

### Running in Docker
1. Build image
    ```shell
    docker build . -t gbhisma/guruda-api
    ```
2. Run
    ```shell
    docker run -d -p 8000:8000 --name guruda-api --env-file=.env  <your-image-tag>
    docker run -d -p 8000:8000 --name guruda-api --env-file=.env  gbhisma/guruda-api
    ```
    Should be accessible from http://localhost:8000/

## Jangan lupa dokumentasikan library sebelum push
`pip freeze > requirements.txt`
