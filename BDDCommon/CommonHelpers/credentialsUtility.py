#
# import os
#
#
# class CredentialsUtility(object):
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_api_credentials():
#
#         key = os.environ.get('KEY')
#         secret = os.environ.get('SECRET')
#
#         if not key or not secret:
#             raise Exception("The API credentials 'KEY' and 'SECRET' must be in env variable")
#         else:
#             return {'key': key, 'secret': secret}
#
#     @staticmethod
#     def get_db_credentials():
#         db_user = os.environ.get('DB_USER')
#         db_password = os.environ.get('DB_PASSWORD')
#
#         if not db_user or not db_password:
#             raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable")
#         else:
#             return {'db_user': db_user, 'db_password': db_password}
#
#
# if __name__ == '__main__':
#
#     obj = CredentialsUtility()
#     print(obj.get_api_credentials())
#     print(obj.get_db_credentials())
