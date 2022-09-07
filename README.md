# Скрипты для внесения исправлений в сайт e-dairy

Скрипты для изменения оценок в электронном дневнике, удаления замечаний, внесения похвалы.

### Как установить

Скрипты не будут работать без запущенного проекта [e-dairy](https://github.com/amicuswat/e-diary).
Как установить и запустить e-dairy смотрите Readme.

- Сохраните файл scripts.py в папку
- Активируйте виртуальное окружение.
- Войдите в shell django:
```
python manage.py shell
```
Для изменения оценок:
```
>>> from scripts import fix_marks
>>> fix_marks("Фамилия Имя")
```
Для удаления замечаний:
```
>>> from scripts import remove_chastisements
>>> remove_chastisements("Фамилия Имя")
```
Для добавления похвалы:
```
>>> from scripts import create_commendation
>>> create_commendation("Фамилия Имя", "Предмет")
```

### Цель проекта
Код написан в образовательных целях,
на курсе для разработчиков [dvmn.org](https://dvmn.org/referrals/u4guYYiV5HjY6tnwtCShzP2cWFYE0EWnKeoJLEWP/)
