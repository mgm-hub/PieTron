import json


class WebCodex:
    def __init__(self, theTestGenre, theFileName, CodexMap):
        self.theTestGenre = theTestGenre
        self.theFileName = theFileName
        self.CodexMap = CodexMap

    def get_codex_map(self):
        return self.CodexMap

    def get_file_name(self):
        return self.theFileName

    def print_object(self):
        print("theTestGenre :: " + self.theTestGenre)
        print("theFileName :: " + self.theFileName)
        print("CodexMap :: " + self.CodexMap)


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
