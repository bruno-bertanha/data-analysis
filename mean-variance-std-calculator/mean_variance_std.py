from logging import raiseExceptions
import numpy as np

def calculate(list):
    try:
        mx = np.array(list).reshape((3,3))
        calculations = {
            'mean': [[mx[:,0].mean() , mx[:,1].mean(), mx[:,2].mean()], [mx[0,:].mean(), mx[1,:].mean(), mx[2,:].mean()], mx.mean()],
            'variance': [[mx[:,0].var(), mx[:,1].var(), mx[:,2].var()], [mx[0,:].var(), mx[1,].var(), mx[2,:].var()], mx.var()],
            'standard deviation': [[mx[:,0].std(), mx[:,1].std(), mx[:,2].std()], [mx[0,:].std(), mx[1,:].std(), mx[2,:].std()], mx.std()],
            'max': [[mx[:,0].max(), mx[:,1].max(), mx[:,2].max()], [mx[0,:].max(), mx[1,:].max(), mx[2,:].max()], mx.max()],
            'min': [[mx[:,0].min(), mx[:,1].min(), mx[:,2].min()], [mx[0,:].min(), mx[1,:].min(), mx[2,:].min()], mx.min()],
            'sum': [[mx[:,0].sum(), mx[:,1].sum(), mx[:,2].sum()], [mx[0,:].sum(), mx[1,:].sum(), mx[2,:].sum()], mx.sum()]
        }
    except ValueError:
        print(f'List must contain nine numbers.')

    return calculations