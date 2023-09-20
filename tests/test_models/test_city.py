#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from unittest import skipIf
from os import getenv
import MySQLdb


class test_City(test_basemodel):
    """ """

    def setUp(self):
        username= getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.connection = MySQLdb.connect(host, username, password, db, port=3306)
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_new_city(self):
        rows = self.cursor.execute("SELECT name FROM cities")
        new = self.value()
        new.save()

    @skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "Storage is filestorage")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)
    @skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "Storage is filestorage")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
