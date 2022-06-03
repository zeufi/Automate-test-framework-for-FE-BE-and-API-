ADD_COMPUTERS = {
    'computer name': {'type': 'id', 'locator': 'name'},
    'create computer bnt': {'type': 'xpath', 'locator': '//body/section[@id="main"]/form[1]/div[1]/input[1]'},
}

HOME_PAGE_LOCATORS = {
    'main navigation': {'type': 'id', 'locator': 'main'},
    'top navigation': {'type': 'xpath', 'locator': '//header/h1[1]'},
    'options': {'type': 'xpath', 'locator': '//body/section[@id="main"]/div[@id="actions"]/form[1]'},
    'add a new computer': {'type': 'id', 'locator': 'add'},
    'confirm new computer added': {'type': 'xpath', 'locator': '//body/section[@id="main"]/div[1]'}
}
