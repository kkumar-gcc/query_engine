# query_engine

## How to use
```bash
# fork(clone) repository using
git clone https://github.com/{{username]}/query_engine.git

#go to chatty folder
cd query_engine

# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# copy .env.example to .env
cp .env.example .env

# run notebooks if you want to store data in chromodb vector database

# run fastapi server
uvicorn main:api --reload

# open http://localhost:8000/search?query={{query}} in browser or postman
# to get results for given query
```


