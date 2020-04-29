from shamir_secret_sharing import ShamirSecretSharing

SECRET_CODE = 1267
QUANT_PUBLIC_KEYS = 9

sss = ShamirSecretSharing()
# keys = sss.generate_public_keys(SECRET_CODE, QUANT_PUBLIC_KEYS)
# print(keys)

secret_code = sss.get_secret_code('75766068', '37828', '943047988', '816778483', '11268', '21523', '61680883', '466803', '5391892')
print(secret_code)
