from django.shortcuts import render


def handler404(request, exception):
    return render(request, '404.html', status=404)


def exchange(reqests):
    currencies = {
        "-": (10 ** 0, 0),
        "атто": (10 ** -18, -18), "фемто": (10 ** -15, -15), "пико": (10 ** -12, -12), "нано": (10 ** -9, -9),
        "микро": (10 ** -6, -6), "мили": (10 ** -3, -3), "санти": (10 ** -2, -2), "деци": (10 ** -1, -1),
        "дека": (10 ** 1, 1), "гекто": (10 ** 2, 2), "кило": (10 ** 3, 3), "мега": (10 ** 6, 6),
        "гига": (10 ** 9, 9), "тера": (10 ** 12, 12), "пета": (10 ** 15, 15), "экса": (10 ** 18, 18)
    }

    if reqests.method == "GET":
        context = {
            'currencies': currencies
        }
        return render(request=reqests, template_name='ex_app/index.html', context=context)

    if reqests.method == "POST":
        if not reqests.POST.get('from-amount'):
            context = {
                'currencies': currencies
            }
            return render(request=reqests, template_name='ex_app/index.html', context=context)

        from_amount = float(reqests.POST.get('from-amount'))
        from_curr = reqests.POST.get('from-curr')
        to_curr = reqests.POST.get('to-curr')

        cur = currencies[from_curr][1] - currencies[to_curr][1]
        res = 10 ** (currencies[from_curr][1] - currencies[to_curr][1]) * float(from_amount)
        bunch = "или"

        if cur > 18:
            res = "Число слишком большое"
            bunch = "Как степень 10ки: "

        elif cur < -18:
            res = "Число слишком маленькое"
            bunch = "Как степень 10ки: "

        res1 = str(from_amount) + " * 10^" + str(cur)

        context = {
            'from_amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'res': res,
            'res1': res1,
            'bunch': bunch
        }
        return render(request=reqests, template_name='ex_app/index.html', context=context)
