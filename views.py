form django.shirtcuts import rende 
form .models import Libro

# Create your views here
def lista_libros(request):
  libros = Libro.objects.all()
  return render(request, 'lista_libros.html',{'libros': libros})
  