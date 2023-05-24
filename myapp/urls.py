from django.urls import path
from . import views
from .views import progress_view
from django.urls import include

urlpatterns = [
    path('caap_ap',views.index),
    path('view/<int:id>',views.viewProject),
    path('show/<int:id>',views.showView),
    path('dashboard',views.dashView),
    path('',views.login_view),
    # path('search',views.searchView),   
    path('logout',views.logout_view),    
    path('info/', views.infoView),
    path('addnew',views.addnew),
    path('complete-projects',views.complete_projects),
    path('ongoing-projects',views.ongoing_projects),
    path('procurement-projects',views.procurement_projects),
    path('edit/<int:id>', views.edit),  
    path('delete/<int:id>', views.destroy),  
    path('update/<int:id>', views.update),  

    path('progress/', views.progress_view),

    
]
