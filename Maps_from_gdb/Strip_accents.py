
#               Caracteres especiais


def strip_accents(text):
    # type: (object) -> object
    try:
        text = unicode(text, 'utf-8')
    except:
        pass

    text = unicodedata.normalize('NFD', text) \
        .encode('ascii', 'ignore') \
        .decode("utf-8")

    return str(text)