from django.utils.text import slugify
import random
import string
from . import models


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def artist_unique_slug_generator(instance, new_slug=None):
    print('gak')
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    print(qs_exists)
    if qs_exists:
        print('gak')
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return artist_unique_slug_generator(instance, new_slug=new_slug)
    return slug


def song_unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = "{name}-{artist}".format(
            name=slugify(instance.name),
            artist=slugify(instance.artist)
        )
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                slug=slug,
                randstr=random_string_generator(size=4)
            )
            return song_unique_slug_generator(instance, new_slug=new_slug)
    return slug








# def unique_slug_generator(instance, new_slug=None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.name)
#
#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug=slug).exists()
#     if qs_exists:
#         if Klass == 'Artist':
#             new_slug = "{slug}-{randstr}".format(
#                 slug=slug,
#                 randstr=random_string_generator(size=4)
#             )
#             return unique_slug_generator(instance, new_slug=new_slug)
#     if Klass == 'Song':
#         new_slug = "{slug}-{artist}".format(
#             slug=slug,
#             artist=instance.artist.name
#             )
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug

