from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()  # loads environment variables

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_words(request):
    try:
        response = supabase.table("words").select("*").execute()
        return JsonResponse({"data": response.data}, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def get_idioms(request):
    try:
        response = supabase.table("idioms").select("*").execute()
        return JsonResponse({"data": response.data}, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
