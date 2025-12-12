def assert_text_contains(actual, expected):
    assert expected.lower() in actual.lower(), (
        f"Expected '{expected}' to be inside '{actual}'"
    )


def assert_element_visible(element):
    assert element.is_displayed(), "Element is not visible on the page"


def assert_url_contains(driver, text):
    assert text in driver.current_url, (
        f"URL does not contain '{text}'. Current: {driver.current_url}"
    )


def assert_css_class_contains(element, class_name):
    classes = element.get_attribute("class").split()
    assert class_name in classes, (
        f"Expected CSS class '{class_name}', got {classes}"
    )


def assert_element_text(element, expected):
    actual = element.text.strip()
    assert actual == expected, (
        f"Expected text '{expected}', got '{actual}'"
    )