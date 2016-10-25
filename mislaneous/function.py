def format_name(first_name, last_name):
    """ format name by putting returing a string which contains last name vs first name
    @type first_name: str
    @type last_name: str
    @rtype: str

    >>> format_name('David','Cohen')
    'Cohen, David'
    """
    return '{},{}'.format(last_name, first_name)

def format_info(first_name, last_name, phone):
    """ format info and return a string containing last name followed by frist name followed by phone
    @type first_name: str
    @type last_name: str
    @type phone: (str|int)

    >>> format_info('Sagnik','Adusumilli',647972744)
    'Adusumilli, Sagnik: 6472782744'
     >>> format_info('Sagnik','Adusumilli',647972744)
'Adusumilli, Sagnik: 6472782744'
    """

    return format_name(first_name,last_name)+":" + str(phone)


