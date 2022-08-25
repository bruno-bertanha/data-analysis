from logging import raiseExceptions
import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  arr = np.array(list).reshape(3,3)
  calculations = {}

  for key, method in {
    'mean': 'mean',
    'variance': 'var',
    'standard deviation': 'std',
    'max': 'max',
    'min': 'min', 
    'sum': 'sum'
  }.items():
    calculations[key] = [
      getattr(arr, method)(axis=0).tolist(),
      getattr(arr, method)(axis=1).tolist(),
      getattr(arr, method)()
    ]

  return calculations