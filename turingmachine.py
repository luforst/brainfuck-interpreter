class TuringMachine():
    """The TuringMachine class represents a Turing machine and is initialised by optionally passing a tape and an index"""
    def __init__(self, tape=[0], index=0):
        self._tape = tape
        self._index = index

    def __repr__(self):
        return "Turing machine with tape\n   " + self._tape + "\non index " + self._index
    
    @property
    def tape(self):
        return self._tape

    @tape.setter
    def tape(self):
        if type(tape) != list:
            raise TypeError(tape, "is not a list")
        for i in tape:
            if type(i) != int:
                raise TypeError(i, "is not an integer")
        self._tape = tape

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self):
        if type(index) != int:
            raise TypeError("Turing machine index has to be an integer")
        if index > self.tape().len():
            raise ValueError("Index out of current range")
        self._index = index

    @index.setter
    def index_inc(self):
        self._index += 1

    @index.setter
    def index_dec(self):
        self._index -= 1

    @property
    def curr_cell(self):
        return self.tape()[self.index()]

    @tape.setter
    def curr_cell(self):
        if type(curr_cell) == int:
            self._tape[self.index()] = curr_cell

    @tape.setter
    def curr_cell_inc(self):
        self._tape[self.index()] += 1

    @tape.setter
    def curr_cell_dec(self):
        self._tape[self.index()] -= 1


