from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json, jsonschema
from . models import Info
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return JsonResponse({"message" : "This is Info page"})

def all_info(request):
    required_info = Info.objects.values('info_id', 'title', 'desc', 'url', 'marketplace', 'blockchain', 'category', 'supply', 'private_mint_price', 'public_mint_price', 'private_mint_time', 'public_mint_time', 'private_mint_date', 'public_mint_date', 'verified', 'flagged', 'reported')
    context = {"data" : list(required_info)}
    return JsonResponse(context, safe=False)

def get_info(request, info_id):
    # Info.objects.values('info_id', 'title', 'desc', 'url', 'marketplace', 'blockchain', 'category', 'supply', 'private_mint_price', 'public_mint_price', 'private_mint_time', 'public_mint_time', 'private_mint_date', 'public_mint_date', 'verified', 'flagged', 'reported')
    required_info = Info.objects.filter(info_id = info_id).values()
    if (len(required_info) == 0):
        context = {"response_code" : 400, "response": "error", "message": "No Info exists for the given info_id"}
        return JsonResponse(context)

    if request.method == "POST":
        return JsonResponse({"response_code" : 500, "response" : "error", "message" : "POST Method not allowed"})
    
    context = {"data" : list(required_info)}
    return JsonResponse(context, safe=False)

@csrf_exempt
def update_info(request, info_id):
    if request.method == "POST":
        try:
            required_info = Info.objects.get(info_id=info_id)
        except:
            return JsonResponse({"error" : "No Info Exists for the given info id"})
        # Assuming the Frontend Developer sends the field with current key and values
        for key, value in request.POST.items():
            setattr(required_info, key, value)

        required_info.save()
        context = {"response" : "Success", "message" : "Data Updated Successfully"}
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse({"response_code": 500, "response" : "error", "message" : "Only POST Method Allowed"})

@csrf_exempt
def delete_info(request, info_id):
    if request.method == "POST":
        try:
            required_info = Info.objects.get(info_id=info_id)
        except:
            return JsonResponse({"error" : "No Info Exists for the given info id"})
        # Assuming the Frontend Developer sends the field with current key and values
        required_info.delete()
        context = {"response" : "Success", "message" : "Data Deleted Successfully"}
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse({"response_code": 500, "response" : "error", "message" : "Only POST Method Allowed"})

@csrf_exempt
def add_info(request):
    if request.method == "POST":
        try:
            required_info = Info.objects.create()
            # Assuming the Frontend Developer sends the field with current key and values
            for key, value in request.POST.items():
                setattr(required_info, key, value)
        except:
            return JsonResponse({"error" : "Failed to insert the data"})

        required_info.save()
        context = {"response" : "Success", "message" : "Data Added Successfully"}
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse({"response_code": 500, "response" : "error", "message" : "Only POST Method Allowed"})

def search(request):
    pass