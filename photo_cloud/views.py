from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm, ImageForm
from .models import Image
from django.contrib import messages


def home(request):
    images = Image.objects.all()
    return render(request, "index.html", {"images": images})


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ImageUploadForm()
    return render(request, "upload.html", {"form": form})


def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)  # Fetch the image by its primary key
    return render(request, "image_detail.html", {"image": image})


def edit_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully!")
            return redirect("home")
    else:
        form = ImageForm(instance=image)
    return render(request, "image_edit.html", {"form": form, "image": image})


def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    image.delete()
    messages.success(request, "Image deleted successfully!")
    return redirect("home")
