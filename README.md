# Python developer 17.08.2021 MSK (UTC+3)

## 1. Python - синтаксис языка, базовые структуры данных, функциональное программирование.

### Задание 1.
> Написать функцию, реализующую вывод таблицы умножения размерностью `AｘB`. Первый и второй множитель должны задаваться в виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле. После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку. Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.

### Задание 2.
>Дополнить следующую функцию недостающим кодом:
> 
>def print_directory_contents(sPath):
> 
>>   """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
>>
>>    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с 
    вложенными структурами.
>> 
>>    """
    # заполните далее


### Задание 3.
> Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.

### Задание 4.
> Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка: 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада. Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (`begin_sum`, `end_sum`, `6`, `12`, `24`). Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока. В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.

### Задание 5.
> Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.


## 2. Python - парадигма ООП особенности и отличия от других ЯП.

### Задание 1. 
> Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (`ItemDiscount`), должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (`ItemDiscountReport`), должен содержать функцию (`get_parent_data`), отвечающую за отображение информации о товаре в одной строке. Проверить работу программы, создав экземпляр (объект) родительского класса.

### Задание 2.
> Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.

### Задание 3.
> Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).

### Задание 4.
> Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод `__init__`, в который должна передаваться переменная — скидка), и перегрузку метода `__str__` дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).

### Задание 5.
> Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс `ItemDiscountReport` на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию `get_info`, которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.


## Урок 3. Python - стандартная библиотека Python.

### Задание 1. 
> Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).

### Задание 2. 
> Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают, программа должна возвращать значение `True`, иначе `False`.

### Задание 3. 
> Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре для него должно сохраняться значение `None`. Значения, которым не хватило ключей, необходимо отбросить.

### Задание 4. 
> Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию `zip()`. Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.

### Задание 5. 
> Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений заменить на значения типа `example345` (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, `example345`.


## Урок 4. Django - основные понятия ORM, структура и особенности проектирования.

### Задание 1.
>Создать виртуальное окружение проекта, под которым установить необходимый инструментарий (файл `requirements.txt`).

### Задание 2.
>Под виртуальным окружением создать Django-проект и одно приложение, настроить файл `settings.py`, выполнить базовые миграции. Запустить Django-сервер для проверки работоспособности проекта.

### Задание 3.
>В каталоге приложения создать модель, которая должна хранить информацию о поступивших товарах: название, дату поступления, цену, единицу измерения, имя поставщика. Выполнить миграции

### Задание 4.
>Проверить правильность созданной модели, зарегистрировав ее в админке приложения.

### Задание 5.
>На основе модели добавить класс формы указания данных о товаре. Использовать наследование от `forms.ModelForm`. 

### Задание 6.
>Настроить файл `urls.py` внутреннего каталога проекта. Он должен содержать два шаблона url-адресов: привязку к url-адресу админки проекта (будет в файле по умолчанию после создания проекта) и привязку к набору шаблонов url-адресов созданного приложения (оператор `include`).

### Задание 7.
>Создать и настроить файл привязок `urls.py` для приложения. В этом файле создать две привязки: к url-адресу главной страницы проекта и к странице добавления товара. Для каждой из привязок указать функцию-контроллер и название. Функции-контроллеры должны отвечать за загрузку списка товаров на главной странице и добавление товара на второй странице.

### Задание 8.
>В файле `views.py` каталога проекта реализовать два контроллера в формате функций. Первый должен извлекать все записи из модели с каталогом товаром и передавать переменную со списком товаров в контекст шаблона (html-страница со списком товаров). Во втором контроллере должен создаваться объект формы для ввода данных о товаре и выполняться рендеринг шаблона страницы добавления товара. В контекст шаблона необходимо передавать объект формы.

### Задание 9.
>В корне проекта создать директорию `templates` с двумя стандартными шаблонами: базовым (`base.html`) и шаблоном формы (`form.html`). Базовый шаблон будет соответствовать каркасу главной страницы. В нем необходимо реализовать один динамически обновляемый блок — например, `{% block content %}{% endblock %}`. Он будет содержать таблицу со списком товаров, которая динамически подгружается из шаблона-наследника (html-страница со списком товаров). В файле `base.html` необходимо подключить статику и указать ссылку на CSS-файл со стилизацией проекта. Можно воспользоваться файлом `bootstrap.min.css` (его нужно скачать и поместить в каталог `.static/css`).

### Задание 10.
>В шаблоне формы `form.html`, используя теги шаблонов, реализовать разметку формы. При этом использовать переменную контекста шаблона, содержащую объект формы, — например, form. К надписям полей обращаться по `field.label`, к самим полям — `field`.

### Задание 11.
>В каталоге приложения создать директорию `templates` с двумя шаблонами: шаблоном html-страницы со списком товаров (`goods_list.html`) и html-страницы (формы) их добавления (`good_create.html`). В первом шаблоне необходимо указать шаблон-родитель `base.html`, кнопку добавления товара и разметить html-таблицу. Каждая из ее строк (кроме той, что с заголовками) должна формироваться при переборе содержимого переменной со списком товаров — мы ее предварительно передали в контекст данного шаблона из соответствующего контроллера. Для каждого из значений переменной (фактически — это запись базы данных), полученного в цикле, необходимо обратиться к нужному полю и вывести его в соответствующей ячейке. К кнопке привязать ссылку на страницу добавления товара. Для этого использовать имя нужного шаблона url-адреса файла `urls.py` приложения.

### Задание 12.
>В шаблоне `good_create.html` создать html-тег `form`. В него поместить тег `include`, добавляющий html-разметку формы (`form.html`) и кнопку добавления товара. Для тега `form` необходимо определить два атрибута: `method` со значением `post` и `enctype` со значением `multipart/form-data`.


## Урок 5. Django - AJAX, JavaScript, jQuery.
>Продолжим работать над каталогом товаров. На данный момент приложение действует в синхронном режиме, т.е. пользователь нажимает кнопку добавления, после чего выполняется переход на соответствующую страницу.
Усовершенствуем работу проекта: сделаем его более похожим на десктопное приложение — без всяких перезагрузок страницы. Форма должна загружаться, как модальное окно, как бы «поверх» содержимого главной страницы. После этого пользователь может указать данные нового товара и сохранить его в базе. При этом модальное окно формы должно закрываться, а изменения, т.е. строка с добавленным товаром, должна отобразиться в таблице на главной странице. Таким образом мы реализуем асинхронную работу приложения. Для этого необходимо использовать знания языка программирования JavaScript и библиотеки jQuery. Разобьем выполнение задания на несколько этапов:

### Задание 1. Доработка шаблонов
#### 1.1 `goods_list.html`
>В первую очередь необходимо внести изменения в шаблон `goods_list.html`. Создадим пустую структуру вложенных блочных элементов `div` (три элемента). Ее содержимое будет динамически изменяться при нажатии кнопки добавления товара, т.е. будет загружаться модальное окно формы добавления товара

#### 1.2 `base.html`
> В этом файле необходимо добавить подключение библиотеки jQuery. Для локального подключения следует скачать и поместить в директорию static/js файл с кодом библиотеки — например, `jquery-3.3.1.min.js`. В эту же директорию следует добавить файл `bootstrap.min.js`, который позволит упростить стилизацию элементов страницы.

#### 1.3 `good_create.html`
>Это шаблон, в котором находится разметка формы добавления товара. Его следует модифицировать, указав в атрибуте `action` тега `form` имя url-шаблона адреса, при переходе на который запускается контроллер записи в модель введенных данных. В нашем случае это шаблон `good_create.html`.
Также в данный шаблон необходимо поместить тег импорта разметки самой формы `form.html` в блочный элемент и добавить две кнопки: сохранения данных в форме и ее закрытия.

#### 1.4 `form.html`
>В шаблон формы необходимо выполнить загрузку инструментов пакета `django-widget-tweaks`:


### Задание 2. Доработка контроллеров (Я реализую более современный вариант, на CBV! Соответственно в методах выполнения есть различия, но результат выполненного задания идентичен)
>Необходимо доработать один из двух наших контроллеров и написать третий. С первым — `good_list` — все в порядке, а во втором контроллере необходимо реализовать только проверку типа запроса: `POST` или `GET`. При этом также должен генерироваться экземпляр формы. Возвращать этот контроллер должен вызов дополнительного контроллера-функции `save_good_form` с со следующими параметрами: объект запроса, объект формы, шаблон. Поскольку данный контроллер должен «открыть» форму добавления товара, в качестве шаблона следует передавать `good_create.html`.
Контроллер `save_good_form` используется для проверки валидности и формирования словаря `data`, в котором мы будем указывать, является ли форма валидной, а также передавать преобразованный в строку шаблон и контекст (метод `render_to_string`). Данный контроллер будет возвращать ответ в формате `JSON`. Это позволит работать с формой и контекстом из файла скрипта средствами библиотеки jQuery, то есть асинхронно делать форму и передавать данные на сторону сервера.


### Задание 3. Написание скрипта
>Этот скрипт должен обрабатывать переданные в формате JSON данные: обращаться с помощью селекторов к элементам веб-страницы и осуществлять манипуляции над ними. Подразумевается динамическое обновление содержимого главной страницы: подгрузка шаблона формы, а также асинхронное (без перезагрузки главной страницы) сохранение данных в модель.
Для этого в файле сценария должны быть реализованы две функции. Первая отвечает за загрузку формы, вторая — за сохранение введенных в форму данных. Для запуска первой функции необходимо выполнить ее привязку к событию нажатия на кнопку добавления товара. Для запуска второй привязка должна быть выполнена к событию отправки формы. И функции, и инструкции их вызова должны быть сохранены в функции-обертке `$(function(){....программный код….});`, чтобы решить всю задачу средствами библиотеки jQuery.


## Урок 6. Базы данных - работа с БД в Python и Django. Особенности и различия
>Практическое задание шестого и седьмого урока — разработать десктопное приложение с графическим интерфейсом пользователя, предназначенное для ведения простого складского учета. Это приложение с оконным интерфейсом будет реализовано в привязке к СУБД SQLite и позволит заносить в базу данных сведения о номенклатуре товаров, поставщиках и сотрудниках предприятия.
На данном этапе работы с проектом выполним первую часть практическое задания: подготовим фрагменты программного кода, отвечающие за создание таблиц базы данных. В седьмом уроке отображение этих таблиц реализуем в специальных виджетах. Ниже приведено описание необходимых блоков программного кода. 

### Задание 1. Создать файл базы данных
>С помощью одного из менеджеров баз данных (например, SQLiteStudio) создать пустой файл SQLite-базы данных. 

### Задание 2. Создать подключение к базе данных
>Выполнить импорт модуля с Python DB-API для реализации взаимодействия с СУБД SQLite. Создать подключение к базе данных, путь к которой записан в переменную `db_path`. Создать объект-курсор для выполнения операций с данными.

### Задание 3. Создать вспомогательные таблицы

#### 3.1 Категории товаров.
>Написать запрос создания таблицы `categories` (с проверкой ее существования). Таблица должна содержать два поля: `category_name` (категория), `category_description` (описание). Все поля должны быть не пустыми. Поле `category` должно быть первичным ключом.

#### 3.2 Единицы измерения товаров. 
>Написать запрос создания таблицы `units` с проверкой ее существования. Таблица должна содержать одно поле — `unit` (единица измерения). Оно должно быть не пустым и выступать первичным ключом.

#### 3.3 Должности.
>Написать запрос создания таблицы `positions` (с проверкой ее существования). Таблица должна содержать одно поле — `position` (должность). Оно должно быть не пустым и выступать первичным ключом.

### Задание 4. Создать основные таблицы

#### 4.1 Товары.
>Написать запрос создания таблицы `goods` с проверкой ее существования. Таблица должна содержать четыре поля: `good_id` (номер товара — первичный ключ), `good_name` (название товара), `good_unit` (единица измерения товара — внешний ключ на таблицу `units`), `good_cat` (категория товара — внешний ключ на таблицу `categories`).

#### 4.2 Сотрудники. 
>Написать запрос создания таблицы `employees` с проверкой ее существования. Таблица должна содержать три поля: `employee_id` (номер сотрудника — первичный ключ), `employee_fio` (ФИО сотрудника), `employee_position` (должность сотрудника — внешний ключ на таблицу `positions`).

#### 4.3 Поставщики.
>Написать запрос создания таблицы `vendors` с проверкой ее существования. Таблица должна содержать шесть полей: `vendor_id` (номер поставщика — первичный ключ), `vendor_name` (название поставщика), `vendor_ownerchipform` (форма собственности поставщика), `vendor_address` (адрес поставщика), `vendor_phone` (телефон поставщика), `vendor_email` (email поставщика).