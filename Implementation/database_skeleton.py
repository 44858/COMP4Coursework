#DATABASE
import sqlite3
class Database:
        def __init__(self, db_name):
                self._db_name = db_name
                self.CreateTables()

        def ExecuteSql(self, sql):
                with sqlite3.connect(self._db_name) as db:
                        cursor = db.cursor()
                        cursor.execute(sql)
        def CreateTables(self):
                sql = """create table if not exists Stock
                        (ProductID integer,
                        ProductName text,
                        Brand text,
                        Model text,
                        Quantity integer,
                        Price integer,
                        primary key(ProductID))"""
                self.ExecuteSql(sql)

        def AddNewProduct(self, name, brand, model, quantity, price):
                sql = """insert into Stock values
                        ((SELECT max(ProductID) FROM Stock)+1,
                        '{0}', '{1}', '{2}', {3}, {4})""".format(name, brand, model, quantity, price)
                self.ExecuteSql(sql)

        def GetAllProducts(self):
                with sqlite3.connect(self._db_name) as db:
                        cursor = db.cursor()
                        cursor.execute("select * from Stock")
                        products = cursor.fetchall()
                        return products
                        
g_database = Database("stock_database.db") 

