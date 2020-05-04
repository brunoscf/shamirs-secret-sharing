# Shamir's Secret Sharing

The [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) consists in a method wich allows you to divide a secret codes into public keys. You can reconstruct the original code using the correct public keys.

## Installation

Use the command _pipenv sync_ to install all libs.

```bash
pipenv sync
```

## Examples
### How to generate up public keys
```python
from shamirs_secret_sharing import ShamirsSecretSharing as SSS

SECRET_CODE = 2020  # The secret code must be an integer number
QUANT_PUBLIC_KEYS = 5

public_keys = SSS.generate_public_keys(SECRET_CODE, QUANT_PUBLIC_KEYS) #The output of this function is not deterministic
print(public_keys)
```

### How to reconstruct a secret code
```python
from shamirs_secret_sharing import ShamirsSecretSharing as SSS

public_keys = ['63316', '42276', '74421', '12021', '52645']
secret_code = SSS.get_secret_code(public_keys)
print(secret_code)
```
