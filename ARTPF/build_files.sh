python3 -m install -r requirements.txt 
python3.9 manage.py make migrations 
python3.9 manage.py migrate 
python3.9 manage.py collectstatic --noinput

#TESTING
