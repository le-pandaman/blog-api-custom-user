from django.db import models
from django.conf import settings
from django.urls import reverse


from accounts.models import CustomUser
# Create your models here.


class Posts(models.Model):

    # class Meta:
    #     verbose_name = 'Post'

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation of the object.
        """

        return self.title

    def __repr__(self):
        """
        Return a string representation of the object.
        """

        return self.title

    def author_name(self):

        return self.author.username

    def get_absolute_url(self):
        """
        Return the absolute URL for the current object using the 'post_detail_api' view with the object's primary key as a parameter.
        """

        return reverse('post_detail_api', kwargs={"pk": self.pk})
