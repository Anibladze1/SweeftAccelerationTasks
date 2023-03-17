To run the project, first you have to download the project. Then open project in your IDE.

Add local interpreter: 

python3 -m venv "name of venv"
source "name of venv"/bin/activate

than run the following:

pip install requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# ENJOY ! 
