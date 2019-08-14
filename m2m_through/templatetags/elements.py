from django import template


register = template.Library()


@register.inclusion_tag('elements/return_to_top.html')
def return_to_top(**kwargs):
    """ Returns the circled arrow that when clicked,
    moves the user to the top of the page. """

    element_id = 'return-to-top'
    if 'id' in kwargs:
        element_id = kwargs.get("id")

    background_color = 'black'
    if 'background_color' in kwargs:
        background_color = kwargs.get("background_color")

    font_color = 'white'
    if 'font_color' in kwargs:
        font_color = kwargs.get("font_color")

    return {'id': element_id,
            'background_color': background_color,
            'font_color': font_color,
            }


@register.inclusion_tag('elements/hamburger_button.html')
def hamburger_button(**kwargs):
    """ Returns the hamburger button that when clicked,
    expands an html dom element. """

    element_id = 'hamburger'
    if 'id' in kwargs:
        element_id = kwargs.get("id")

    target_id = 'collapsibleNavbar'
    if 'target_id' in kwargs:
        target_id = kwargs.get("target_id")

    button_class = 'navbar-toggler'
    if 'button_class' in kwargs:
        button_class = kwargs.get("button_class")

    color = "#008181"
    if 'color' in kwargs:
        color = kwargs.get("color")

    return {'id': element_id, 
        'target_id': target_id,
        'button_class': button_class,
        'color': color,
    }