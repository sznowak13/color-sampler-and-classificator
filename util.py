COLOR_LABELS = {
    'red-ish': 0,
    'yellow-ish': 1,
    'green-ish': 2,
    'purple-ish': 3,
    'brown-ish': 4,
    'blue-ish': 5,
    'pink-ish': 6,
    'orange-ish': 7,
    'black-ish': 8,
    'white-ish': 9
}


class Result:
    def __init__(self, status, message, body):
        self.status = status
        self.message = message
        self.body = body

    def __repr__(self):
        return f'{self.status}: {self.message}'

    def to_dict(self):
        return {
            'message': self.message,
            'status': self.status,
            'body': self.body
        }


class ColorDataset:
    """
    Dataset class for color labels. Takes set of rgb values with labels corelated to this values.
    """
    def __init__(self, rawdata):
        self.data = [[row['red'], row['green'], row['blue']] for row in rawdata]
        self.target = [COLOR_LABELS[row['color_guess']] for row in rawdata]
        self.length = len(rawdata)

    def __repr__(self):
        return f"Color dataset with {len(self.data)} entries."
