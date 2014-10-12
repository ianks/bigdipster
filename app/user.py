#!/usr/bin/env python3.4

from lib.basehandler import BaseHandler
from lib import database

class User(BaseHandler):
    def get(self):
        user_id = self.get_argument("user_id")
        data = database.get("user", user_id)
        self.api_response(data)
