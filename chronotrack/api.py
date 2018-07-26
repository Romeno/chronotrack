import requests
import hashlib
import json


AUTH_OAUTH2_WEB_FLOW = 0
AUTH_OAUTH2_PASSWORD_FLOW = 1
AUTH_HTTP_BASIC_AUTH = 2
AUTH_SIMPLE = 3

API_ENDPOINTS = {
    "production": "https://api.chronotrack.com/api",
    "test": "https://qa-api.chronotrack.com/api"
}


class Chronotrack:
    def __init__(self, client_id, user_id, user_pass, debug=True):
        self.client_id = client_id
        self.user_id = user_id
        self.user_pass = user_pass
        self.user_pass_sha1 = hashlib.sha1(self.user_pass.encode('ascii')).hexdigest()
        self.auth_type = AUTH_SIMPLE
        self.debug = debug
        self.endpoint = API_ENDPOINTS["test"]

    def set_auth_type(self, auth_type):
        self.auth_type = auth_type

    def set_debug(self, debug):
        self.debug = debug
        if self.debug:
            self.endpoint = API_ENDPOINTS["test"]
        else:
            self.endpoint = API_ENDPOINTS["production"]

    def request(self, resource_name, *args, format="json", method="GET", resource_id=None, sub_resource_name=None, **kwargs):
        url = self.endpoint

        # authentication params
        url_params = "client_id={}&user_id={}&user_pass={}".format(self.client_id, self.user_id, self.user_pass_sha1)

        url += "/{}.{}".format(resource_name, format)

        if resource_id:
            url += "/{}".format(resource_id)

        if sub_resource_name:
            url += "/{}".format(sub_resource_name)

        url += "?{}".format(url_params)
        url += "&".join(["{}={}".format(k, v) for k, v in kwargs.items()])

        r = requests.request(method=method, url=url)
        if r.ok:
            return json.loads(r.content.decode('utf8'))

    def events(self):
        result = self.request("event")
        return result

    def brackets(self, event_id):
        result = self.request("event", event_id, "bracket")
        return result

    def intervals(self, event_id):
        result = self.request("event", event_id, "interval")
        return result

    def races(self, event_id):
        result = self.request("race", event_id, "race")
        return result





