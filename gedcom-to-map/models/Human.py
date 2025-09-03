class Human:
    def __init__(self, xref_id):
        self.xref_id = xref_id
        self.name = None
        self.father = None
        self.mother = None
        self.pos = None

    def __repr__(self):
        return "[ {} : {} - {} {} - {} ]".format(
            self.xref_id, self.name, self.father, self.mother, self.pos
        )
