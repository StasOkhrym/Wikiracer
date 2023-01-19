# Broscorp Test Task
### Wikiracer implementation

## Installing using Github
Python 3.10 and Docker must be installed

- Clone repo and set up virtual environment:
```shell
git clone https://github.com/StasOkhrym/ZIPAirlines-test-task.git
python -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```
- Build docker container for database:
```shell
docker-compose up --build
```

#### Notes:

- WikirRacer class implemented in `wikiracing.py`
- Required queries are written in `queries.sql` 
- Collected data for faster testing is located in `pg_data` folder
