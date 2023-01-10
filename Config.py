def read_token():
    with open("token") as token_file:
        return token_file.read()


class Config:
    def __init__(self):
        self.token = read_token()

    def get_token(self):
        return self.token


