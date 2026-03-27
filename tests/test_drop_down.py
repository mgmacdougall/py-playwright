from factory.page_factory import PageFactory

def test_drop_down_loads(page):
    app = PageFactory(page)

    # TODO: Add navigation step
    assert app.drop_down.is_loaded()


def test_drop_down_header(page):
    app = PageFactory(page)
    app.drop_down.goto_drop_down_page()

    assert app.drop_down.get_page_header() == "Dropdown List"


def test_drop_down_options(page):
    app = PageFactory(page)
    app.drop_down.goto_drop_down_page()

    options = app.drop_down.get_all_options()
    assert options == ["Please select an option", "Option 1", "Option 2"]


def test_drop_down_select_option_1(page):
    app = PageFactory(page)
    app.drop_down.goto_drop_down_page()

    app.drop_down.select_option_by_text("Option 1")
    selected_option = app.page.locator("select#dropdown").input_value()
    assert selected_option == "1"  # Assuming the value for Option 1 is "1"

def test_drop_down_select_option_2(page):
    app = PageFactory(page)
    app.drop_down.goto_drop_down_page()

    app.drop_down.select_option_by_text("Option 2")
    selected_option = app.page.locator("select#dropdown").input_value()
    assert selected_option == "2"  # Assuming the value for Option 2 is "2"

def test_drop_down_select_invalid_option(page):
    app = PageFactory(page)
    app.drop_down.goto_drop_down_page()

    try:
        app.drop_down.select_option_by_text("Invalid Option")
        selected_option = app.page.locator("select#dropdown").input_value()
        assert selected_option == ""  # Assuming no option is selected for invalid input
    except Exception as e:
        assert "No option with label 'Invalid Option' found" in str(e)      