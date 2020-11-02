from django.shortcuts import render, redirect
import numpy as np
import PIL.Image as Image
import tensorflow as tf
import tensorflow_hub as hub
from data.models import Data
from data.forms import Form
from django.core.files.storage import FileSystemStorage

def prediction(img1):
    model = tf.keras.models.load_model('model/indian_currency.h5',custom_objects={'KerasLayer': hub.KerasLayer})
    img = Image.open(img1).resize((224, 224))
    img = np.array(img) / 255.0
    classes = ['100 ruppes note', '200 ruppes note', '2000 ruppes note', '500 ruppes note', '50 ruppes note', '10 ruppes note', '20 ruppes note']
    predicted_number = classes[np.argmax(model.predict(img[np.newaxis,...]))]
    return predicted_number


def index(request):
    form = Form()
    if request.method == "POST":
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            x = form.cleaned_data['img']
            form.save()
            return render(request,'index.html',{'pre_pred':prediction(f'media\\image\\{x}'),'form': form,'img':x})
    return render(request, 'index.html',{
        'form': form
    })