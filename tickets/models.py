from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique ticket id

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created"]

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    
class Chat(models.Model):
    part=models.CharField(max_length=255)
    rece=models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    message= models.TextField() 


class Genre(models.Model):
    """
    Class to create a table representing a Genre, to be tied to an song.
    Extension of models.Model
    Variables:
        title: the song title
    Author: Ben Marks
    """
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API
        Returns a string representaion of the payment method's name field
        """
        return self.name

    class Meta:
        ordering = ('name',)


class Artist(models.Model):
    """
    Class to create a table representing an artist
    Extension of models.Model
    Variables:
        name: the artist title
        date_formed: the date of release
    Author: Ben Marks
    """
    name = models.CharField(max_length=100, blank=True, default='')
    date_formed = models.DateField(auto_now_add=False)

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API
        Returns a string representaion of the payment method's name field
        """
        return self.name

    class Meta:
        ordering = ('name',)


class Song(models.Model):
    """
    Class to create a table representing a song, to be tied to an artist or group of artists
    Extension of models.Model
    Variables:
        title: the song title
        release_date: the date of release
        author: the song's writer
    Author: Ben Marks
    """
    title = models.CharField(max_length=100, blank=True, default='')
    release_date = models.DateField(auto_now_add=False)
    author = models.CharField(max_length=100, blank=True, default='')
    duration = models.PositiveIntegerField()
    artist = models.ManyToManyField(Artist)
    genre = models.ForeignKey(Genre, related_name="genre",on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API
        Returns a string representaion of the payment method's name field
        """
        return self.title

    class Meta:
        ordering = ('title',)


class Album(models.Model):
    """
    Class to create a table representing an Album, to be tied to an artist or group of artists and the songs therein.
    Extension of models.Model
    Variables:
        title: the song title
        release_date: the date of release
        author: the song's writer
    Author: Ben Marks
    """
    title = models.CharField(max_length=100, blank=True, default='')
    disc_number = models.PositiveIntegerField()
    disc_total = models.PositiveIntegerField()
    release_date = models.DateField(auto_now_add=False)
    songs = models.ManyToManyField(Song)
    label = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API
        Returns a string representaion of the payment method's name field
        """
        return self.title

    class Meta:
        ordering = ('title',)

    def _str_(self):
       return self.name