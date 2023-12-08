from django.shortcuts import render

from first_app.forms import StudentForm

# Create your views here.
def home(res):
    if res.method == 'POST':
        form = StudentForm(res.POST)
        if form.is_valid():
            form.save()
            print(res.POST)
    else:
        form = StudentForm()
    return render(res,'home.html',{'form':form})