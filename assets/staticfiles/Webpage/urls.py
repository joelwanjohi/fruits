from django.urls import path,include
from . import views


urlpatterns = [

  path('accounts/', include('django.contrib.auth.urls')),
  path('signup/',views.signup,name='signup'),
  path('',views.home,name='home'),
  path('images/',views.images,name='display_images'),
  path('multiple/',views.multiple,name='multiple_tabs'),
  path('menu/',views.menu_items,name='menu_bar'),
  path('slider/',views.slider,name='slider'),
  path('autocomplete/',views.autocomplete,name='autocomplete'),
  path('collapsable/',views.collapse,name='collapsecontent'),
  path('tooltip/',views.tooltip,name='tooltip'),
  path('popup/',views.popups,name='display_popup'),
  path('links/',views.links,name='Website_links'),
  path('css/',views.cssprop,name='cssprop'),
  path('iframe/',views.iframe,name='iframe'),
  path('create/',views.create_employe,name='create_emp'),
  path('details/',views.show_details,name='show_detail'),
  path('delete_data/<int:id>/',views.delete_data,name='delete_dataa'),
  path('<int:id>/',views.update_date,name='update_data'),
  path('search/', views.search_employees, name='search_employees'),
  
  

]