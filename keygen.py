class KeyGenerator:
    def init(self, initial_key):
        self.initial_key = initial_key

    def next_key(self):
        return self.initial_key