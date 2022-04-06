from models.conference import Conference


def get_conferences() -> str:
    if Conference.objects.count() == 0:
        return "На данный момент нет созданных конференций."
    conf = ""
    for conference in Conference.objects.all():
        conf += (f"{conference.title}, количество "
                 f"участников: {len(conference.pupils)}\n")
    return conf
