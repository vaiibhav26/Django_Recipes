from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    #  for dynamic data 
    peoples =[
        {'name': 'Vaibhav', 'age': 21},
        {'name': 'Sanket', 'age': 4},
        {'name': 'Sachin', 'age': 45},
        {'name': 'Varun', 'age': 98}
    ]

    text = """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod laboriosam fugit, libero tempora labore adipisci repudiandae officia accusantium maiores consectetur, eius in quia aut, provident voluptates! Impedit, illo repellat in vero amet maiores accusamus eveniet a dicta recusandae perspiciatis voluptas ducimus consectetur beatae neque iusto quos? Illum, velit deserunt ipsum, qui fuga incidunt magni odio dolor error provident asperiores!"""

    vegetables = ['tomato', 'potato', 'cucumber', 'brinjal']

    for people in peoples:
        print(people)


    #to return a file on the webpage (index.html)
    
    return render(request, "index.html", context={'page':'home','peoples': peoples, 'text': text, 'vegetables': vegetables})


    # return HttpResponse("""<h1>hey! I am a django server</h1>
    #                     <p> this is a paragraph just for testing</p>
    #                     <hr>
    #                     <h3 style = "color: red; font-size: 30px;"> hope this is fun </h3>

    #                     <!--so this way we can put html here but this is not feasible because big websites may have 
    #                      larger html template-->

    #                     """)

def Success_page(request):
    print("#" * 10)
    return HttpResponse("This is the success_page")

def about(request):
    context = {'page': 'about'}
    return render(request, "about.html",context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, "contact.html",context)