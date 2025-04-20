import sqlite3
#המודל שלנו מה שכל פונקציה ופונקציה עושה
class City:
    #לאיפה ילד הדאדט בייס
    @staticmethod
    def get_db_connection():
        return sqlite3.connect("mydb.db")
    
    #יצירת שולחן של ערים
    @staticmethod
    def create_table():
        with City.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                    create table if not exists cities 
                    (
                    city_id integer primary key autoincrement,
                    name text not null 
                    )
                '''
            cursor.execute(sql)
            cursor.close()
    
    #הופסת ערים 
    @staticmethod
    def create_city(name):
        with City.get_db_connection() as conneciton:
            cursor = conneciton.cursor()
            sql = 'insert into cities (name) values (?)'
            cursor.execute(sql, (name,))
            city_id = cursor.lastrowid
            conneciton.commit()
            cursor.close()
            return {"id":city_id, "name":name}
    
    #מציג את כל הערים 
    @staticmethod
    def get_all():
        with City.get_db_connection() as conneciton:
            cursor = conneciton.cursor()
            sql = 'select * from cities'
            cursor.execute(sql)
            show = cursor.fetchall()
            cursor.close()
            return [dict(id=city[0], name = city[1]) for city in show]
        
    #מציג עיר לפי האיי  די שלה     
    @staticmethod
    def get_city_by_id(city_id):
        with City.get_db_connection() as connection:
            city = connection.execute("select * from cities where city_id = ?"), (city_id)
            city = city.fetchone()
            if city is None:
                return {"message":"city not found"}
            return {"city_id":city[0], "name":city[1]}