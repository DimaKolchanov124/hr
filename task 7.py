# 7.1
# month = int(input('Ввидете номер месяца:'))

# if month in [12, 1, 2]:
#    print('зима')
# elif month in [3, 4, 5]:
#   print('весна')
# elif month in [6, 7, 8]:
#    print('лето')
# elif month in [9, 10, 11]:
#    print('осень')
# else:
#    print('некоректный номер месяца')

# 7.2
# is_logged_in = True
# has_item_in_cart = True
# has_shipping_address = True
# has_order = True
# if is_logged_in and has_item_in_cart and has_shipping_address:
#     print('все критерии для заказа выполнены, ')
# else:
#     print('не все критерии выполнены')
#
# if is_logged_in and has_item_in_cart and has_shipping_address:
#     is_first_order = False
#     min_purchase = 1000
#     total_purchase = 1500
#     if has_order and (is_first_order or total_purchase >= min_purchase):
#         print('вы получаете скидку')
#     else:
#          print('вы не получаете скидку')
# else:
#     print('!')

# 7.3
# number = int(input('ввидите число: '))
# if number in [7, 13, 21]:
#     print('счатливое число!')
# elif number in range(1, 101):
#     print('число в указанном диапазоне')
# else:
#     ('не повезло!')