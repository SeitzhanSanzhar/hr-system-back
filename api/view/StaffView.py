from django.http import HttpResponse, JsonResponse
from api.models import StaffToPosition, Staff, Position
from django.views.decorators.csrf import csrf_exempt
import json

def get_all_stuff(request):
    all_person = Staff.objects.all()
    json_response = {'staff':[x.to_short_json() for x in all_person]}
    print (json_response)
    # print (JsonResponse(json_response))
    return JsonResponse(json_response)

@csrf_exempt
def search_staff(request):
    #FIXME: pls resolve this problem with request type's :(
    search_value = request.GET.get('search_value')
    print(search_value)
    staff_set = Staff.objects.filter(name__startswith=search_value)
    json_response = {'staff': [x.to_short_json() for x in staff_set]}
    print (json_response)
    return JsonResponse(json_response)

def get_stuff(request):
    print ("OK")
    staff_id = request.GET.get('staff_id')
    all_person = Staff.objects.get(id = staff_id)
    json_response = all_person.to_json()
    print (json_response)
    # print (JsonResponse(json_response))
    return JsonResponse(json_response)

