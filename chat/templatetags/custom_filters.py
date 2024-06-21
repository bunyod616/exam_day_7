from django import template

register = template.Library()

@register.filter
def is_image(file_url):
    return file_url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

@register.filter
def is_video(file_url):
    return file_url.lower().endswith(('.mp4', '.avi', '.mov', '.wmv'))

@register.filter
def is_audio(file_url):
    return file_url.lower().endswith(('.mp3', '.wav', '.ogg'))
