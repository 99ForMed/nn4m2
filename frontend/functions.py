import os

def handle_uploaded_file(f, name):
    if not os.path.exists('static/upload/'+name):
        os.mkdir(os.path.join('static/upload/', name))
    
    with open('static/upload/'+name+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)