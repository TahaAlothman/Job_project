from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer
from .models import Job

# @api_view(['GET'])
# def job_list_api(request):
#    jobs = Job.objects.all()
#    data = JobSerializer(jobs,many=True,context={'request':request}).data   #json
#    return Response({'jobs':data})

class JobListAPI(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all() 

# @api_view(['GET'])
# def job_detail_api(request,job_id):
#     job =  Job.objects.get(id = job_id)
#     data = JobSerializer(job,context={'request':request}).data   #json
#     return Response({'jobs':data})

class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all() 