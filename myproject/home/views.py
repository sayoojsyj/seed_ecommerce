# from django.shortcuts import render
# from django.views import View
# from accounts.models import CustomUser
# # from django.views.decorators.cache import never_cache
# # from django.utils.decorators import method_decorator

# # Create your views here.



# # def index(request):
# #     return render(request,'index.html')

# # @method_decorator(never_cache, name='dispatch')
# class IndexView(View):
#     template_name = 'index.html'

#     def get(self, request):
#         return render(request, self.template_name)
    
    
# def current_user (request):
#     user_name = CustomUser.objects.all()
#     context = {'username' : user_name}
#     return render ( 'index.html' , context )
    
    