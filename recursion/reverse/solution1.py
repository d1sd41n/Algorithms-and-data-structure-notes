def reverse(strng):
    if not len(strng):
        return ""
    return strng[-1] + reverse(strng[:-1])


assert reverse("hola") == 'aloh'
assert reverse("me la suda") == 'adus al em'
assert reverse("python") == 'nohtyp'
assert reverse("el bananero") == 'orenanab le'


