from shamir_secret_sharing import ShamirSecretSharing

SECRET_CODE = 255
QUANT_PUBLIC_KEYS = 5

sss = ShamirSecretSharing()
keys = sss.generate_public_keys(SECRET_CODE, QUANT_PUBLIC_KEYS)
print(keys)