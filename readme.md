
# Extracting device interface configuration

This is Docker-compose app constisting of two parts, Python and Postgres Database.
App's purpose is to parse Json file from where it extracts needed data and then uploads them to Database. Whole app can be run via one command 




## Python part

Python part parses Json data and then uploads them to Postgres Database.

It does so by calling main.py file. In this file, the extract_json() function is called. It filters data to needed sublists and here we can in future alter the code to implement more interfaces. 

Then it calls to_class() function. This function creates object instances with needed data put inside. Those obects are the stored to "interfaces" list.

Function get_list_of_interfaces() then retrieves this list of objects.

After succesful data parse, python creates connection to database. It creates table interfaces viac function "create_db_and_table()". Then adds data from previous object list into table via "add_to_table()" function.

Connection to database is closed via funciton "quit_db"
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

