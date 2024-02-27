class Template:
    def generate(self):
        raise NotImplementedError("generate() must be implemented in subclasses")

class StatusTemplate(Template):
    def generate(self):
        status = """|\tAplicacao\t|\tStatus\t|\tIP\t|\tPorta\t|\n"""
        return status