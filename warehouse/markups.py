from aiogram import types


client_start_markup = types.InlineKeyboardMarkup(row_width=2)
client_start_markup_buttons = [
    types.InlineKeyboardButton('Storage condit. (FAQ)', callback_data='faq'),
    types.InlineKeyboardButton('Put things in storage', callback_data='put_things'),
    types.InlineKeyboardButton('My boxes', callback_data='boxes'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
client_start_markup.add(*client_start_markup_buttons)

exit_markup = types.InlineKeyboardMarkup(row_width=1)
exit_markup_button = types.InlineKeyboardButton('Exit', callback_data='exit')
exit_markup.add(exit_markup_button)

client_put_markup = types.InlineKeyboardMarkup(row_width=1)
client_put_markup_buttons = [
    types.InlineKeyboardButton('Addresses of receiving items', callback_data='receiving_addresses'),
    types.InlineKeyboardButton('Order free shipping', callback_data='free_shipping'),
    types.InlineKeyboardButton('I\'ll bring it myself', callback_data='bring_myself'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
client_put_markup.add(*client_put_markup_buttons)

client_things_info_markup = types.InlineKeyboardMarkup(row_width=1)
client_things_info_markup_buttons = [
    types.InlineKeyboardButton('Specify the weight of things', callback_data='things_weight'),
    types.InlineKeyboardButton('Specify the amount of things', callback_data='things_amount'),
    types.InlineKeyboardButton('Specify the storage period', callback_data='storage_period'),
    types.InlineKeyboardButton('Continue without specifying the above', callback_data='without_specifying'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
client_things_info_markup.add(*client_things_info_markup_buttons)

client_things_weight_markup = types.InlineKeyboardMarkup(row_width=3)
client_things_weight_markup_buttons = [
    types.InlineKeyboardButton('<10kg', callback_data='less_10'),
    types.InlineKeyboardButton('10-24kg', callback_data='10-24'),
    types.InlineKeyboardButton('25-39kg', callback_data='25-39'),
    types.InlineKeyboardButton('40-69kg', callback_data='40-69'),
    types.InlineKeyboardButton('70-99kg', callback_data='70-99'),
    types.InlineKeyboardButton('>=100', callback_data='100_more'),
    ]
client_things_weight_markup.add(*client_things_weight_markup_buttons)

client_things_amount_markup = types.InlineKeyboardMarkup(row_width=4)
client_things_amount_markup_buttons = [
    types.InlineKeyboardButton('<3m3', callback_data='less_3'),
    types.InlineKeyboardButton('3-6m3', callback_data='3-6'),
    types.InlineKeyboardButton('7-10m3', callback_data='7-10'),
    types.InlineKeyboardButton('>=10m3', callback_data='10_more'),
    ]
client_things_amount_markup.add(*client_things_amount_markup_buttons)

client_y_n_markup = types.InlineKeyboardMarkup(row_width=2)
client_y_n_markup_buttons = [
    types.InlineKeyboardButton('Yes', callback_data='yes'),
    types.InlineKeyboardButton('NO', callback_data='no'),
    ]
client_y_n_markup.add(client_y_n_markup_buttons)

client_storage_action_markup = types.InlineKeyboardMarkup(row_width=1)
client_storage_action_markup_buttons = [
    types.InlineKeyboardButton('Completing rental', callback_data='completing_rental'),
    types.InlineKeyboardButton('Pick up and return later', callback_data='take_return'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
client_storage_action_markup.add(client_storage_action_markup_buttons)

owner_start_markup = types.InlineKeyboardMarkup(row_width=2)
owner_start_markup_buttons = [
    types.InlineKeyboardButton('Active orders', callback_data='active_orders'),
    types.InlineKeyboardButton('Overdue orders', callback_data='overdue_orders'),
    types.InlineKeyboardButton('List of clients', callback_data='clients_list'),
    types.InlineKeyboardButton('Delivery required', callback_data='delivery_required'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
owner_start_markup.add(owner_start_markup_buttons)


# далее пока все из другого бота - для образца
# start_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='ПРИВЕТУСЫ')
# start_markup_btn1 = types.KeyboardButton('/start')
# start_markup_btn2 = types.KeyboardButton('/del')
# start_markup.add(start_markup_btn1, start_markup_btn2)
#
# end_markup = types.ReplyKeyboardRemove()

