# from BDDCommon.CommonHelpers.dbUtility import DBUtility
# import random
#
#
# class ComputersDAO(object):
#
#     def __init__(self):
#         self.db_heler = DBHelpers()
#
#     def get_app_computers_from_db(self):
#
#         sql = "SELECT * FROM local.wp_posts WHERE post_type = 'computer';"
#         rs_sql = self.db_heler.execute_select(sql)
#         return rs_sql
#
#     def get_random_computers_from_db(self, qty):
#         """
#
#         """
#
#         sql = "SELECT * FROM local.wp_posts WHERE post_type = 'computer' ORDER BY id DESC LIMIT 5000;"
#         rs_sql = self.db_heler.execute_select(sql)
#
#         return random.sample(rs_sql, int(qty))