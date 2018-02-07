import pymysql as mariadb


def connect_db():
    connection = mariadb.connect(user='matt', password='bulbmatt#2')
