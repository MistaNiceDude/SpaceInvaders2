## Custom thread subclass

import threading


class Threadable(threading.Thread):
    def __init__(self, threadID: int, name: str, delay_time: int) -> None:
        threading.Thread.__init__(self)
        self.threadID: int = threadID
        self.name: str = name
        self.delay_time: int = delay_time
        self.mutex: threading.Lock = threading.Lock()
    
    # Meant to be overridden
    def run(self) -> None:
        pass
