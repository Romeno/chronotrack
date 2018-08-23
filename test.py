import chronotrack as ct

from server_keys import *


def main():

    api = ct.Chronotrack(client_id=CT_CLIENT_ID, user_id=CT_LOGIN, user_pass=CT_PASSWORD)
    api.set_auth_type(ct.AUTH_SIMPLE)
    api.set_debug()

    event = api.event(32804)
    print(event["data"])

    entries = api.results(race_id=81829, size=50)
    for e in entries["data"]:
        print(e["entry_type"])

    brackets = api.brackets(race_id=81829)
    for b in brackets["data"]:
        print(b["bracket_name"])


if __name__ == "__main__":
    main()
