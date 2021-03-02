# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).
"""
LEADING DOCSTRING
"""
def make_alert_sound():
    """
    FUNC DOCSTRING
    """
    print('made alert sound.')
def make_accept_sound():
    """
    FUNC DOCSTRING
    """
    print('made acceptance sound')

ingredients = ['sodium benzoate']
has_sodium_nitrate = 'sodium nitrate' in ingredients
has_sodium_benzoate = 'sodium benzoate' in ingredients
has_sodium_oxide = 'sodium oxide' in ingredients
if has_sodium_nitrate or has_sodium_benzoate or has_sodium_oxide:
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
