from django.shortcuts import render
from .models import ChangeEncode
import base64
from .forms import ChangeEncodeForm
import hashlib


def index(request):
    return render(request, 'index.html')


def Base64(request):
    """
    base64_encode
    """
    if request.method == 'POST':
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen').encode('ascii')
        changeencode.change = base64.b64encode(changeencode.change)
        changeencode.change = changeencode.change.decode('ascii')
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)


def MD5(request):
    """
    md5_encode
    """
    if request.method == 'POST':
        md = hashlib.md5()
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        md.update(form.data.get('origen').encode('utf-8'))
        changeencode.change = md.hexdigest()
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)


def SHA1(request):
    """
    SHA1_encode
    """
    if request.method == 'POST':
        md = hashlib.sha1()
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        md.update(form.data.get('origen').encode('utf-8'))
        changeencode.change = md.hexdigest()
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)


def SHA224(request):
    """
    SHA224_encode
    """
    if request.method == 'POST':
        md = hashlib.sha224()
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        md.update(form.data.get('origen').encode('utf-8'))
        changeencode.change = md.hexdigest()
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)


def SHA256(request):
    """
    SHA256_encode
    """
    if request.method == 'POST':
        md = hashlib.sha256()
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        md.update(form.data.get('origen').encode('utf-8'))
        changeencode.change = md.hexdigest()
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)


def SHA384(request):
    """
    SHA384_encode
    """
    if request.method == 'POST':
        md = hashlib.sha384()
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        md.update(form.data.get('origen').encode('utf-8'))
        changeencode.change = md.hexdigest()
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)


def SHA512(request):
    """
    SHA1_encode
    """
    if request.method == 'POST':
        md = hashlib.sha512()
        form = ChangeEncodeForm(request.POST)
        changeencode = ChangeEncode(origen=form.data.get('origen'))
        changeencode.change = form.data.get('origen')
        md.update(form.data.get('origen').encode('utf-8'))
        changeencode.change = md.hexdigest()
    else:
        form = ChangeEncodeForm(request.GET)
        changeencode = ChangeEncode(origen="Please click button after entering data next to")
    context = {'form': form,
               'changeencode': changeencode}
    return render(request, 'encode.html', context)
