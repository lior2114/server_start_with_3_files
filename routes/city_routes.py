from flask import Blueprint,jsonify
from  controllers.city_controller import CityController
#מנתבת את הפעולה של המודל ושל הקונטרולר לתוך הסרבר ומדפיסה אותה 
#יוצרת מיני שרת לכל פעולה
city_bp = Blueprint("city", __name__)

@city_bp.route("/cities", methods = ["POST"])
def create_city():
    return CityController.create_city()

@city_bp.route("/cities", methods = ["GET"])
def show_all_cities():
    return CityController.show_cities()
