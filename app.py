from queries import *

init()
create_book("Евгений Онегин")
create_book("Война и Мир")
result = get_all_books()
print(result)