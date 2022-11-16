from utils import get_email_list, get_valid_email, get_result

# iter with valid emails
data = (item if get_valid_email(item) else print(f'Строка "{item}" не является ссылкой') for item in get_email_list())

# remove all is None values
data = filter(lambda item: item, data)

# take CLI result
print(get_result(data))
