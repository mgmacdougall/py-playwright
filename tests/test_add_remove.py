from factory.page_factory import PageFactory

def test_add_remove_loads(page):
    app = PageFactory(page)

    app.add_remove.goto_add_remove_page()
    app.add_remove.click_add_element()

    assert app.add_remove.get_element_count() == 1

def test_add_remove_header(page):
    app = PageFactory(page)

    app.add_remove.goto_add_remove_page()

    assert app.add_remove.get_page_header() == "Add/Remove Elements"

# def test_add_remove_multiple_elements(page):
#     app = PageFactory(page)

#     app.add_remove.goto_add_remove_page()

#     for _ in range(5):
#         app.add_remove.click_add_element()

#     assert app.add_remove.get_element_count() == 5

#     for _ in range(5):
#         app.add_remove.get_element_count()
#         app.add_remove.remove_element_by_place(_)
    
#     assert app.add_remove.get_element_count_after_removal() == 0


def test_add_remove_remove_nonexistent_element(page):
    app = PageFactory(page)

    app.add_remove.goto_add_remove_page()

    app.add_remove.click_add_element()

    app.add_remove.remove_element_by_place(0)  # Attempt to remove an element that doesn't exist
    # console.log("Attempted to remove a non-existent element.")
    assert app.add_remove.get_element_count_after_removal() == 0 # Should still be 1 since the second element doesn't exist