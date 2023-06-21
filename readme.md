
# Extracting device interface configuration
This is a Docker-compose app that consists of two parts: Python and a Postgres database.
The app's purpose is to parse a JSON file, from which it extracts needed data and then uploads them to the database. The whole app can be run with one command.




## Python part

The Python part parses JSON data and then uploads them to the Postgres database.

It does so by calling the main.py file. In this file, the "extract_json()" function is called. It filters data into needed sublists and here we can  alter the code to implement more interfaces. 

Then it calls the "to_class()" function. This function creates object instances with the needed data inside. Those objects are then stored in the "interfaces" list.

Function "get_list_of_interfaces()" then retrieves this list of objects.

After successful data parsing, Python creates a connection to the database. It creates table name "interfaces" via the function "create_db_and_table()". Then it adds data from the previous object list into the table via the "add_to_table()" function.

The connection to the database is closed via the function "quit_db()".
## Database part

Database is created by docker-compose.yaml file. User name, password and name of database is fetched from .env file.

## Creation of table "interfaces"

```sql
CREATE TABLE interfaces(id SERIAL PRIMARY KEY,
                        connection INTEGER,
                        name VARCHAR(255) NOT NULL,
                        description VARCHAR(255),
                        config json,
                        type VARCHAR(50),
                        infra_type VARCHAR(50),
                        port_channel_id INTEGER,
                        max_frame_size INTEGER)
```


## Deployment

To deploy this project run:

```bash
  docker-compose up
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`POSTGRES_DB`

`POSTGRES_HOST`

`POSTGRES_PORT`

## Screenshot of table after running the app
![scr](https://github.com/Rastisslav/interfaces/assets/99832718/5560f90f-0d34-43ee-8048-56fd2596fc23)


