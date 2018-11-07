class Attr:

    def __init__(self, name, options):
        self._Name = name
        self._Options = options
        self._Index = 0


    def get_options(self):
        options_copy = []
        for option in self._Options:
            options_copy.append(option)
        return options_copy


    def get_name(self):
        return self._Name

    def __iter__(self):
        return iter(self._Options)

    def __next__(self):
        try:
            self._Index += 1
            return self._Options[self._Index]

        except IndexError:
            self._Index = 0
            return []


