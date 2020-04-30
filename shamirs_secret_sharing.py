from typing import List

import numpy as np
from scipy.interpolate import lagrange


class ShamirsSecretSharing:
    @classmethod
    def _function(self, x: int, root: int, degree: int) -> int:
        """
        Returns the math function below
         * The variable ´root´ is the ´secret_code´
         * 'degree´ is equals to ´quant_public_keys - 1´
        """
        return x ** degree + root

    @classmethod
    def generate_public_keys(self, secret_code: int, quant_public_keys: int) -> List[str]:
        """
        Returns the public keys
         * This function can generate up to 9 public keys
         * The first character of either key corresponds to the position X and the remaining characters are the position Y of a point
         * The results are not deterministic
        """
        X = np.random.choice(np.arange(1, 10), size=quant_public_keys, replace=False)
        Y = [self._function(x=xi, root=secret_code, degree=quant_public_keys - 1) for xi in X]

        public_keys = [str(x) + str(y) for x, y in zip(X, Y)]
        return public_keys

    @classmethod
    def get_secret_code(self, keys: List[str]) -> int:
        """
        Returns the secret code recovered using the keys passed to this function
         * This function uses the Langrange interpollation method to reconstruct the original polynomial function
         * The result corresponds to the reconstructed function applied to zero
        """
        keys = [str(key) for key in keys]
        X, Y = [], []
        for key in keys:
            X.append(int(key[:1]))
            Y.append(int(key[1:]))

        poly_function = lagrange(X, Y)
        return int(round(poly_function(0), 0))
