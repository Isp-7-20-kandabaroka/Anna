import telebot

from telebot import types
bot = telebot.TeleBot('5634364361:AAEh9WhXcj2cPOWiJfmafyo-DDWmj8fJZU4')
ROBOKASSA_LOGIN = 'Ваш_логин'
ROBOKASSA_PASSWORD_1 = 'Ваш_пароль_1'
ROBOKASSA_PASSWORD_2 = 'Ваш_пароль_2'
ROBOKASSA_TEST_MODE = True
@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.chat.id


    markup = types.InlineKeyboardMarkup()
    forward_button = types.InlineKeyboardButton("Вперед", callback_data='forward')
    markup.add(forward_button)


    welcome_message = """
    👋Добро пожаловать в Мастерскую писателя, где всё легко! 

Пожалуйста, располагайтесь и чувствуйте себя как дома. Меня зовут ТАН – я маленький, гостеприимный бот известного писателя, автора более 60 книг, переведенных на английский, корейский, китайский и словацкий, Анны Никольской. Я буду держать вас в курсе новостей нашей Мастерской и напоминать о важных событиях курса. 

А чтобы я не потерялся, пожалуйста, закрепите меня и включите уведомления. Надеюсь, вы готовы, потому что мы стартуем прямо сейчас!
    """


    bot.send_message(user_id, welcome_message, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'forward')
def forward_button_handler(call):
    user_id = call.message.chat.id


    markup = types.InlineKeyboardMarkup()
    forward_button = types.InlineKeyboardButton("Вперед", callback_data='forward1')  # заменяем callback_data на 'forward1'
    markup.add(forward_button)


    forward_message = """
   ТАН обещал – ТАН сделал. Наша программа на ближайшие дни такая: 

1. Теория: видео-урок от Анны Никольской «Процесс создания «вкусного» рассказа».

2. Практика-1: Пишем рассказ по нашей методике. За выполненное задание получаем подарок – 200 упражнений для ежедневного креативного письма. 

3. Практика-2: Саморедактура. Чек-лист писательских ошибок.

4. Двухнедельный курс Мастерская писателя (2 - 15 октября). Программа. Кейсы. Отзывы.
    """




    bot.send_message(user_id, forward_message)
    image_path = r'photos/photo_2023-09-23_14-50-14.jpg'
    with open(image_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'forward1')
def forward_button_handler2(call):
    user_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    forward_button3 = types.InlineKeyboardButton("Получить первое задание",
                                                callback_data='forward2')
    markup.add(forward_button3)
    forward_message1 = """
    Посмотрите видео урок от Анны Никольской «Процесс создания «вкусного» рассказа»

    https://youtu.be/f2W_s9MtVpw

    После просмотра сможете получить первое задание
    """

    bot.send_message(user_id, forward_message1,reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'forward2')
def forward_button_handler2(call):
    user_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    forward_button4 = types.InlineKeyboardButton("Задание выполнено",
                                                 callback_data='forward3')
    markup.add(forward_button4)
    forward_message3 = """
   Итак, наше творческое задание: Напишем рассказ <b>«Яркий момент из моего детства». </b>

Закройте глаза и представьте себя в детстве. 

Сколько вам сейчас лет? Не вспомните это, а именно окунитесь в один. Конкретный. Момент. Прямо сейчас. 

Вы – ребенок. Где вы? С кем вы? Что находится рядом с вами? Что вы чувствуете прямо сейчас? Что видите вокруг? А слышите? 

Побудьте в этом состоянии какое-то время, погуляйте в нем, потрогайте предметы, понюхайте цветы, поразглядывайте детали интерьера, поговорите с окружающими вас людьми (или самим собой), погрузитесь в свои ОЩУЩЕНИЯ от этого момента. 

Хорошо. А теперь рассказывайте. 
Говорите обычной разговорной речью, словно беседуете с близком человеком вечером, на кухне, за чашкой чая. 

Для точной передачи используйте все пять чувств (зрение, слух, вкус, обоняние, осязание) + шестое (ощущение того, чего нет, прямо здесь и сейчас). Поделитесь ими с читателем так, чтобы он ухватил ваше состояние, настроение, атмосферу происходящего и соединился с вами через текст не только мыслями, но и сердцем. Почувствовал вас. 

Важно: точность, тонкость ощущений, подробность и тщательность в описании деталей. Объем текста - до 2000 знаков. На выполнение задания – 24 часа, полетели!
    """

    bot.send_message(user_id, forward_message3,reply_markup=markup,parse_mode='HTML')
@bot.callback_query_handler(func=lambda call: call.data == 'forward3')
def forward_button_handler2(call):
    user_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    forward_button4 = types.InlineKeyboardButton("Далее",
                                                 callback_data='forward4')
    markup.add(forward_button4)
    forward_message4 = """
    Отлично! Благодарю за выполнение письменного задания! Надеюсь, Вы получили удовольствие, выполняя его, ведь это в творчестве - самое важное. А теперь пришло время узнать о самых популярных писательских ошибках, чтобы их не совершать.  Внимательно ознакомьтесь с нашим чек-листом и сделайте саморедактуру выполненного письменного задания. 

    Предварительно не забудьте "отлежать" текст хотя бы пару часов, чтобы посмотреть на него свежим взглядом редактора. 😊
    
    """
    forward_message5 = """
    <b>Чек-лист писательских ошибок</b>  (Я рекомендую сохранить в избранное)

<b>• Наречия.</b> Почти всегда наречия лучше заменять более точными глаголами или деталями. Наречия как будто облегчают нам жизнь, но на самом деле, они не дают создать в тексте живой объёмной картинки. 

<b>• Повторы слов и однокоренных слов </b>– самая распространенная наша ошибка. Тщательно вычитывайте такие повторы, желательно вслух. Тогда они становятся очевидней. 

<b>• Свои.</b> В 99% случаев слова «свой», «своя», «свои» и так далее можно опустить без потери смысла. 

<b>• Уменьшительно-ласкательные суффиксы.</b> Соблазн использовать их в текстах для детей очень велик, но мы держимся. Эти суффиксы дают ненужную интонацию сюсюканья и обращения к ребёнку «сверху вниз». 

<b>• Много восклицательных знаков.</b> Всегда достаточного одного знака восклицания. Остальную «восклицательность» передаём через сам текст. 

<b>• Разжёвывание.</b> Читатель считывает больше, чем нам поначалу кажется. Ему нравится быть Шерлоком: разгадывать настроение, мотивы, характеры героев через детали, которые мы даём ему в тексте. Когда мы говорим в лоб: «он расстроился», «она была счастлива», «город был красивым», где-то грустят внутренние шерлоки. 

<b>• Изобилие прилагательных</b> в тексте подобно масляному маслу. Уходите от прилагательных. Всегда лучше выбрать одно, но точное. А вообще тяготейте к глагольным предложениям. Именно глаголом мы «жжем сердца». 

<b>• Много предложений одинаковой длины подряд.</b> Из-за этого текст звучит рублено. Это особенно заметно на коротких предложениях. Чтобы этого избежать и сделать текст живым и мелодичным, чередуем предложения разной длины. 

<b>• Клише.</b> Это расхожие затёртые образы, которые уже не вызывают у читателя никаких эмоций — он просто пробегает мимо. А наша задача — погрузить читателя в наш текст, дать ему почувствовать уникальные запахи, увидеть новые оттенки, уловить необычные звуки. 

<b>• Причастные обороты.</b> Чаще всего они утяжеляют текст — читателю приходится сквозь них продираться. Поэтому стараемся такие моменты перефразировать. 

<b>• Общие слова вместо конкретных деталей.</b> Сравните: «мы купались и дурачились в воде» и «мы брызгались, делали ожерелья из кувшинок и гонялись за голубыми стрекозами». Чувствуете, как картинка сразу становится живой и выпуклой? 

<b>• Не называем эмоции,</b> состояния, мысли персонажа, а передаём их через детали. Вместо «она нервничала» — «она теребила пуговицу пиджака и то и дело поглядывала на дверь». 

<b>• Страдательный залог.</b> Это ещё один утяжелитель текстов. Фраза «яичница была пожарена мужем» звучит Франкенштейном по сравнению с «муж пожарил яичницу», чувствуете? 

<b>• Излишнее нагнетание эмоций.</b> Самые напряжённые моменты в тексте лучше всего описывать сдержано и немного отстранённо, без «заламывание рук». Тогда текст прозвучит гораздо сильнее и искреннее. 

<b>• Слишком длинные предложения.</b> Читатель в них просто заблудится, потеряет мысль и, возможно, даже удовольствие от чтения. А нам этого не надо, мы хотим, чтобы он дошёл с нами до финала текста. Поэтому слишком длинные предложения разбиваем на два или три коротких. 

<b>• «Высокий штиль»,</b> высокопарность вместо простой живой речи в тексте. Даже если вы фанат «Илиады» и стихотворений Державина, в своих текстах лучше говорите с читателем просто — так, будто общаетесь с другом. Искренность располагает к вам читателя. 

<b>• Начинать текст с того, как герой просыпается.</b>Это табу. Так начинаются 90% текстов начинающих авторов. Если вы не хотите среди них затеряться, придумайте такое начало, которое моментально поймает интерес читателя. 

<b>• Морализаторство. </b>Мало кто любит нравоучения. Если вы хотите донести какую-то мысль в тексте, всегда лучше сделать это тонко, через детали. Вы рисуете картинку — а читатель сам делает выводы. Это разговор на равных.
"""
    forward_message6 = """
    После изучения нажмите на кнопку Далее и я пришлю Вам <b>200 упражнений для ежедневного креативного письма</b>
    """
    bot.send_message(user_id, forward_message4)
    bot.send_message(user_id, forward_message5,parse_mode='HTML')
    bot.send_message(user_id, forward_message6,reply_markup=markup,parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: call.data == 'forward4')
def forward_button_handler2(call):
    user_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    forward_button_6 = types.InlineKeyboardButton("Далее",callback_data='forward5')
    markup.add(forward_button_6)

    m = 'Держите 200 упражнений для ежедневного креативного письма (более двух миллионов просмотров ВКонтакте) Сохраняйте в избранное и практикуйте!'
    pdf_path = 'photos/200-upraznenii-pisatelei-spontancev.pdf'
    pdf_file = open(pdf_path, 'rb')
    bot.send_message(user_id, m)
    bot.send_document(user_id, pdf_file,reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'forward5')
def bt(call):
    user_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    f1 = types.InlineKeyboardButton("Отзывы", callback_data='OTT')
    f2 = types.InlineKeyboardButton("Программа курса", callback_data='PGG')
    f3 = types.InlineKeyboardButton("Забронировать место", callback_data='forward8')
    markup.row(f1)
    markup.row(f2,f3)
    welcome_message = (
        "Поздравляю, теперь у Вас есть ценная выжимка знаний для начинающего писателя. "
        "А сейчас можете ознакомиться с программой нового сезона двухнедельной Мастерской писателя (2-15 октября)."
    )


    # Отправка сообщения с клавиатурой
    bot.send_message(user_id, welcome_message,reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'OTT')
def bt1(call):
    user_id = call.message.chat.id

    f2 = types.InlineKeyboardButton("Программа курса", callback_data='PGG')
    f3 = types.InlineKeyboardButton("Забронировать место", callback_data='forward8')
    markup = types.InlineKeyboardMarkup()
    markup.row(f2)
    markup.row(f3)
    otv = """
       <b>Кейсы:</b>
За пять лет работы Мастерской мы выпустили более 5000 авторов, сотни из которых стали профессиональными публикующимися писателями. Вот несколько их историй – вам для вдохновения! 
 
<b>Нюта Яковлева</b>
До Мастерской работала юристом, проверяла документы, сочиняла исковые заявления и ходила с толстыми папками в суд. А после - начала писать книги для детей, отправлять их в издательства и зарабатывать на творчестве. Сейчас у Нюты одна изданная книга и ещё на 7 заключены контракты. 
 
<b>Анастасия Хачатурова </b>
Начала писать художественную прозу, когда её дочке было 2 месяца. После прохождения Мастерской заключила 7 договоров с 5 издательствами и начала получать высокие гонорары. В ближайшее время планируется подписание ещё 3 договоров. Сейчас все Настины рукописи пристроены в издательства. 
 
<b>Этери Заболотная </b>
До Мастерской писала развивающие книги для дошкольников, но хотела писать художественную прозу, не совсем представляя, как это делать. После нашего курса заключила 13 договоров в разных издательствах только на прозу. Ни один текст Этери, написанный в Мастерской, не остался невостребованным. Она получает стабильный заработок от любимого дела. 
 
<b>Веста Васягина</b> 
До курса не было ни одной книги, да и в принципе не писала для детей. После Мастерской опубликовала 5 книг, одна из них "Чудик Нехочуха" стала бестселлером, вышедшим тиражом 35000 экземпляров. Ещё на 11 книг заключены договоры. Благодаря Мастерской сделала писательство хорошим средством заработка. 
 
<b>Ксения Горбунова</b>
До курса писала в стол. Сейчас у нее 12 книг, многие из которых получили престижные литературные награды и денежные призы. Ксения стала лауреатом премий «Большая сказка», Корнея Чуковского и «Новая детская книга». 
 
<b>Анна Маншина</b> 
До курса не писала художественную прозу. После курса стала редактором Мастерской писателя, издающимся автором и начала стабильно зарабатывать литературным ремеслом. На сегодня у Ани 4 книги и еще 4 готовятся к выходу. 
 
И таких историй у нас сотни. Приходите к нам писать свою!
"""
    bot.send_message(user_id,otv,parse_mode='HTML')
    otv1 = """
    *Отзывы наших выпускников*
 
<b>Анастасия Медведева:</b>
Первый день - до слёз. Как слепой котёнок тычусь, ничего понять не могу, а уже надо задания делать, такой темп динамичный! Постепенно влилась и началось… невероятное! Здесь не писать учат, здесь люди меняются. Исцеляются всей душой. Я не знаю, как возможно создать такую атмосферу в чате и на курсе , объединяя совершенно незнакомых людей? Это самый невероятный подход к обучению! Здесь просто невозможно «не сделать», «не раскрыться». О глубоко душевной стороне ТАНа можно говорить бесконечно. Но и много новых знаний я получила. Подача информации особенная, поэтому она не просто врезается в память, материал усваивается всем сердцем. 
 
<b>Наталья Бондаренко:</b>
Полезной информации дают с горкой, на вырост. Я даже не успела всё посмотреть за время курса. Видео от приглашенных экспертов буду еще досматривать. Обратная связь от редакторов очень теплая и нежная, от нее расцветаешь. Отмечают не только то, что можно поправить, но и то, что уже хорошо получается и это очень воодушевляет. 
 
<b>Анна Логвинова:</b>
ТАН-28 был для меня первым. И удачным! Хочу выразить благодарность Ане Никольской за такие насыщенные материалом лекции! Никакой воды, всё чётко по пунктам, по полочкам, с примерами. И за ободряющие голосовые в чате тоже спасибо! Каждое утро они заряжали энергией и верой в себя. Аню Маншину крепко обнимаю за деликатные разборы и рецензии! С такими приятными и обаятельными учителями учиться было сплошным удовольствием. 
 
<b>Татьяна Виноградова:</b>
ТАН- это то место, куда хочется возвращаться. Я вернулась в который раз и не собираюсь закрывать эту дверь. Атмосфера, созданная Анной Никольской и всей командой, вдохновляет и вселяет уверенность. А огромный блок обучающих материалов подробно рассказывает, как стать писателем.
"""
    bot.send_message(user_id,otv1,parse_mode='HTML')
    image_path = r'photos/photo_2023-09-24_13-52-49.jpg'
    with open(image_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'PGG')
def bt2(call):
    user_id = call.message.chat.id
    f2 = types.InlineKeyboardButton("Отзывы", callback_data='OTT')
    f3 = types.InlineKeyboardButton("Забронировать место", callback_data='forward8')
    markup = types.InlineKeyboardMarkup()
    markup.row(f2)
    markup.row(f3)

    proggggg = """
         Мастерская писателя Анны Никольской «Путь лёгкости». 36-й сезон пройдёт с 4 по 17 декабря. 
 
* За 2 недели курса вы получаете всю необходимую информацию и чёткий план действий на пути идея -> черновик -> редактура -> письмо в издательство -> заключение договора -> изданная книга – стабильный заработок на любимом деле. 
* Работа именно с вашими текстами, ответы мастера именно на ваши вопросы. 
* Преподаватель Анна Никольская — известный писатель, автор более 60 книг. 
* Конструктивная и доброжелательная обратная связь от профессиональных редакторов. 
* Вы поймёте, в чём ваши сильные стороны, и почувствуете уверенность в себе-писателе. 
* Курс подходит даже для тех, кто до этого никогда не писал. 
* Не нужно перестраивать жизнь под писательство. Мы учим, как органично встроить писательство в жизнь. 
* Вы экономите годы на пути к первой опубликованной книге и заработку творчеством. 
* Клуб выпускников Мастерской, куда вы попадете после курса, — это сообщество издающихся авторов, площадка для обмена полезной профессиональной информацией и поддержка единомышленников. 
 
На <b>более 1000 книг</b> подписаны договоры с ведущими издательствами России. Это первые книги наших выпускников. 6 из 10 победителей конкурса «Новая книга» издательства «Росмэн» в прошлом году — выпускники Мастерской. На конкурс было прислано 3800 текстов. 
 
<b>Преподаватель А. Никольская</b> — автор учебных программ по писательскому мастерству. Обладатель золотой медали С. Михалкова, лауреат премии В. Крапивина, «Новая детская книга», кинофестиваля «Золотой витязь», премии Э. Успенского-2020 и 2021. Книги переведены на английский, корейский, немецкий, словацкий и китайский языки, по произведениям А. Никольской в средней школе сдают ВПР по литературе. В 2019 г. вышла одноименная экранизация бестселлера «Я уеду жить в Свитер». 
 
- Каждый день мы выполняем письменное задание и ведем дневник наблюдений. 
- Вы смотрите проработанные экспертами, качественные видеоуроки в удобное для вас время. 
- Получаете обратную связь редактора по 10 текстам (если выбираете группу с фидбэком) 
- Плотное личное взаимодействие с мастером в течение всего курса. 
- В курсе участвуют 30 приглашенных спикеров (известные писатели, издатели, главные редакторы, PR-менеджеры издательств). 
 """
    bot.send_message(user_id, proggggg, parse_mode='HTML')
    ano = """
    <b>Видеолекции:</b>
1. Самоменеджмент свободного художника. 
2. Как войти в творческий поток и получать удовольствие от работы. 
3. Тактические ошибки начинающего автора. 
4. Стилистические ошибки начинающего автора. 
5. Комическое в литературе. 
6. Тонкости сотрудничества с российскими и зарубежными издательствами. 
7. Критика и ресурсное отношение к ней. 
8. Как создаются бестселлеры. 
9. Online и offline продвижение книги. 
10. От начинающего автора – к известному писателю. 
 
<b>Стоимость участия:</b>
- курс без проверки заданий редактором– 20.000 руб. 
- курс с проверкой заданий редактором – 36.000 руб. 
– vip-курс с кураторством в личных сообщениях — разбор в текстовом формате, голосовое сопровождение, возможность диалога и повторной проверки текстов. Подробный анализ мастером выполненных заданий и личные рекомендации по работе с издательствами — 60.000 руб. 

<b>Скидка - 3000 руб. при раннем бронировании</b> (бронь – от 2000 руб.). Возможна рассрочка платежа. 

Оплата за курс не возвращается. Выпускники получают пожизненный доступ ко всем материалам для самостоятельного обучения (для групп с обратной связью) и рабочие адреса издательств и журналов. Курс подходит авторам, пишущим и для детей, и для взрослых. 
Более 3000 выпускников. Их отзывы: https://vk.com/topic-163604618_38751358 
Если остались вопросы, пишите! 
 
Всё легко, когда знаешь как.
    """

    bot.send_message(user_id,ano, parse_mode='HTML')
    image_path = r'photos/photo_2023-07-05_19-06-17.jpg'
    with open(image_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'forward8')
def bt3(call):
    user_id = call.message.chat.id
    user_name = call.from_user.username
    bot.send_message(-1001885886162,f"Пользователь:<b> {user_name}\n </b>отправил заявку",parse_mode='HTML')
    bot.send_message(user_id, f"<b>{user_name}:</b>\nзаявка успешно отправлена! В скором времени с вами свяжутся.",parse_mode='HTML')




bot.infinity_polling()
