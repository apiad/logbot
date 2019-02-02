import requests


def send(token, msg, host="http://localhost", port=6778):
    response = requests.post("%s:%d" % (host,port), json=dict(
        token=token,
        msg=msg
    ))

def ask(token, msg, *actions, host="http://localhost", port=6778):
    response = requests.post("%s:%d" % (host,port), json=dict(
        token=token,
        msg=msg,
        actions=list(actions)
    ))

    return response.json()['response']

def yes(token, msg, host="http://localhost", port=6778):
    response = requests.post("%s:%d" % (host,port), json=dict(
        token=token,
        msg=msg,
        actions=['Yes', 'No']
    ))

    return response.json()['response'] == 'Yes'


class Client:
    def __init__(self, token, host="http://localhost", port=6778):
        self.token = token
        self.host = host
        self.port = port

    def send(self, msg):
        send(self.token, msg, self.host, self.port)

    def ask(self, msg, *actions):
        return ask(self.token, msg, *actions, host=self.host, port=self.port)

    def yes(self, msg):
        return yes(self.token, msg, self.host, self.port)
