import telebot

keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard1.row('Да', 'Нет')

keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard2.row('Выезд за границу', 'Авто', 'Жилье', 'Здоровье')

keyboard3 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard3.row('Страхования путешественников', 'Зеленая карта', 'На главную')

keyboard4 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard4.row('Азия', 'Европа', 'Северная Америка', 'Южная Америка','Африка', 'Австралия','На главную')

keyboard5 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard5.row('Квартира', 'Дом', 'Гражданская ответсвенность', 'На главную')

keyboard6 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard6.row('На главную')

keyboard7 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard7.row('ОСАГО','КАСКО','Зеленая карта','На главную')

keyboard8 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard8.row('Антиклещ','Мультиспортсмен','Школьная пора','На главную')

keyboard9 = telebot.types.ReplyKeyboardMarkup(row_width=10)
keyboard9.row('Марс','Венера','Плутон','На главную')
