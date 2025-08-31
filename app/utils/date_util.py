import time

def current_epoch_millis() -> int:
    """Returns the current timestamp in epoch milliseconds"""
    return int(time.time() * 1000)