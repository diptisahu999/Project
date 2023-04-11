from django.urls import path
from UserOpeartion import views

urlpatterns = [
    path('user_register',views.employee_register,name='user_register'),
    path('employeeopr',views.EmployeeOpr.as_view(),name='employeeopr'),
    # path('operation/',views.operation)
    
    # path('emp-opr',include('UserOpeartion.urls')),

]
