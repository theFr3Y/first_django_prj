from django.http import Http404
from django.shortcuts import get_object_or_404
from webapp.models import PostModel
class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'content', 'slug', 'thumbnail', 'status', 'author']
        elif request.user.is_author:
            self.fields = ['title', 'content', 'slug', 'thumbnail']
        else:
            raise Http404('you cant see this page...')
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save()
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super(FormValidMixin, self).form_valid(form)

class AuthoraccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(PostModel, pk=pk)
        if article.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('you cant see this page...')

class SuperuserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('you cant see this page...')
