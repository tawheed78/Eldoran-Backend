from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Info
from .serializers import InfoSerializer, TrendSerializer, SearchSerializer
from django.http import Http404
from django.db.models import Q

# ViewSet for CRUD operations
class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

# APIView for listing and creating Info
class InfoList(APIView):
    def get(self, request):
        infos = Info.objects.all()
        serializer = InfoSerializer(infos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView for retrieving, updating, and deleting Info
class InfoDetail(APIView):
    def get_object(self, pk):
        try:
            return Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        info = self.get_object(pk)
        info.click_count += 1
        info.save()
        serializer = InfoSerializer(info)
        return Response(serializer.data)

    def put(self, request, pk):
        info = self.get_object(pk)
        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        info = self.get_object(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class SearchView(APIView):
    model = Info
    def get(self, request):
        query = self.request.GET.get("q")
        if query:
            object_list = Info.objects.filter(
            Q(title__icontains=query) | Q(desc__icontains=query))
        else:
            object_list = Info.objects.none()
        serializer = SearchSerializer(object_list, many=True)
        return Response(serializer.data)
    

    

class Trends(APIView):
    def get(self, request):
        paid_nfts = Info.objects.filter(paid_status=True)
        if len(paid_nfts)<=5:
            trending_nfts = Info.objects.filter(~Q(info_id__in=paid_nfts)).order_by('-click_count')[:10]
        combined_nfts = list(paid_nfts) + list(trending_nfts) if trending_nfts else []
        serializer = TrendSerializer(combined_nfts, many=True)
        return Response(serializer.data)


