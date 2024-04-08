# Database and data model

This project presents how to add new table and data models. It is based alembic trace tools.

## Add new data model or change data model in the database
1. Under the folder `models` add new class with the new model name
2. In the file `Models.py` amend the import for the new model
3. run command: `alembic revision --autogenerate -m "changes information"` in the console with the path `*\Entities`
4. run command: `alembic upgrade head` to upgrade the changes to database
5. run command: `alembic downgrade -1` to revert the changes to database

