from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306208426',
        'name': 'Raysha Reifika',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)