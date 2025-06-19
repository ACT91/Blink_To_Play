import time

class BlinkTimer:
    def __init__(self, threshold=1.0):
        self.start_time = None
        self.threshold = threshold

    def update(self, is_closed):
        if is_closed:
            if self.start_time is None:
                self.start_time = time.time()
        else:
            self.start_time = None

    def is_long_blink(self):
        return self.start_time is not None and (time.time() - self.start_time) >= self.threshold
