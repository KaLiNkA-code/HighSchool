from typing import Tuple

from mongoengine.queryset.visitor import Q

from models.classroom import ClassRoom


async def create_user_func(data, user) -> Tuple[str, str] or str:
    try:
        status = "Участник группы"
        classroom = ClassRoom.objects.filter(
            Q(code=data["code"]) | Q(admin_code=data["code"])
        ).first()
        if classroom is None:
            return "Класс не найден, попробуйте еще раз."
        # Сохранение полей и отправка сообщения с подтверждением
        if data["code"] == classroom.admin_code:
            user.is_admin = True
            user.classroom = classroom
            status = "Администратор группы"
        user.classroom = classroom
        classroom.pupils.append(user)
        classroom.save()
        user.save()
        return status, classroom.name
    except Exception as error:
        print(error)
