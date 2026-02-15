
## INSTALLATION AND LAUNCHING GUIDE


```bash
    1) git clone https://github.com/mist258/DRFDocker.git

    2) Create a .env file and fill in the variables listed in .env.example

    3) poetry shell  (#initaialize environment)

    4) poetry install  (#install dependencies)

    4) docker compose build

    5) docker compose up -d

    Optional if the database wasn’t created, run the following command:

       docker exec -it drfdocker-db-1[container_name] psql -U postgres[user_name] -c "CREATE DATABASE [db_name]";

    6) docker compose run --rm app sh
        ./manage.py makemigrations
        ./manage.py migrate

```
# Available links for docs: 
http://0.0.0.0:8000/api/doc/ 


http://localhost/api/doc/ 
