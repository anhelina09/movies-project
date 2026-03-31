from django.shortcuts import render, redirect

def movies_list(request):
    return render(request, 'movies/movies_list.html')


def movie_detail(request):
    return render(request, 'movies/movie_detail.html')



def add_movie(request):
    if request.method == 'POST':
        
        return redirect('movies_list')

    return render(request, 'movies/add_movie.html')



def edit_movie(request):
    return render(request, 'movies/edit_movie.html')



def delete_movie(request):
    return render(request, 'movies/delete_movie.html')
