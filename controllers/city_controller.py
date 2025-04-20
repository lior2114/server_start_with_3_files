from flask import Flask,jsonify,request
from models.city import City
# ווידוא תקינות של ההכנסה של המשתמש 
class CityController:
    @staticmethod
    def create_city():
        data = request.get_json()
        if not data or 'name' not in data: #כי יש לנו משתנה בשם ניימ אז אם לא רושמים אותו בפוסט מאן לפני שנכניס שם הוא יחזיר שגיאה 
            return jsonify({"error":"name os requried"})
        result = City.create_city(data["name"])
        return jsonify(result)
    
    @staticmethod
    def show_cities():
        cities = City.get_all()
        if not cities:  # אם אין ערים במערכת
            return jsonify({"error": "No cities found"})
        return jsonify(cities)