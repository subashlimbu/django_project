import os

db_user = os.environ.get['EMAIL_USER']
db_password = os.environ.get['EMAIL_PASS']
print(db_user)
print(db_password)
# print(f'{username} home directory is {home_dir}')

# db_pass = os.environ.get('EMAIL_PASS')

# print(os.environ)
# print(db_pass)
