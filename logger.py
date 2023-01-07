import numpy as np

from typing import Dict, List

def calcuate_average_timing(logger: Dict[str, List[float]]):
    for check in logger.keys():
        print(f"Check \'{check}\' average elapse - {np.mean(logger[check]) * 1000:.5}ms")
        print(f"  Num of array - {len(logger[check])}")
        print(f"  Total - {np.sum(logger[check]):.5}s")
