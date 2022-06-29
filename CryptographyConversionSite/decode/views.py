from django.shortcuts import render
from .models import ChangeDecode
from .forms import ChangeDecodeForm
import base64


def Base64(request):
    """
    Base64_decode
    """
    if request.method == 'POST':
        form = ChangeDecodeForm(request.POST)
        changeencode = ChangeDecode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        changeencode.change = base64.b64decode(changeencode.change)
        changeencode.change =changeencode.change.decode('ascii')
    else:
        form = ChangeDecodeForm(request.GET)
        changeencode = ChangeDecode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'decode.html', context)
