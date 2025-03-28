from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('shi', 'quan')
    full_name = "shi quan"
    assert formatted_name == full_name.title()

def test_first_middle_last_name():
    formatted_name = get_formatted_name('shi', 'quan', 'yu')
    full_name = "shi yu quan"
    assert formatted_name == full_name.title()

    