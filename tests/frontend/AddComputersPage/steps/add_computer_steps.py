from behave import *
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs.locatorsconfig import *
import pdb


@When("I click on the '{btn_name}' button")
def i_click_on_the_add_computer_button(context, btn_name):
    """
    :param context:
    :param btn_name:
    :return:
    """
    if btn_name.lower() == 'add new computer':
        add_computer_btn_locator_type = HOME_PAGE_LOCATORS['add a new computer']['type']
        add_computer_btn_locator_string = HOME_PAGE_LOCATORS['add a new computer']['locator']
    else:
        raise Exception("Not implemented")

    webcommon.click(context, add_computer_btn_locator_type, add_computer_btn_locator_string)


@when(u'I type "{computer}" into username of computer name form')
def type_computer_name_into_the_form(context, computer):
    """
    :param computer:
    :param context:
    :return:
    """
    computer_locator_type = ADD_COMPUTERS['computer name']['type']
    computer_locator_string = ADD_COMPUTERS['computer name']['locator']

    webcommon.type_into_element(context, computer, computer_locator_type, computer_locator_string)


@step("Then I click on the '{btn_name}' button")
def i_click_on_the_login_button(context, btn_name):
    """

    :param context:
    :param btn_name:
    :return:
    """
    if btn_name.lower() == 'create this computer':
        create_computer_btn_locator_type = ADD_COMPUTERS['create computer bnt']['type']
        create_computer_btn_locator_string = ADD_COMPUTERS['create computer bnt']['locator']
    else:
        raise Exception("Not implemented")

    webcommon.click(context, create_computer_btn_locator_type, create_computer_btn_locator_string)


@then("New computer should be created")
def user_should_be_logged_in(context):
    """
    :param context:
    :return:
    """

    nav_bar_type = HOME_PAGE_LOCATORS['confirm new computer added']['type']
    nav_bar_text = HOME_PAGE_LOCATORS['confirm new computer added']['locator']

    webcommon.assert_element_visible(context, nav_bar_type, nav_bar_text)
