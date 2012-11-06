# -*- coding: utf-8 -*-
import os

from cStringIO import StringIO
from PIL import Image

from django.core.files.base import ContentFile
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile


class ImageThumbsFieldFile(ImageFieldFile):

    def __init__(self, *args, **kwargs):
        super(ImageFieldFile, self).__init__(*args, **kwargs)

    def save(self, name, content, save=True):
        # Saving uploaded original image
        super(ImageFieldFile, self).save(name, content, save)
        # Creating thumbnail
        self._generate_thumbnail(content)

    def thumbnail_url(self):
        filename, file_ext = os.path.splitext(self.name)
        thumbname = '{0}{1}{2}'.format(filename, self.field.prefix, file_ext)
        if self.storage.exists(thumbname):
            return thumbname
        return None

    def _generate_thumbnail(self, image):
        if not image:
            raise TypeError("It isn't possible to generate a thumbnail from a non-image file")

        filename, file_ext = os.path.splitext(self.name)
        thumbname = '{0}{1}{2}'.format(filename, self.field.prefix, file_ext)

        img_file = self.storage.open(self.name)
        img_file.seek(0)
        img = Image.open(img_file)

        str_io = StringIO()
        img.thumbnail(self.field.size, Image.ANTIALIAS)
        image_type = self.file.content_type.split('/')[1]
        if image_type == 'jpg':
            image_type = 'jpeg'
        img.save(str_io, image_type)
        str_io.seek(0)
        thumbnail = ContentFile(str_io.getvalue())
        self.storage.save(thumbname, thumbnail)


class ImageThumbField(ImageField):
    attr_class = ImageThumbsFieldFile

    def __init__(self, verbose_name=None, name=None, width_field=None,
                 height_field=None, size=None, prefix='_small', **kwargs):
        self.name = name
        self.verbose_name = verbose_name
        self.size = size
        self.prefix = prefix
        self.width_field = width_field
        self.height_field = height_field
        super(ImageField, self).__init__(**kwargs)
