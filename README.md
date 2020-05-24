# DimensionsApp

# Prerequisites
latest version of python and pip  
make sure virtualenv is using python3  

# Install dependencies
pip install -r requirements.txt  

# run migrations
python3 manage.py makemigrations  
python3 manage.py migrate --run-syncll_withdb  

# run server
python3 manage.py runserver
