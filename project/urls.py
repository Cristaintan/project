
from django.contrib import admin
from django.urls import path, include
from MyApp import views as App_views
# 路由设计
urlpatterns = [
    path('MyApp/',include('MyApp.urls')),
    path('admin/', admin.site.urls),
    path('new_login/', App_views.new_login),
    path('patient_manage/',App_views.patient_manage),
    path('work_time_search/', App_views.work_time_search),
    path('out_hospital/', App_views.out_hospital),
    path('exit/', App_views.exit),
    path('return1/', App_views.return1),
    path('return2/',App_views.return2),
    path('return3/',App_views.return3),
    path('return4/', App_views.return4),
    path('return5/', App_views.return5),
    path('return6/', App_views.return6),
    path('distribute_room/', App_views.distribute_room),
    path('doctor_choose/', App_views.doctor_choose),
    path('display/', App_views.display),
    path('insert_deal_method/', App_views.insert_deal_method),
    path('search_room/', App_views.search_room),
    path('display/', App_views.display),
    path('choose/', App_views.choose),
    path('guahao/', App_views.guahao),
    path('search_p/', App_views.search_p),
    path('search_d/', App_views.search_d),
    path('medicine/', App_views.medicine),
    path('add_patient/', App_views.add_patient),
    path('search_by_patient_name/', App_views.search_by_patient_name),
    path('search_by_patient_dept/', App_views.search_by_patient_dept),
    path('diagnosis_detail/', App_views.diagnosis_detail),
    path('search_by_doctor_name/', App_views.search_by_doctor_name),
    path('search_by_doctor_dept/', App_views.search_by_doctor_dept),
    path('search_medicine/', App_views.search_medicine),
    path('take_medicine/', App_views.take_medicine),
    path('add_medicine/', App_views.add_medicine),
    path('alter/', App_views.alter),
    path('back1/', App_views.back1),
    path('back2/', App_views.back2),
    path('back3/', App_views.back3),
    path('back4/', App_views.back4),
    path('work1/', App_views.work1),
    path('work2/', App_views.work2),
    path('doctor_login/', App_views.doctor_login),
    path('alter_work_time/', App_views.alter_work_time),
    path('add_medicine_type/', App_views.add_medicine_type),
    path('doctor_regist/', App_views.doctor_regist),
    path('', App_views.new_login),
]

