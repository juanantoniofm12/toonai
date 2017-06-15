#!env/bin/python
# -*- coding:utf-8 -*-

import os
import json
import toonapp
import unittest
import tempfile

class BT(unittest.TestCase):
    def setUp(self):
        toonapp.app.testing = True
        self.app = toonapp.app.test_client()
        with toonapp.app.app_context():
            pass

    def tearDown(self):
        pass


class test_toonstuff(BT):
    def setUp(self):
        super(test_toonstuff, self).setUp()
        # some fake request data
        with open("sample.json") as fh:
            self.request_data = json.dumps(json.load(fh)) or u"{}"
            print "Loaded some data"
            print len(self.request_data)


    def test_basic(self):
        assert len(self.request_data) > 2 is True
        rv = self.app.post(
            "/v1/toonstuff",
            data=dict(self.request_data)
        )

        assert rv.data is True

#@app.route("/v1/toonstuff", methods=["POST", "PUT"])
if __name__ == '__main__':
    unittest.main()
