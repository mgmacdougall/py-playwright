def click_role(page, role, name):
    page.get_by_role(role, name=name).click()

def fill_role(page, role, name, value):
    page.get_by_role(role, name=name).fill(value)
