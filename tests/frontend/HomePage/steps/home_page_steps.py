from behave import given, when, then
from BDDCommon.CommonConfigs import locatorsconfig
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig
import pdb


# start of step definitions
@given('I go to the site "{site}"')
def go_to_url(context, site):
    """
    Step definition to go to the specified url.
    :param site:
    :param context:
    """
    # url = urlconfig.URLCONFIG.get(site)
    print("Navigating to the site: {}".format(site))

    webcommon.go_to(context, site)


# ========================================================================================#
@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies the home page title is as expected.
    :param context:
    :param expected_title:
    :return:
    """

    webcommon.assert_page_title(context, expected_title)


# ========================================================================================#
@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    """
    Verifies the current uls is as expected_url
    :param context:
    :param expected_url:
    """

    webcommon.assert_current_url(context, expected_url)


@then(u'the "{nav_bar}" bar should be visible')
def verify_nav_bars_visible(context, nav_bar):
    expected_bars = ['top navigation', 'main navigation', 'options']
    if nav_bar not in expected_bars:
        raise Exception("The passed in nav_bar type is not one of expected."
                        "Actual: {}, Expected in: {}".format(nav_bar, expected_bars))

    locator_info = locatorsconfig.HOME_PAGE_LOCATORS.get(nav_bar)
    locator_type = locator_info['type']
    locator_text = locator_info['locator']

    nav_element = webcommon.find_element(context, locator_type, locator_text)

    webcommon.assert_element_visible(nav_element)


