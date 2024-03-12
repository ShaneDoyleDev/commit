from django import template

register = template.Library()


@register.filter(name='category_color')
def category_color(category):
    """
    Returns the CSS variable name for the color associated with a category.
    If the category is not found, returns the CSS variable name for the primary color.
    """

    variables = {
        "frontend": "--clr-frontend-category",
        "backend": "--clr-backend-category",
        "design": "--clr-design-category",
        "devops": "--clr-devops-category",
        "perspectives": "--clr-perspectives-category",
    }

    return variables.get(category, "--clr-primary")
