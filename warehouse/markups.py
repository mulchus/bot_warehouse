from aiogram import types

# ======= CLIENT BLOCK (START) ==============================================================================
client_start_markup = types.InlineKeyboardMarkup(row_width=2)
client_start_markup_buttons = [
    types.InlineKeyboardButton('Storage conditions (FAQ)', callback_data='faq'),
    types.InlineKeyboardButton('Put things in storage', callback_data='put_things'),
    types.InlineKeyboardButton('My boxes', callback_data='boxes'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
client_start_markup.add(*client_start_markup_buttons)

choose_weight = types.InlineKeyboardMarkup(row_width=3)
choose_weight_buttons = [
    types.InlineKeyboardButton('0-10 kg', callback_data='mass_0_10'),
    types.InlineKeyboardButton('10-25 kg', callback_data='mass_10_25'),
    types.InlineKeyboardButton('25-40 kg', callback_data='mass_25_40'),
    types.InlineKeyboardButton('40-70 kg', callback_data='mass_40_70'),
    types.InlineKeyboardButton('70-100 kg', callback_data='mass_70_100'),
    types.InlineKeyboardButton('100+ kg', callback_data='mass_100'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
choose_weight.add(*choose_weight_buttons)

choose_square = types.InlineKeyboardMarkup(row_width=2)
choose_square_buttons = [
    types.InlineKeyboardButton('0-3 sq.m', callback_data='metr_0_3'),
    types.InlineKeyboardButton('3-7 sq.m', callback_data='metr_3_7'),
    types.InlineKeyboardButton('7-10 sq.m', callback_data='metr_7_10'),
    types.InlineKeyboardButton('10+ sq.m', callback_data='metr_10'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
choose_square.add(*choose_square_buttons)


choose_delivery = types.InlineKeyboardMarkup(row_width=2)
choose_delivery_buttons = [
    types.InlineKeyboardButton('our delivery', callback_data='delivery_yes'),
    types.InlineKeyboardButton('your delivery', callback_data='delivery_no'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
choose_delivery.add(*choose_delivery_buttons)

make_order = types.InlineKeyboardMarkup(row_width=2)
make_order_buttons = [
    types.InlineKeyboardButton('make order', callback_data='order_yes'),
    types.InlineKeyboardButton('no, thanks', callback_data='order_no'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
make_order.add(*make_order_buttons)


accept_personal_data = types.InlineKeyboardMarkup(row_width=2)
accept_personal_data_buttons = [
    types.InlineKeyboardButton('Accept', callback_data='personal_yes'),
    types.InlineKeyboardButton('Decline', callback_data='personal_no'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
accept_personal_data.add(*accept_personal_data_buttons)


manage_order = types.InlineKeyboardMarkup(row_width=2)
manage_order_buttons = [
    types.InlineKeyboardButton('Get access', callback_data='access_order'),
    types.InlineKeyboardButton('Close order', callback_data='close_order'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
manage_order.add(*manage_order_buttons)
# ======= CLIENT BLOCK (END) ===============================================================================

# ======= OWNER BLOCK (START) ===============================================================================
owner_start_markup = types.InlineKeyboardMarkup(row_width=2)
owner_start_markup_buttons = [
    types.InlineKeyboardButton('Clients', callback_data='clients'),
    types.InlineKeyboardButton('Orders', callback_data='orders'),
    types.InlineKeyboardButton('Expired orders', callback_data='exp_orders'),
    types.InlineKeyboardButton('Create QR', callback_data='qr'),
    types.InlineKeyboardButton('Exit', callback_data='exit'),
    ]
owner_start_markup.add(*owner_start_markup_buttons)


# ======= EXIT BLOCK (START) ================================================================================
exit_markup = types.InlineKeyboardMarkup(row_width=1)
exit_markup_btn = types.InlineKeyboardButton('Exit', callback_data='exit')
exit_markup.add(exit_markup_btn)
# ======= EXIT BLOCK (START) ================================================================================
# далее пока все из другого бота - для образца
menu_markup = types.InlineKeyboardMarkup(row_width=2)
menu_markup_fb = types.InlineKeyboardButton('Запрещенные сообщения', callback_data='forbidden_message')
menu_markup_bw = types.InlineKeyboardButton('Плохие слова', callback_data='bad_words')
menu_markup_exit = types.InlineKeyboardButton('Назад', callback_data='exit')
menu_markup.add(menu_markup_fb, menu_markup_bw, menu_markup_exit)

forbidden_message_markup = types.InlineKeyboardMarkup(row_width=2)
forbidden_message_markup_audio = types.InlineKeyboardButton('Аудио', callback_data='audio')
forbidden_message_markup_photo = types.InlineKeyboardButton('Фото', callback_data='photo')
forbidden_message_markup_sticker = types.InlineKeyboardButton('Стикер', callback_data='sticker')
forbidden_message_markup_video = types.InlineKeyboardButton('Видео', callback_data='video')
forbidden_message_markup_video_note = types.InlineKeyboardButton('Видеосообщение', callback_data='video_note')
forbidden_message_markup_voice = types.InlineKeyboardButton('Голос', callback_data='voice')
forbidden_message_markup_document = types.InlineKeyboardButton('Документ', callback_data='document')
forbidden_message_markup_animation = types.InlineKeyboardButton('Анимация(GIF)', callback_data='animation')
forbidden_message_markup_exit = types.InlineKeyboardButton('Назад', callback_data='exit')
forbidden_message_markup.add(forbidden_message_markup_audio, forbidden_message_markup_photo, forbidden_message_markup_sticker,
                forbidden_message_markup_video, forbidden_message_markup_video_note, forbidden_message_markup_voice, forbidden_message_markup_document,
                forbidden_message_markup_animation, forbidden_message_markup_exit)

bad_words_markup = types.InlineKeyboardMarkup(row_width=2)
bad_words_markup_add = types.InlineKeyboardButton('Добавить', callback_data='bad_words_add')
bad_words_markup_del = types.InlineKeyboardButton('Удалить', callback_data='bad_words_del')
bad_words_markup_exit = types.InlineKeyboardButton('Назад', callback_data='exit')
bad_words_markup.add(bad_words_markup_add, bad_words_markup_del, bad_words_markup_exit)

y_n_markup = types.InlineKeyboardMarkup(row_width=2)
y_n_markup_y = types.InlineKeyboardButton('Да', callback_data='yes')
y_n_markup_n = types.InlineKeyboardButton('Нет', callback_data='no')
y_n_markup.add(y_n_markup_y, y_n_markup_n)


# start_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='ПРИВЕТУСЫ')
# start_markup_btn1 = types.KeyboardButton('/start')
# start_markup_btn2 = types.KeyboardButton('/del')
# start_markup.add(start_markup_btn1, start_markup_btn2)
#
# end_markup = types.ReplyKeyboardRemove()

