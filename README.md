## To run the application + db
**Run:**

```
docker-compose up
```
> This will spin up the db, migrate the db structure and start the application

## To access Web app:

```
localhost:8000

```
## To create a super user run

docker-compose run web python manage.py createsuperuser
