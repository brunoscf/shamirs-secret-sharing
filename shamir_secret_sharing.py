import numpy as np
from scipy.interpolate import lagrange


class ShamirSecretSharing:
    def _function(self, x, root, degree):
        return x **degree + root

    def generate_public_keys(self, secret_code, quant_public_keys):
        X = np.random.choice(np.arange(1, 9), size=quant_public_keys-1, replace=False)
        Y = [self._function(x=xi, root=secret_code, degree=quant_public_keys-1) for xi in X]
        
        public_keys = [str(x)+str(y) for x,y in zip(X, Y)]
        return public_keys