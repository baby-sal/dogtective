# CFG-Degree-Autumn-2024-Group-5
## adventure (crossy roads style) / puzzle based dog detective game

a dog detective navigates around cars while solving simple puzzles on the way


## Set-up and running order

The files should be actioned in the following order:

### 1. Config
Filepath: logic/score_db_connection/config.py

Add your username and password into the relevant fields in order to connect to the database.

### 2. requirements.txt
Refer to this document for any additional installations required.

Note: Should you have encounter any issues connecting to the database, please refer to the following:

- Having both mysql-connector and mysql-connector-python packages installed may cause conflicts.
  - Therefore please ensure only mysql-connector-python is installed
- If issues persist, please try uninstalling and reinstalling the following:
```
pip uninstall mysql-connector-python
pip install mysql-connector-python
```
 
### 3. SQL script
Filepath: logic/score_db_connection/dogtective_scores_db.sql

Run the `dogtective_scores_db.sql` script _(i.e. in SQLWorkbench or similar programme)_ to create the database