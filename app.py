from flask import Flask 
from models.city import City 
from routes.city_routes import city_bp 

#יצירת שרת עם קובץ טקסט של הורדת הסיפריות
#python -m venv env
#env\Scripts\activate
# pip freeze > requirements.txt
#pip install -r requirements.txt

app = Flask(__name__)

#=========יצירת השרת תוך קריאה לרות======================
app.register_blueprint(city_bp)
City.create_table() #create city table 
City.get_all()

if(__name__=="__main__"):
    app.run(debug=True, host='0.0.0.0', port=5000)