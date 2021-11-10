from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from PIL import Image
from .models import Profile, Post, Category_choices



class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """


# Позже переведу все формы через апи
# Импортировал модели для сериализации-профиль,пост
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('login', 'name', 'bio', 'ava')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CurrentUserDefault()
    title = serializers.CharField(max_length=1400)
    text = serializers.CharField(style={'base_template': 'textarea.html', 'rows': 7})
    category = serializers.ChoiceField(choices=Category_choices)
    img = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = Post
        fields = ('id','title', 'text', 'category', 'public_time', 'author', 'img')









class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension