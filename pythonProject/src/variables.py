"""URL"""
url_prod = "https://clearcase.net/"  # Прод урла.
url_stand = "https://stand.ru.tuna.am/"  # Стенд урла.

url = url_stand

"""Куку и прочее"""
token = "v4.local.qsWTdNfKyB2Y5ydrhvLSYg0G1L1eP47lMBAwaDq86x-PFZam9w3j17InKxfCNcrvIhAF-tTQgX5ytW-fIRaSyRPIaxR2pwRXH5SFTjeTO6KiqCfqLtwRXEmbwKgmELjZ0IU0FwHcT-XgH4Q_IN-pRCtRb9ZJStSYirxW7T9ZWGGERzMGJ6zvYRx50LItqEng0ooR1i3lNvDhcVvGt3g"

"""Главная страница и хедер"""
clear_case_inscription_xpath = "//img[@alt='home']"  # Clera Case надпись.

# cases_button_xpath = "//div[@class='flex flex-row gap-[38px] self-center z-10']/div[1]"  # Кнопка "Кейсы". Новогоднее.
cases_button_xpath = "//div[@class='flex flex-row gap-[38px] self-center']/button[1]"  # Кнопка "Кейсы".

# upgrade_button_xpath = "//div[@class='flex flex-row gap-[38px] self-center z-10']/div[2]"  # Кнопка "Апгрейды". Новогоднее.
upgrade_button_xpath = "//div[@class='flex flex-row gap-[38px] self-center']/button[2]"  # Кнопка "Апгрейды".

# contract_button_xpath = "//div[@class='flex flex-row gap-[38px] self-center z-10']/div[3]"  # Кнопка "Контракты". Новогоднее.
contract_button_xpath = "//div[@class='flex flex-row gap-[38px] self-center']/button[3]"  # Кнопка "Контракты".

replenishment_button_xpath = "//div[@class='replenishment-button']"  # Кнопка пополнения счёта.
balance_xpath = "//div[@class='replenishment-button']/div[1]"  # Баланс из хедера.
avatar_icon_xpath = "//img[@alt='изображение аватара профиля']"  # Аватарка профиля в хедере.

banner_xpath = "//video[@class='object-cover h-full']"  # Баннер.
case_xpath = f"//main[@class='page-content']/div[{2}]/div[2]/button[{1}]"  # Случайный кейс.

login_through_inscription_xpath = "//p[@class='login-text']"  # Надпись "Войти через".
telegram_xpath = "//div[@class='flex gap-6']/button[1]"  # Телеграм.
steam_xpath = "//div[@class='flex gap-6']/button[2]"  # Стим.

"""Cтраница Кейсы"""
container_open_cases_button_xpath = "//div[@class='control-buttons-container']"  # Контейнер с кнопками открытия.

case_name_xpath = "//h2"  # Имя кейса.
one_opening_price = "//p[@class='__className_86079f box-price text-custom-orange']"  # Цена одного открытия кейса.

telegram_case_xpath = "//div[@class='control-buttons-container']/button[1]"  # Кнопка входа в Телеграм со страницы кейса.
steam_case_xpath = "//div[@class='control-buttons-container']/button[2]"  # Кнопка входа в Стим со страницы кейса.
count_skin_button_xpath = f"//div[@class='count-boxes-container']/button[{1}]"  # Кнопка выбора количества скинов для открытия.
opening_skin_button_xpath = f"//div[@class='control-buttons-container']/button[{1}]"  # Кнопка открытия скина.
fast_opening_skin_button_xpath = f"//div[@class='control-buttons-container']/button[{2}]"  # Кнопка быстрого открытия скина.
first_fast_opened_skin_xpath = "//div[@class='box-container']/div[1]/div/div[1]"  # Первый быстро открытый скин.

"""Cтраница Апгрейд"""
result_xpath = "//div[@class='upgrade-container']/div[2]/div[1]/h3"  # Результат апгрейда.

start_button_xpath = "//button[@class='button-light undefined false mt-[22px] w-[220px] gap-4 text-[20px] font-semibold']"  # Кнопка запуска апгрейда.
inactive_start_button_xpath = "//div[@class='w-full items-center flex flex-col']/button"  # Неактивная нопка запуска апгрейда.

spending_balance_xpath = "//p[@class='__className_86079f text-white text-[24px] font-normal leading-[28.8px]']"  # Баланс потраченый для апгрейда.
balance_adjustment_slider_xpath = "//div[@aria-valuemax]"  # Слайдер настройки баланса для апгрейда.

upgrade_container_xpath = "//div[@class='upgrade-container']"  # Контейнер апгрейда.
skin_from_inventory_xpath = f"//div[@class='upgrade-inventories-container']/div[1]/div[3]/div/div/div[{1}]"  # Скин в инвентаре.
skin_for_upgrade_xpath = f"//div[@class='upgrade-inventories-container']/div[2]/div[3]/div/div/div[{1}]"  # Предметы для апгрейда.
price_inventory_case_xpath = "//div[@class='upgrade-container']/div[1]/div[2]/button/div/div/div[1]/div"  # Цена скина из инвентаря.
price_upgrade_case_xpath = "//div[@class='upgrade-container']/div[3]/div[2]/button/div/div/div[1]/div"  # Цена скина для апгрейд.
name_inventory_case_xpath = "//div[@class='upgrade-container']/div[1]/div[2]/button/div/div/div[2]/div"  # Имя скина из инвентаря.
name_upgrade_skin_xpath = "//div[@class='upgrade-container']/div[3]/div[2]/button/div/div/div[2]/div"  # Имя скина для апгрейд.
percent_xpath = "//div[@class='upgrade-container']/div[2]/div[1]/div[6]/h3"  # Процент.
start_button_xpath = "//button[@class='button-light undefined false mt-[22px] w-[220px] gap-4 text-[20px] font-semibold']"  # Кнопка запуска апгрейда.
inactive_start_button_xpath = "//div[@class='w-full items-center flex flex-col z-10']/button"  # Неактивная нопка запуска апгрейда.

"""Cтраница Контракт"""
contract_container_xpath = "//div[@class='contract-grid-container']"  # Сетка-контейнер для контракта.

"""Cтраница пользователя"""
profile_content_xpath = "//div[@class='profile-content']"  # Контент профиля на странице пользователя.

logout_button_xpath = "//button[@class='__className_86079f logout-button']"  # Кнопка выхода из аккаунта.

active_sale_button_xpath = "//div[@class='flex flex-row justify-center gap-6']/button[1]"  # Активная кнопка "Продать".
select_all_button_xpath = "//div[@class='flex flex-row justify-center gap-6']/button[2]"  # Кнопка "Выделить всё".

button_inventory_xpath = "//div[@class='__className_86079f profile-switcher']/button[1]"  # Кнопка "Инвентарь".
case_name_inventory_xpath = "//div[@class='default-inventory-container']/div[1]/div/div/div[2]/div"  # Имя скина из инвентаря.

any_skin_in_inventory_xpath = "//div[@class='default-inventory-container']/div"  # Скин в инвентаре.

button_history_xpath = "//div[@class='__className_86079f profile-switcher']/button[3]"  # Кнопка "История".
case_name_history_xpath = "//div[@class='default-inventory-container']/div[1]/div/div/div[2]/div"  # Имя скина из истории.

inventory_is_empty_inscription_xpath = "//p[@class='__className_86079f text-[#545A6B] text-[24px] leading-[28px]']"  # Надпись "Инвентарь пуст".
download_more_button_xpath = "//button[@class='button-light undefined undefined mt-5 h-[40px] w-[160px] font-semibold']"  # Кнопка "Загрузить ещё".

"""Главная Пополнения счёта"""
payment_block_xpath = "//div[@class='payment-blocks']"  # Блок пополнения.

"""Стим и Телеграм"""
telegram_some_inscription_xpath = "//div[@class='login_header_text']"  # Надпись для проверки отображения страницы Телеграма.
steam_some_inscription_xpath = "//img[@src='https://community.fastly.steamstatic.com/public/shared/images/header/logo_steam.svg?t=962016']"  # Надпись для проверки отображения страницы Стима.

"""Пользовательское соглашение"""
agreement_link_xpath = "//div[@class='footer-links md:flex-row md:gap-5']/a[1]"  # Линка на пользовательское соглашение в футере.
agreement_inscription_xpath = "//h1[@class='self-center text-4xl uppercase']"  # Надпись "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ".

"""Вопрос - Ответ"""
questions_link_xpath = "//div[@class='footer-links md:flex-row md:gap-5']/a[2]"  # Линка на Вопрос-Ответ в футере.
questions_inscription_xpath = "//h1[@class='self-center text-4xl uppercase']"  # Надпись "Часто задаваемые вопросы".

"""Всплывающие сообщения"""
head_message_xpath = "//div[@class=' w-full h-full  px-[10px] pb-[6px] pt-[4px]']/div[1]/h3"  # Заголовок сообщения.
body_message_xpath = "//div[@class=' w-full h-full  px-[10px] pb-[6px] pt-[4px]']/div[2]/p"  # Текст сообщения.
