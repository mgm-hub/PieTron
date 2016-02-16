import json


class WebCodexShell:
    def __init__(self, WebCodex):
        self.WebCodex = WebCodex


    def get_web_codex(self):
        return self.WebCodex


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
