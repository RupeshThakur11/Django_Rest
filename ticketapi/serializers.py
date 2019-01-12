from rest_framework import serializers

from django.contrib.auth.models import User
from tickets.models import Ticket, Category , Chat , Genre , Artist, Song , Album

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','title', 'ticket_id','user', 'content', 'category','created', 'modified')

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')

class ChatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Chat
		fields =('part','rece','created','modified','message')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields =('name')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields =('name','date_formed')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields =('title','release_date','author','duration','artist','genre')                            

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields =('title','disc_number','disc_total','release_date','songs','label')
