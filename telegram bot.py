import telebot
import keyboards
import  lesson_2.planets


bot = telebot.TeleBot('995341757:AAEqdUJXkGIxmM0jUAnL_jU1MmkJRZCh7o0')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты готов(а) узнать цену на страхования?)',reply_markup=keyboards.keyboard1)

@bot.message_handler(commands=['planet'])
def start_to_planet(message_1):
    bot.send_message(message_1.chat.id,'Привет, выбери планету из списка',reply_markup=keyboards.keyboard9)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Отлично!!! Выбери что именно тебе интересно', reply_markup=keyboards.keyboard2)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Жаль, возвращайся, нам будет тебя не хватать')
    elif message.text.lower() == 'выезд за границу':
        bot.send_message(message.chat.id, 'Как сказал Эмиль Золя «Ничто так не развивает ум, как путешествие». Выбери, что именно тебя интересует:', reply_markup=keyboards.keyboard3)
    elif message.text.lower() == 'я готов':
        bot.send_message(message.chat.id, 'В какой континент вы отправляетесь?', reply_markup=keyboards.keyboard4)
    elif message.text.lower() == 'жилье':
        bot.send_message(message.chat.id, 'Какой тип имущества вы хотите застраховать?', reply_markup=keyboards.keyboard5)
    elif message.text.lower() == 'здоровье':
        bot.send_message(message.chat.id, 'Какой вид страхования вам подходит?', reply_markup=keyboards.keyboard8)
    elif message.text.lower() == 'на главную':
        bot.send_message(message.chat.id, 'Давай заново подумаем, что тебе будет интересно', reply_markup=keyboards.keyboard2)
    elif message.text.lower() == 'страхования путешественников':
        bot.send_message(message.chat.id, 'Полис защитит и любознательного путешественника, и специалиста в ответственной командировке. Если что-то пойдет не по плану, в любой точке мира вы получите помощь на родном языке. Перейди по ссылке и узнаешь сколько стоит застрахованное путешествие: https://www.soglasie.ru/puteshestviya/kalkulyator-strahovaniya-vyezjayushih-za-rubej/#/programs', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'зеленая карта':
        bot.send_message(message.chat.id, 'Международный полис «Зеленая карта» (Green Card) позволит чувствовать себя в путешествии за границей так же комфортно, как и на родных дорогах. Перейди по ссылке и узнаешь сколько стоит застрахованное путешествие: https://www.soglasie.ru/avto/kalkulyator-zelenaya-karta/#/options', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'авто':
        bot.send_message(message.chat.id, 'Какой вид страхования авто вас интересует?', reply_markup=keyboards.keyboard7)
    elif message.text.lower() == 'осаго':
        bot.send_message(message.chat.id, 'Полис ОСАГО защитит вашу ответственность, если будет причинен ущерб жизни, здоровью или имуществу других участников дорожного движения. Перейди по ссылке и узнаешь сколько стоит застраховать авто: https://www.soglasie.ru/avto/kalkulyator-eosago/#/auto', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'каско':
        bot.send_message(message.chat.id, 'Страхование автомобилей с учетом ваших индивидуальных пожеланий. Перейди по ссылке и узнаешь сколько стоит застраховать авто: https://www.soglasie.ru/avto/kalkulyator-kasko/#/auto ', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'квартира':
        bot.send_message(message.chat.id, 'Страхование квартиры – простой и надежный способ уберечь себя и своих близких от финансовых потерь в случае непредвиденных обстоятельств! Стоимость страхования - от 250 руб. в месяц!. Перейди по ссылке и оформи полис: https://www.soglasie.ru/nedvijimost/kalkulyator-strahovaniya-kvartiry/#/options ', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'дом':
        bot.send_message(message.chat.id, 'Комплексное страхование каменных и деревянных домов, бань, движимого имущества, хозяйственных построек и гражданской ответственности перед третьими лицами от 317 рублей в месяц. Перейди по ссылке и оформи полис: https://www.soglasie.ru/nedvijimost/house/#/options ', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'гражданская ответсвенность':
        bot.send_message(message.chat.id, 'Защита вашего бюджета от расходов за причинение вреда имуществу, жизни и здоровью соседей при эксплуатации квартиры / дома. Перейди по ссылке и узнаешь сколько стоит застраховать авто: https://www.soglasie.ru/nedvijimost/kalkulyator-grajdanskoj-otvetstvennosti/#/options ', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'антиклещ':
        bot.send_message(message.chat.id, 'Организация высококвалифицированной медицинской помощи при укусе клеща на всей территории России. Перейди по ссылке и оформи полис: https://www.soglasie.ru/zdorovje/kalkulyator-antiklestch/#/insured ', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'школьная пора':
        bot.send_message(message.chat.id, 'Страховая компания "Согласие" предлагает застраховать своих детей-школьников от несчастных случаев. Детские годы жизни практически всегда сопряжены с риском получения разнообразных травм. В силу того, что дети не обладают большим жизненным опытом, но зато чрезвычайно активны, травмы у них случаются довольно часто. Перейди по ссылке и оформи полис на своего ребенка: https://www.soglasie.ru/zdorovje/kalkulyator-school-time/#/options ', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'мультиспортсмен':
        bot.send_message(message.chat.id, '«Коробочный» страховой продукт для клиентов, которые покупают страховой полис на время участия в спортивном мероприятии (соревновании, чемпионате, первенстве, спортивных играх). Перейди по ссылке и оформи полис спортсмена: https://www.soglasie.ru/zdorovje/kalkulyator-multisportsmen/#/options', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'марс':
        ii = lesson_2.planets.place('Mars')
        bot.send_message(message.chat.id, f'Местоположение для данной планеты : {ii}', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'венера':
        ii = lesson_2.planets.place('Venus')
        bot.send_message(message.chat.id, f'Местоположение для данной планеты : {ii}', reply_markup=keyboards.keyboard6)
    elif message.text.lower() == 'плутон':
        ii = lesson_2.planets.place('Pluto')
        bot.send_message(message.chat.id, f'Местоположение для данной планеты : {ii}', reply_markup=keyboards.keyboard6)

bot.polling()
