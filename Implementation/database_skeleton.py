#DATABASE
import sqlite3
class Database:
        def __init__(self):
                with sqlite3.connect("StockDB.db") as self.db:
                    self.CreateTables()
                    self.cursor = self.db.cursor()

        def ExecuteSql(self, sql):
                with sqlite3.connect("StockDB.db") as db:
                        cursor = db.cursor()
                        cursor.execute(sql)
        def CreateTables(self):
                sql = """create table if not exists StockDB
                        (ProductID integer,
                        ProductName text,
                        Brand text,
                        Model text,
                        Quantity integer,
                        Price integer,
                        primary key(ProductID))"""
                self.ExecuteSql(sql)

        def AddNewProduct(self, name, brand, model, quantity, price):
                sql = """insert into StockDB values
                        ((SELECT max(ProductID) FROM StockDB)+1,
                        '{0}', '{1}', '{2}', {3}, {4})""".format(name, brand, model, quantity, price)
                self.ExecuteSql(sql)

        def EditProduct(self, name, brand, model, quantity, price):
                sql = """UPDATE StockDB
                        SET 
                """
        def GetProductList(self):
                SQL = ("""SELECT ProductName FROM StockDB""")
                self.cursor.execute(SQL)
                self.db.commit()
                self.product_list = self.cursor.fetchall()
                return self.product_list

        def GetAllProducts(self):
                with sqlite3.connect("StockDB.db") as db:
                        cursor = db.cursor()
                        cursor.execute("select * from StockDB")
                        products = cursor.fetchall()
                        return products
                        
g_database = Database() 

