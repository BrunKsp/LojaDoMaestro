
from django.urls import path 
from produtos.views import ProdutoView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',ProdutoView.listaProd,name = "produto-list"),
    path('produto/<int:id>',ProdutoView.produtoView,name = "produto-view"),
    path('newproduto/', ProdutoView.newProduto, name="new-produto"),
    path('edit/<int:id>',ProdutoView.editProduto,name = "edit-produto"),
    path('delete/<int:id>',ProdutoView.deleteProduto,name = "delete-produto"),
  
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)