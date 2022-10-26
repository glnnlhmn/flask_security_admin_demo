# demo_config
"""demo_config
file to maintain all the flask settings for the application
"""

DEBUG = True

# Generate a nice key using secrets.token_urlsafe()
SECRET_KEY = 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw'


# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
SECURITY_PASSWORD_SALT = '146585145368132386173505678016728509634'
