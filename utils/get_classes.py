from models.classroom import ClassRoom


def get_classes() -> str:
    if ClassRoom.objects.count() == 0:
        return "На данный момент нет созданных классов."
    classes = ""
    for classroom in ClassRoom.objects.all():
        classes += f"{classroom.name}, участников: {len(classroom.pupils)}\n"
    return classes
