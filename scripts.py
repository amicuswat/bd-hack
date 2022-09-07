from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)


def fix_marks(schoolkid_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except MultipleObjectsReturned:
        print("Уточните имя - найдено несколько учеников")
        return
    except ObjectDoesNotExist:
        print("Не нашли такого ученика - проверьте имя")
        return
    marks = Mark.objects.filter(schoolkid=child, points__lt=4)
    for mark in marks:
        if mark.points == 2:
            mark.points = int(4)
        else:
            mark.points = int(5)
        mark.save()


def remove_chastisements(schoolkid_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except MultipleObjectsReturned:
        print("Уточните имя - найдено несколько учеников")
        return
    except ObjectDoesNotExist:
        print("Не нашли такого ученика - проверьте имя")
        return
    chastisements = Chastisement.objects.filter(schoolkid=child)
    for elm in chastisements:
        elm.delete()


def create_commendation(schoolkid_name, subj_title):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except MultipleObjectsReturned:
        print("Уточните имя - найдено несколько учеников")
        return
    except ObjectDoesNotExist:
        print("Не нашли такого ученика - проверьте имя")
        return
    lesson = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter, subject__title=subj_title)[0]
    Commendation.objects.create(text="Very Good", created=lesson.date, schoolkid=child, subject=lesson.subject,
                                teacher=lesson.teacher)