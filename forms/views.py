from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from datetime import datetime,timedelta
import json
from pyauth.auth import HasRoleAndDataPermission
from .auth.permissions import SkipPermissionsIfDisabled

from .forms import RegisterSerializer
@api_view(['POST'])
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def registration(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Register
@api_view(['POST'])
@csrf_exempt  
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def login(request):
    if request.method == 'POST':
        employee_id = request.data.get('employeeId')       
        password = request.data.get('password')
        try:
            user = Register.objects.get(id=employee_id, password=password)
            if request.data.get('endpoint') == 'AdminLogin' and user.role != 'Admin':
                return Response('Access denied', status=status.HTTP_403_FORBIDDEN)

            return Response({'message': 'Login successful', 'role': user.role, 'id': user.id, 'name': user.name}, status=status.HTTP_200_OK)
        except Register.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


from .forms import FrontOfficeSerializer
@api_view(['POST'])
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def frontoffice_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if FrontOffice.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = FrontOfficeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstFloorSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def firstfloor_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if FirstFloor.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = FirstFloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SecondFloorSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def secondfloor_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if SecondFloor.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = SecondFloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import ThirdFloorSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def thirdfloor_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if ThirdFloor.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = ThirdFloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstSuitSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def firstsuit_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if FirstSuit.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = FirstSuitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SecondSuitSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def secondsuit_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if SecondSuit.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = SecondSuitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import LabSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def lab_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Lab.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = LabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import CTSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def CT_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if CT.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = CTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import MRISerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def MRI_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if MRI.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = MRISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import XraySerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def Xray_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Xray.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = XraySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OPDSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def OPD_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if OPD.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = OPDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OTSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def OT_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if OT.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = OTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import HRSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def HR_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if HR.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = HRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import PhysiotherapySerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def physiotherapy_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Physiotherapy.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = PhysiotherapySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import DialysisSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def dialysis_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Dialysis.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = DialysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
from .forms import EmergencyRoomSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def emergency_room_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if EmergencyRoom.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = EmergencyRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import MRDSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def MRD_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if MRD.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = MRDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
from .forms import ChemoWardSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def chemo_ward_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if ChemoWard.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = ChemoWardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import RecoveryWardSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def recovery_ward_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if RecoveryWard.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = RecoveryWardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SICUSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def SICU_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if SICU.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = SICUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import MICUSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def MICU_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if MICU.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = MICUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
from .forms import NICUSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def NICU_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if NICU.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = NICUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import FirstFloorRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def firstfloor_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if FirstFloorRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = FirstFloorRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import FirstSuitRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def firstsuit_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if FirstSuitRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = FirstSuitRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import SecondFloorRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def secondfloor_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if SecondFloorRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = SecondFloorRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import SecondSuitRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def secondsuit_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if SecondSuitRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = SecondSuitRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
from .forms import ThirdFloorRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def thirdfloor_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if ThirdFloorRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = ThirdFloorRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import SICURawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def sicu_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if SICURawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = SICURawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import MICURawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def micu_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if MICURawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = MICURawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
from .forms import NICURawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def nicu_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if NICURawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = NICURawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import EmergencyRoomRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def emergencyroom_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if EmergencyRoomRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = EmergencyRoomRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import ChemoWardRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def chemoward_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if ChemoWardRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = ChemoWardRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import RecoverywardRawDataSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def recoveryward_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        # Check if data for the selected date already exists
        if RecoverywardRawData.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = RecoverywardRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

from datetime import datetime
import calendar
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def get_export_data(request):
    if request.method == 'GET':
        ward = request.GET.get('ward')
        year = request.GET.get('year')
        month = request.GET.get('month')
        date = request.GET.get('date')

        query_params = {}

        if ward and date:
            query_params['ward'] = ward
            parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").date()  # Convert to proper date
            query_params['selectedDate'] = parsed_date

        if ward and year and month:
            year = int(year)
            month = int(month)

            # Ensure start_date is 1st of the month
            start_date = datetime(year, month, 1).date()

            # Get the last day of the month
            last_day = calendar.monthrange(year, month)[1]
            end_date = datetime(year, month, last_day).date()  # Ensure it's just date, not datetime

            query_params['ward'] = ward
            query_params['selectedDate__gte'] = start_date
            query_params['selectedDate__lte'] = end_date  # Ensure last day is included

        if query_params:
            try:
                selected_model = get_ward_model(ward)
                data = selected_model.objects.filter(**query_params).values()
                return JsonResponse(list(data), safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Please select a ward, year, and month'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

@csrf_exempt
def delete_export_data(request):
    if request.method == 'DELETE':
        date = request.GET.get('date')
        ward = request.GET.get('ward')
        if not date or not ward:
            return JsonResponse({'error': 'Date and Ward are required'}, status=400)
        try:
            selected_model = get_ward_model(ward)
            # Try parsing the date in multiple formats
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").date()  # ISO 8601
            except ValueError:
                try:
                    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()  # YYYY-MM-DD
                except ValueError:
                    return JsonResponse({'error': 'Invalid date format'}, status=400)
            deleted_count, _ = selected_model.objects.filter(selectedDate=parsed_date).delete()
            if deleted_count > 0:
                return JsonResponse({'message': 'Data deleted successfully'})
            else:
                return JsonResponse({'error': 'No matching data found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
@csrf_exempt
def delete_export_rawdata(request):
    if request.method == 'DELETE':
        date = request.GET.get('date')
        ward = request.GET.get('ward')
        if not date or not ward:
            return JsonResponse({'error': 'Date and Ward are required'}, status=400)
        try:
            selected_model = get_rawdata_model(ward)
            # Try parsing the date in multiple formats
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").date()  # ISO 8601
            except ValueError:
                try:
                    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()  # YYYY-MM-DD
                except ValueError:
                    return JsonResponse({'error': 'Invalid date format'}, status=400)
            deleted_count, _ = selected_model.objects.filter(selectedDate=parsed_date).delete()
            if deleted_count > 0:
                return JsonResponse({'message': 'Data deleted successfully'})
            else:
                return JsonResponse({'error': 'No matching data found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
  

@csrf_exempt
def update_export_data(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            for row in data:
                selected_date = datetime.strptime(row.get('selectedDate'), "%Y-%m-%dT%H:%M:%S.%fZ").date()
                ward = row.get('ward')
                selected_model = get_ward_model(ward)

                try:
                    # Update the record based on selected_date
                    existing_instance = selected_model.objects.get(selectedDate=selected_date)
                except selected_model.DoesNotExist:
                    return JsonResponse({'error': f'Instance with selectedDate {selected_date} does not exist'}, status=404)
                
                for key, value in row.items():
                    if key not in ['_id', 'ward', 'selectedDate']:
                        setattr(existing_instance, key, value)
                existing_instance.save()
                
            return JsonResponse({'success': 'Data updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=405)
    

@csrf_exempt
def get_export_rawdata(request):
    if request.method == 'GET':
        ward = request.GET.get('ward')
        year = request.GET.get('year')
        month = request.GET.get('month')
        date = request.GET.get('date')
        
        query_params = {}

        if ward and date:
            query_params['ward'] = ward
            parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            query_params['selectedDate'] = parsed_date.date()

        if ward and year and month:
            start_date = datetime(int(year), int(month), 1)
            end_date = start_date.replace(day=1, month=int(month)+1) if int(month) < 12 else start_date.replace(year=int(year)+1, month=1)
            query_params['ward'] = ward
            query_params['selectedDate__gte'] = start_date
            query_params['selectedDate__lt'] = end_date

        if query_params:
            try:
                selected_model = get_rawdata_model(ward)
                data = selected_model.objects.filter(**query_params).values()
                return JsonResponse(list(data), safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Please select a ward, year, and month'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    

@csrf_exempt
def update_export_rawdata(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            for row in data:
                selected_date = datetime.strptime(row.get('selectedDate'), "%Y-%m-%dT%H:%M:%S.%fZ").date()
                ward = row.get('ward')
                selected_model = get_rawdata_model(ward)
                try:
                    # Update the record based on selected_date
                    existing_instance = selected_model.objects.get(selectedDate=selected_date)
                except selected_model.DoesNotExist:
                    return JsonResponse({'error': f'Instance with selectedDate {selected_date} does not exist'}, status=404)
                for key, value in row.items():
                    if key not in ['_id', 'ward', 'selectedDate']:
                        setattr(existing_instance, key, value)
                existing_instance.save()
            return JsonResponse({'success': 'Data updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=405)


from .constant import floor_beds
def availabilityofroomsandbeds(request, ward):
    try:
        # Get the corresponding model class based on the selected ward
        selected_model = get_ward_model(ward)
        if selected_model:
            # Query the selected model for occupancy date
            yesterday = (datetime.today() - timedelta(days=1)).date()
            form_data = selected_model.objects.filter(selectedDate=yesterday).first()
            occupied_beds = int(form_data.numberOfBedsOccupied) if form_data else 0
            
            # Logging for debugging
            print('Yesterday:', yesterday)
            print('Form Data:', form_data)
            if form_data:
                print('Occupied Beds:', form_data.numberOfBedsOccupied)
            else:
                print('No data found for the given date.')
            
        else:
            return JsonResponse({'error': 'Ward type not recognized'}, status=400)

        # Calculate the number of available beds using data from constants.py
        total_beds = floor_beds.get(ward, 0)
        available_beds = total_beds - occupied_beds

        # Return the data in JSON format
        return JsonResponse({
            'ward': ward,
            'numberOfBedsOccupied': occupied_beds,
            'numberOfBedsAvailable': available_beds
        })

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error: {e}")
        # Return a more descriptive error message
        return JsonResponse({'error': 'An error occurred while processing your request'}, status=500)
    

from .models import FrontOffice,FirstFloor,FirstSuit,SecondFloor,SecondSuit,ThirdFloor,Lab,CT,MRI,Xray,Pharmacy
from .models import OT,MRD,MICU,NICU,SICU,RecoveryWard,ChemoWard,Physiotherapy,Dialysis,EmergencyRoom,OPD,HR 
def get_ward_model(ward):
    ward_model_map = {
        'Front Office': FrontOffice,
        "HR": HR,
        'First Floor': FirstFloor,
        'First Suit': FirstSuit,
        'Second Floor': SecondFloor,
        'Second Suit': SecondSuit,
        'Third Floor': ThirdFloor,
        'Lab': Lab,
        'CT': CT,
        'MRI': MRI,
        'X-Ray': Xray,
        'OT': OT,
        'MRD': MRD,
        'MICU': MICU,
        'NICU': NICU,
        'SICU': SICU,
        'Recovery ward': RecoveryWard,
        'Chemo Ward': ChemoWard,
        'Physiotherapy': Physiotherapy,
        'Dialysis': Dialysis,
        'ER': EmergencyRoom,
        'OPD': OPD,
        'Pharmacy': Pharmacy, 
        'MockDrill': MockDrill,     

    }
    selected_model = ward_model_map.get(ward, None)
    if selected_model:
        return selected_model
    else:
        raise ValueError('Ward type not recognized')
    

from .models import FirstFloorRawData,SecondFloorRawData,SecondSuitRawData,FirstSuitRawData,ThirdFloorRawData 
from .models import NICURawData,MICURawData,SICURawData,EmergencyRoomRawData,RecoverywardRawData,ChemoWardRawData 
def get_rawdata_model(ward):
    rawdata_model_map = {
        'First Floor Raw Data': FirstFloorRawData,
        'First Suit Raw Data': FirstSuitRawData,
        'Second Floor Raw Data': SecondFloorRawData,
        'Second Suit Raw Data': SecondSuitRawData,
        'Third Floor Raw Data': ThirdFloorRawData,
        'SICU Raw Data': SICURawData,
        'MICU Raw Data': MICURawData,
        'NICU Raw Data': NICURawData,
        'EmergencyRoom Raw Data': EmergencyRoomRawData,
        'Recoveryward Raw Data': RecoverywardRawData,
        'ChemoWard Raw Data': ChemoWardRawData,
    }
    selected_rawdata_model = rawdata_model_map.get(ward, None)
    if selected_rawdata_model:
        return selected_rawdata_model
    else:
        raise ValueError('Ward type not recognized')



from .models import HandHygenieAudit  # make sure this is the model
from .forms import HandHygenieAuditSerializer

@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def HandHygenieAuditView(request):
    if request.method == 'POST':        
        serializer = HandHygenieAuditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def get_all_hand_hygiene_data(request):
    audits = HandHygenieAudit.objects.all()
    serializer = HandHygenieAuditSerializer(audits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

from .models import TrainingFeedBack  # make sure this is the model
from .forms import TrainingFeedBackSerializer

@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def TrainingFeedBackView(request):
    if request.method == 'POST':
        name = request.data.get('name')
        selected_date = request.data.get('selectedDate')

        if TrainingFeedBack.objects.filter(name=name, selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date and name.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TrainingFeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET'])
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def get_all_training_feedback(request):
    audits = TrainingFeedBack.objects.all()
    serializer = TrainingFeedBackSerializer(audits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import (
    FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit,
    Lab, CT, MRI, Xray, OPD, OT, Physiotherapy, Dialysis,
    EmergencyRoom, ChemoWard, RecoveryWard, SICU, MICU, NICU, Pharmacy,
    MockDrill, HandHygenieAudit, MRD
)

def get_filtered_data(model, year, month, date_field='selectedDate'):
    month_str = f"{int(month):02}"  # ensures '04' format
    return [
        model_to_dict(obj)
        for obj in model.objects.all()
        if getattr(obj, date_field) and
           getattr(obj, date_field)[:4] == str(year) and
           getattr(obj, date_field)[5:7] == month_str
    ]


def get_formula_data(request):
    year = request.GET.get('year')
    month = request.GET.get('month')

    if not year or not month:
        return JsonResponse({'error': 'Missing year or month'}, status=400)

    try:
        year = int(year)
        month = int(month)
    except ValueError:
        return JsonResponse({'error': 'Invalid year or month format'}, status=400)

    data = {
        'first_floor': get_filtered_data(FirstFloor, year, month),
        'second_floor': get_filtered_data(SecondFloor, year, month),
        'third_floor': get_filtered_data(ThirdFloor, year, month),
        'first_suit': get_filtered_data(FirstSuit, year, month),
        'second_suit': get_filtered_data(SecondSuit, year, month),
        'lab': get_filtered_data(Lab, year, month),
        'ct': get_filtered_data(CT, year, month),
        'mri': get_filtered_data(MRI, year, month),
        'xray': get_filtered_data(Xray, year, month),
        'opd': get_filtered_data(OPD, year, month),
        'ot': get_filtered_data(OT, year, month),
        'physiotherapy': get_filtered_data(Physiotherapy, year, month),
        'dialysis': get_filtered_data(Dialysis, year, month),
        'emergency_room': get_filtered_data(EmergencyRoom, year, month),
        'chemo_ward': get_filtered_data(ChemoWard, year, month),
        'recovery_ward': get_filtered_data(RecoveryWard, year, month),
        'sicu': get_filtered_data(SICU, year, month),
        'micu': get_filtered_data(MICU, year, month),
        'nicu': get_filtered_data(NICU, year, month),
        'pharmacy': get_filtered_data(Pharmacy, year, month),
        'mockdrill': get_filtered_data(MockDrill, year, month),
        'hand_hygenie_audit': get_filtered_data(HandHygenieAudit, year, month),
        'mrd': get_filtered_data(MRD, year, month),
    }

    return JsonResponse(data, safe=False)



from .forms import PharmacySerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def Pharmacy_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        # Check if data for the selected date already exists
        if RecoveryWard.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        # If no existing data, proceed with saving
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MockDrill
from .forms import MockDrillSerializer
@api_view(['POST'])
@permission_classes([SkipPermissionsIfDisabled, HasRoleAndDataPermission])
def create_mockdrill(request):
    serializer = MockDrillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
