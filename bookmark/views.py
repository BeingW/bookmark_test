from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark


# Create your views here.
class BookmarkList(ListView):
    #object_list 가 기본적으로 데이터 변수를 넘겨주는
    # context_oBookmarkCreateViewbject_name = 이름 정의 / 이름을 정의하면 지정한 이름으로 전달 가능
    # model 을 Bookmark 로 해주면, Bookmark 를 소문자로 바꾸어
    model = Bookmark
    paginate_by = 3


class BookmarkCreateView(CreateView):
    #모델설정
    model = Bookmark
    #모델의 fields 셋팅
    fields = ['site_name', 'url']
    #url 반응 성공시 reverse_lazy('list') 로 간다.
    success_url = reverse_lazy('list')


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')