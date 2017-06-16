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

        self.headers = {
            'Content-Type': "application/json",
            "secret" : "toon-secret",
            "key" : "toon-key",
            "blabla" : "fofofofo"
        }


    def test_basic(self):
        rv = self.app.post(
            "/v1/mirror",
            data=self.request_data,
            headers=self.headers
        )
        response_body =  rv.response.next()
        assert rv.status == "200 OK"
        assert rv.content_type == "application/json"
        shared = set(json.loads(self.request_data)) & set(json.loads(response_body))
        assert len(shared) > 0


    def test_respond_to_heat_on(self):
        """
        Try t ofind a heat on command
        """
        rv = self.app.post(
            "/v1/toonstuff",
            data = self.request_data,
            headers = self.headers
        )
        response_body = rv.response.next()
        assert rv.status == "200 OK"
        assert rv.content_type == "application/json"
        response_data = json.loads(response_body)
        print [ x for x in response_data.iteritems()]
        assert len(response_body) > 2



#@app.route("/v1/toonstuff", methods=["POST", "PUT"])
if __name__ == '__main__':
    unittest.main()
