import time

class ETAProgress:
    def __init__(self, total: int):
        self.total = total
        self.start_time = time.time()
        self.last_time = self.start_time
        self.last_index = -1
        self.last_eta = 0
        self.last_speed = 0

    def update(self, index: int):
        now = time.time()
        elapsed = now - self.last_time
        if elapsed < 1:
            return
        self.last_time = now
        speed = (index - self.last_index) / elapsed
        self.last_index = index
        eta = (self.total - index) / speed
        self.last_eta = eta
        self.last_speed = speed
        print(f"ETA: {self._format_time(eta)} - Speed: {self._format_speed(speed)}it/s")

    def _format_time(self, seconds: float) -> str:
        seconds = int(seconds)
        hours = seconds // 3600
        seconds -= hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def _format_speed(self, speed: float) -> str:
        if speed > 1000:
            return f"{speed / 1000:.2f}k"
        return f"{speed:.2f}"

    def __str__(self):
        return f"- ETA: {self._format_time(self.last_eta)} - Speed: {self._format_speed(self.last_speed)}"

