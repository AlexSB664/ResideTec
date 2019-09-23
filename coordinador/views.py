from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method ==  'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('redi')
        else:
            mensaje = "Error contraseña o correo no valido"
            return render(request,'login.html',{'mensaje':mensaje})
    else:
        return render(request,'login.html')

