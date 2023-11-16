class Batch:
    def __init__(self, capacity, stream, timing):
        self.capacity = capacity
        self.stream = stream
        self.timing = timing
        self.students = []
