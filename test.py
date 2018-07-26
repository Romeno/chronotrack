import chronotrack as ct


def main():

    api = ct.Chronotrack(client_id="e637a76f", user_id="romenoex@gmail.com", user_pass="Alksvoiim!7ya")
    api.set_auth_type(ct.AUTH_SIMPLE)

    events = api.events()
    # brackets = api.brackets()


if __name__ == "__main__":
    main()