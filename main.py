from shamirs_secret_sharing import ShamirsSecretSharing as SSS

# EXAMPLE

SECRET_CODE = 2020  # The secret code must be a integer number
QUANT_PUBLIC_KEYS = 5

keys = SSS.generate_public_keys(SECRET_CODE, QUANT_PUBLIC_KEYS)
print(keys)


# Try retrieving the secret code

# public_keys = [# <- put here the result of the above example
# secret_code = SSS.get_secret_code(public_keys)
# print(secret_code)
