import datetime

from django.shortcuts import render


def home_page(request):
    now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S")

    return render(
        request=request,
        template_name="base/home_page.html",
        context={
            "greetings_text": f"Hi, now is {now} in UTC.",
            "title": "Django base project",
        },
    )
