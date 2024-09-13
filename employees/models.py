from django.db import models
from PIL import Image

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
        # Override the save method to resize the image before saving
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the original save method

        if self.photo:  # If a photo is uploaded
            img = Image.open(self.photo.path)  # Open the image file

            # Resize the image if it's larger than 300x300 pixels
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)  # Resize the image to fit within the output_size
                img.save(self.photo.path)
