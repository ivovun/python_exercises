# Имеется таблица пользователей следующей структуры:
#
#     id - целочисленный первичный ключ
#     последовательной нумерации
#     username - логин пользователя
#     city_id - город проживания пользователя
#
# Необходимо выбрать города, в которых
# проживает не менее N пользователей.
# Написать запрос на SQL
#  проверить можно тут
# https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

SELECT City, count(ContactName)
FROM Customers
group by  City
having count(ContactName) >= 2  ;


# select city_id, count(username) from myTable group by  city_id having count(username) >= N;
