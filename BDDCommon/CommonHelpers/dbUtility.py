# import os
# import logging as logger
# from BDDCommon.CommonHelpers.credentialsUtility import CredentialsUtility
# from BDDCommon.CommonConfigs.urlconfig import DB_HOST
# import sys
# import pymysql
#
#
# class DBUtility(object):
#
#     def __init__(self):
#         self.creds = CredentialsUtility().get_db_credentials()
#
#         self.machine = os.environ.get('MACHINE')
#         assert self.machine, f"Environment variable 'MACHINE' must be set."
#
#         # setting the host because we can't run Docker locally
#         self.my_host = os.environ.get('MY_HOST')
#         assert self.my_host, f"Environment variable 'MY_HOST' must be set."
#
#         if self.machine == 'docker' and self.my_host == 'local':
#             raise Exception(f"Can not run test in docker if WP_HOST=local")
#
#         self.env = os.environ.get('ENV', 'test')
#
#         self.host = DB_HOST[self.machine][self.env]['host']
#         self.port = DB_HOST[self.machine][self.env]['port']
#         self.database = DB_HOST[self.machine][self.env]['database']
#
#     def create_connection(self):
#
#         if self.my_host == 'local':
#             connection = pymysql.connect(host=self.host, user=self.creds['db_user'], database=self.database,
#                                          password=self.creds['db_password'], port=self.port
#                                          )
#         elif self.my_host == 'ampps':
#             connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
#                                          password=self.creds['db_password'],
#                                          port=self.port)
#         else:
#             raise Exception("Unknown WP_HOST.")
#
#         return connection
#
#     def execute_select(self, sql):
#
#         conn = self.create_connection()
#
#         try:
#             logger.debug(f"Executing: {sql}")
#             cur = conn.cursor(pymysql.cursors.DictCursor)
#             cur.execute(sql)
#             rs_dict = cur.fetchall()
#             cur.close()
#         except Exception as e:
#             raise Exception(f"Failed running sql: {sql} \n  Error: {str(e)}")
#         finally:
#             conn.close()
#         return rs_dict
#
#     def execute_sql(self, sql):
#         pass
