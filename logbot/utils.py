import requests


def send(token, msg, edit=None, progress=None, host="http://localhost", port=6778):
    response = requests.post("%s:%d" % (host,port), json=dict(
        token=token,
        msg=msg,
        progress=progress,
        edit=edit
    ))

    return response.json()

def ask(token, msg, *actions, host="http://localhost", port=6778):
    response = requests.post("%s:%d" % (host,port), json=dict(
        token=token,
        msg=msg,
        actions=list(actions)
    ))

    try:
        return response.json()['response']
    except:
        return None

def yes(token, msg, host="http://localhost", port=6778):
    return ask(token, msg, 'Yes', 'No', host=host, port=port) == 'Yes'


class Client:
    def __init__(self, token, host="http://localhost", port=6778):
        self.token = token
        self.host = host
        self.port = port
        self.last_id = None

    def send(self, msg, progress=None, edit=False):
        self.last_id = send(self.token, msg, progress=progress, edit=self.last_id if edit else None, host=self.host, port=self.port)['id']

    def ask(self, msg, *actions):
        return ask(self.token, msg, *actions, host=self.host, port=self.port)

    def yes(self, msg):
        return yes(self.token, msg, self.host, self.port)
