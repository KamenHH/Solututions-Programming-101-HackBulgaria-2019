class Parser:
    def __init__(self, filename):
        self.parsed_contet = Parser.parse(filename)

    
    @staticmethod
    def parse(filename):
        try:
            with open(filename) as dbfile:
                content = dbfile.readlines()
            return content
        except FileNotFoundError:
            print("Error, database not found!")
            return None

    def content(self):
        return self.parsed_contet