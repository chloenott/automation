from automation.automation import find_phone_numbers, find_emails

# Verify properly formatted phone number can be found: 123-456-7890
def test_find_phone_number_normal_formatting():
    assert find_phone_numbers("123-456-7890") == {"123-456-7890"}

# Find phone number within text
def test_find_phone_number_within_text():
    assert find_phone_numbers("This is a test 123-456-7890 yes it is") == {"123-456-7890"}

# Find phone number surrounded by text that isn't whitespace
def test_find_phone_number_within_text_no_whitespace():
    assert find_phone_numbers("This is a test123-456-7890yes it is") == {"123-456-7890"}

# Find phone number surrounded by numbers
def test_find_phone_number_within_junk_numbers():
    assert find_phone_numbers("3123-456-78900") == {"123-456-7890"}

# Find number without area code and assume 206
def test_find_phone_number_without_area_code():
    assert find_phone_numbers("456-7890") == {"206-456-7890"}

# Find number without area code with junk formatting and within text
def test_find_phone_number_without_area_code_within_text():
    assert find_phone_numbers("This is a4567890,test") == {"206-456-7890"}

# Find number with area code with junk formatting and within text
def test_find_phone_number_with_area_code_within_text():
    assert find_phone_numbers("This is a(206)-4567890,test") == {"206-456-7890"}

# Find number formatted with whitespace
def test_find_phone_number_formatted_with_whitespace():
    assert find_phone_numbers("This is a(206) 456 78908test") == {"206-456-7890"}

# Finds multiple phone numbers
def test_find_phone_numbers_multiple():
    assert find_phone_numbers("123-456-7890 and another number is 987 6543") == {"123-456-7890", "206-987-6543"}

# Does not pick up numbers that are not phone numbers, such as SSN
def test_find_phone_numbers_fail_on_SSN():
    assert find_phone_numbers("123-45-6788") == set()

# Does not pick up numbers that are not phone numbers, such as SSN, surrounded by text
def test_find_phone_numbers_fail_on_SSN_within_text():
    assert find_phone_numbers("test123-45-6789test") == set()

# Finds email address as standalone
def test_find_email_standalone():
    assert find_emails("me@me.com") == {"me@me.com"}

# Finds email address within text
def test_find_email_standalone():
    assert find_emails("this is within me@me.com some text") == {"me@me.com"}

# Finds email address with different extension
def test_find_email_nonstandard_extension():
    assert find_emails("this is within me@me.email some text") == {"me@me.email"}

# Finds email address with hyphens, underscores, and numbers
def test_find_email_with_hyphen_underscore_numbers():
    assert find_emails("this is within me_e8@m-e2.email some text") == {"me_e8@m-e2.email"}

# Finds email address at end of sentence
def test_find_email_end_of_sentence():
    assert find_emails("this is within me@me.com. some text") == {"me@me.com"}
