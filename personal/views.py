from django.shortcuts import render

# Create your views here.


def home_screen_view(request):

    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    list_of_values.append("third entry")
    list_of_values.append("first entry")

    context = {
        'some_string': "This is the string",
        'some_number': 1245,
        'list_of_values': list_of_values
    }

    return render(request, "personal/home.html", context)
