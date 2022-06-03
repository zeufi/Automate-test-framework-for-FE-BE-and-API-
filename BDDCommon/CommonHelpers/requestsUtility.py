
from BDDCommon.CommonConfigs.urlconfig import API_HOSTS
# from BDDCommon.CommonHelpers.credentialsUtility import CredentialsUtility
import requests
import os
import json
# from requests_oauthlib import OAuth1
import logging as logger


class RequestsUtility(object):

    def __init__(self):

        # wc_creds = CredentialsUtility.get_api_credentials()
        # set the default environment to test
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

        # self.auth = OAuth1(wc_creds['key'], wc_creds['secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
          f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
          f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers)
        pdb.set_trace()
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json
