from django.http import HttpResponse, JsonResponse
from api.models import StaffToPosition, Staff, Position


def get_all_stuff(request):
    all_person = Staff.objects.all()
    json_response = {'staff':[x.to_short_json() for x in all_person]}
    print (json_response)
    # print (JsonResponse(json_response))
    return JsonResponse(json_response)

def get_stuff(request):
    all_person = Staff.objects.all()
    json_response = {'staff':[x.to_short_json() for x in all_person]}
    print (json_response)
    # print (JsonResponse(json_response))
    return JsonResponse(json_response)

