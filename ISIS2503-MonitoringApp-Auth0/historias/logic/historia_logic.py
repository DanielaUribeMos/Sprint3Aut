from ..models import Historia

def get_historias():
    queryset = Historia.objects.all()
    return (queryset)

def get_historia(id):
    historia = Historia.objects.raw("SELECT * FROM historias_historia WHERE id=%s" % id)[0]
    return (historia)

def create_historia(form):
    plantilla = form.save()
    plantilla.save()
    return ()
