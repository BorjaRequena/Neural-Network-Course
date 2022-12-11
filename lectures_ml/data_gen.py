# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/lib_nbs/00_data_gen.ipynb.

# %% auto 0
__all__ = ['line', 'noisy_line']

# %% ../nbs/lib_nbs/00_data_gen.ipynb 2
import numpy as np

# %% ../nbs/lib_nbs/00_data_gen.ipynb 3
def line(x:np.ndarray,
         a=1.0,#Slope
         b=0.5,#Intercept
         interval=[-10.,10.],#Interval for x.
         noise=[0,1E-5],# Noise [$\mu$,$\sigma$] with mean $\mu$ and standard deviation $\sigma$
         nsamples=100# Number of samples
        )-> np.ndarray: # the array $y=ax+b$
    '''Create a dataset of nsamples in the interval following the linear regression $y=a x+b$.'''
    return a*x+b

# %% ../nbs/lib_nbs/00_data_gen.ipynb 4
def noisy_line(a=1.0,#Slope
               b=0.5,#Intercept
               interval=[-10.,10.],#Interval for x.
               noise=[0,1E-5],# Noise [$\mu$,$\sigma$] with mean $\mu$ and standard deviation $\sigma$
               nsamples=100# Number of samples
              ):
    '''
    Create a dataset of nsamples in the interval following the linear regression $y=a x+b$ and adds a gaussian noise on y.
    
    Returns
    -------
    tuple
        - a random x vector in the interval of size nsamples
        - the noisy vector following $y= ax+b$
    '''
    x = np.random.uniform(low=interval[0], high=interval[1], size=nsamples)
    mu, sigma = noise
    vnoise = np.random.normal(loc=mu, scale=sigma, size=nsamples)
    return x, a*x+b+vnoise