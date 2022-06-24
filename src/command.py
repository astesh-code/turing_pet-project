### class for Turing command - a set like "q1 1 > q1 1 R" ###

class command():
    def __init__(self, line):

        # start condition of machine - "from"
        self.f = {'state': line.split('>')[0].split()[0],
                  'sym': line.split('>')[0].split()[1]}

        # finish condition of machine - "to"
        self.t = {'state': line.split('>')[1].split()[0],
                  'sym': line.split('>')[1].split()[1],
                  'move': line.split('>')[1].split()[2]}

    def __str__(self):
        return f"{self.f['state']} {self.f['sym']} > {self.t['state']} {self.t['sym']} {self.t['move']}"
