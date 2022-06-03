
from BDDCommon.CommonHelpers.requestsUtility import RequestsUtility


def list_all_products():
    """
    :return:
    """
    all_products = []
    max_pages = 1000
    page_num = 1
    while page_num < max_pages:
        param = {'per_page': 100, 'page': page_num}
        rs_api = RequestsUtility().get(endpoint='computers', payload=param)
        print("Page number: {}".format(page_num))
        if rs_api:
            page_num += 1
            all_products.extend(rs_api)
        else:
            print("No results on page number {}. End loop of calling products.".format(page_num))
            break
    return all_products


def get_product_by_id(product_id):
    """
    :param product_id:
    :return:
    """

    rs_api = WooRequestsHelper().get(wc_endpoint="computers/{}".format(product_id))

    return rs_api
