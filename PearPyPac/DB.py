# -*- coding: utf-8 -*-

import MySQLdb
import configparser


class PearMySQL(object):

    def __init__(self):
        """ initialize """
        self.conf = None
        self.connector = None
        self.cursor = None

    def setConfig(self, conf_path):
        """ set configure """
        self.conf = configparser.ConfigParser()
        self.conf.read(conf_path)

    def openDB(self):
        """ open database """
        self.openConnect()
        self.openCursor()

    def closeDB(self):
        """ close database """
        self.closeCursor()
        self.closeConnector()

    def openConnect(self):
        """ set connector for database """
        _host = self.conf.get("mysql", "host")
        _db = self.conf.get("mysql", "db")
        _user = self.conf.get("mysql", "user")
        _passwd = self.conf.get("mysql", "passwd")
        self.connector = MySQLdb.connect(host=_host, db=_db, user=_user,
                                         passwd=_passwd)

    def openCursor(self):
        """ set cursor for database """
        self.cursor = self.connector.cursor(MySQLdb.cursors.DictCursor)

    def closeConnector(self):
        """ close connector for database """
        self.connector.close()

    def closeCursor(self):
        """ close cursor for database """
        self.cursor.close()

    # fetch request
    def queryFetch(self, query):
        self.openDB()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.closeDB()
        return results

    # insert, update & delete request
    def query(self, query):
        self.openDB()
        self.cursor.execute(query)
        self.connector.commit()
        self.closeDB()

if __name__ == '__main__':
    db = PearMySQL()
