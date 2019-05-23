from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo
# Create your views here.

class IndexView(View):

    def get(self,request):
        return render(request,'address.html')

class AddressAPI(View):

    def get_index_page(request,address_id):

        if int(address_id) == 0:
            address_data = AddressInfo.objects.filter(pid_isnull = True).values('id','address')
        else:
            address_data = AddressInfo.objects.filter(pid_id=int(address_id)).values('id','address')
        area_list = []
        for a in address_data:
            area_list.append({'id':a['id'],'address':a['address']})
        
        return JsonResponse(area_list,content_type='application/json',safe=False)





