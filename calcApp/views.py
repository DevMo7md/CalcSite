from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def main(request):
    context = {}
    return render(request, 'home.html', context=context)


def home(request):
    if request.method == "POST":
        snum = request.POST.get('snum')
        lnum = request.POST.get('lnum')
        opr = request.POST.get('opr')
        try:
            if opr == "plus":
                result = float(snum) + float(lnum)

            elif opr == 'minus':
                result = float(snum) - float(lnum)
                context = {'result': result}
                return render(request, 'home.html', context)

            elif opr == 'multiply':
                result = float(snum) * float(lnum)
                context = {'result': result}
                return render(request, 'home.html', context)

            elif opr == 'devide':
                result = float(snum) / float(lnum)
                context = {'result': result}
                return render(request, 'home.html', context)

            else:
                return render(request, 'home.html')

            context = {'result': result}
            return render(request, 'home.html', context)

        except:
            return redirect("/")

    return redirect("/")
