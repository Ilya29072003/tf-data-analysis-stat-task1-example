import pandas as pd
import numpy as np


chat_id = 422189248

def solution(x: np.array) -> float:
     epsilon = np.random.normal(-9, 1, size=len(x))
     v_avg = np.mean(x + epsilon)
    return  np.mean((x - v_avg) / 10.0)
