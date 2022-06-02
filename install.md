# Creating virtual environment
python -m venv env 

.\env\Scripts\activate 
.\env\Scripts\deactivate 

pip freeze > requirements.txt
pip install -r requirements.txt
    requirements.txt:
        requests==2.18.4
        google-auth==1.1.0


# Installation machine learning stuff
pip install tensorflow
pip install pandas
pip install requests
pip install matplotlib
pip install sklearn


# Installation django
pip install Django