from .models import album
from django.shortcuts import render, get_object_or_404
 
def pen(request):
   all_albums = album.objects.all()
   return render(request,'appp/pen.html',{'all_albums': all_albums})
    
def detail(request, album_id):
   Album = get_object_or_404(album, pk=album_id)
   return render(request, 'appp/detail.html',{'album':Album})

def favorite(request, album_id):
    Album = get_object_or_404(album, pk=album_id)
    return render(request, 'appp/favorite.html',{'album':Album})	

