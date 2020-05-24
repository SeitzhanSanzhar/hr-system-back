from django.http import HttpResponse, JsonResponse
from api.models import StaffToPosition, Staff, Position
import json


def get_all_stuff(request):
    all_person = Staff.objects.all()
    json_response = {'staff':[x.to_short_json() for x in all_person]}
    print (json_response)
    # print (JsonResponse(json_response))
    return JsonResponse(json_response)

def search_staff(request):
    in_json  = json.loads(request.body)
    search_value = in_json.get('search_value', '')
    print(search_value)
    staff_set = Staff.objects.filter(name__startswith=search_value)
    json_response = {'staff': [x.to_short_json() for x in staff_set]}
    return JsonResponse(json_response)

def get_stuff(request):
    all_person = Staff.objects.all()
    json_response = {'staff':[x.to_short_json() for x in all_person]}
    print (json_response)
    # print (JsonResponse(json_response))
    return JsonResponse(json_response)

