# Migrate data from Postgresql to Sqlite using python

### How to use
1. Change the name of sqlite db
2. Change the postgres connection parameters
3. Modify the select statement to select from the table you wish
4. Modify the insert statement to match the fields
5. Run using `python dump.py`
6. The script will create sqlite db file and import data from postgresql

_Scripts are for personal, one-off use. They don't contain error handling, or other aspects normally needed for running in production_