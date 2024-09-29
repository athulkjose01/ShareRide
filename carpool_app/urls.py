from django.urls import path
from . import views
from.views import GiveRidesView, LoginView, LogoutView, MyAccountView, RideGiverUpdateView, complete_ride, join_ride, predict_cost, register, save_ride_giver, withdraw_money

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/',register, name = "register"),
    path('', views.home, name='home'),
    path('save-route/', views.save_route, name='save_route'),
    path('give-rides/', GiveRidesView.as_view(), name='give_rides'),
    path('show-polyline/', views.show_polyline, name='show_polyline'),
    path('get-coordinates/', views.get_coordinates, name='get_coordinates'),
    path('save-request-route/', views.save_request_route, name='save_request_route'),
    path('show-request-polyline/', views.show_request_polyline, name='show_request_polyline'),
    path('match-rides/', views.match_rides, name='match_rides'),
    path('request-ride/', views.request_ride, name='request_ride'),
    path('ride-giver-details/', save_ride_giver, name='save_ride_giver'),
    path('ridegiver/update/', RideGiverUpdateView.as_view(), name='ridegiver_update'),
    path('view_upcoming_rides/', views.view_upcoming_rides, name='view_upcoming_rides'),
    path('accept_request/<int:request_id>/', views.accept_request, name='accept_request'),
    path('decline_request/<int:request_id>/', views.decline_request, name='decline_request'),
    path('dummy-payment/<int:request_id>/', views.dummy_payment, name='dummy_payment'),
    path('join-ride/<int:request_id>/', views.join_ride, name='join_ride'),
    path('predict_cost/', predict_cost, name='predict_cost'),
    path('mark_ride_completed/<int:request_id>/', complete_ride, name='mark_ride_completed'),
    path('my-account/', MyAccountView.as_view(), name='my_account'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('delete-ride/<int:ride_id>/', views.delete_ride, name='delete_ride'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('withdraw_money/', withdraw_money, name='withdraw_money'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('visualization/', views.visualization, name='visualization'),
    path('reports/', views.reports_view, name='reports'),
]