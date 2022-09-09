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
    two_marks = Mark.objects.filter(schoolkid=child, points=2)
    two_marks.update(points=4)
    three_marks = Mark.objects.filter(schoolkid=child, points=3)
    three_marks.update(points=5)


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
    chastisements.delete()


def create_commendation(schoolkid_name, subj_title):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except MultipleObjectsReturned:
        print("Уточните имя - найдено несколько учеников")
        return
    except ObjectDoesNotExist:
        print("Не нашли такого ученика - проверьте имя")
        return
    lesson = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter, subject__title=subj_title)[-1]
    Commendation.objects.create(text="Very Good", created=lesson.date, schoolkid=child, subject=lesson.subject,
                                teacher=lesson.teacher)