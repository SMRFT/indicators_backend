from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from datetime import datetime,timedelta
import json
from pyauth.auth import HasRolePermission


from .forms import RegisterSerializer
@api_view(['POST'])
@permission_classes([HasRolePermission])
def registration(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Register
@api_view(['POST'])
@csrf_exempt  
@permission_classes([HasRolePermission])
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
@permission_classes([ HasRolePermission])
def frontoffice_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if FrontOffice.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = FrontOfficeSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstFloorSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def firstfloor_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if FirstFloor.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = FirstFloorSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SecondFloorSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def secondfloor_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if SecondFloor.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = SecondFloorSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import ThirdFloorSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def thirdfloor_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if ThirdFloor.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = ThirdFloorSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstSuitSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def firstsuit_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if FirstSuit.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = FirstSuitSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SecondSuitSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def secondsuit_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if SecondSuit.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = SecondSuitSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import LabSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def lab_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Lab.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = LabSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import CTSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def CT_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if CT.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = CTSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import MRISerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def MRI_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if MRI.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = MRISerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import XraySerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def Xray_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Xray.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = XraySerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OPDSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def OPD_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if OPD.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = OPDSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OTSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def OT_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if OT.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = OTSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import HRSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def HR_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if HR.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = HRSerializer(data=request.data)
        if serializer.is_valid():
            
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import PhysiotherapySerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def physiotherapy_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Physiotherapy.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = PhysiotherapySerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import DialysisSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def dialysis_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if Dialysis.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = DialysisSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
from .forms import EmergencyRoomSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def emergency_room_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if EmergencyRoom.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = EmergencyRoomSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import MRDSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def MRD_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if MRD.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = MRDSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
from .forms import ChemoWardSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def chemo_ward_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if ChemoWard.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = ChemoWardSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import RecoveryWardSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
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
@permission_classes([ HasRolePermission])
def SICU_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if SICU.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = SICUSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import MICUSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def MICU_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if MICU.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = MICUSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
from .forms import NICUSerializer
@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
def NICU_data(request):
    if request.method == 'POST':
        selected_date = request.data.get('selectedDate')
        
        # Check if data for the selected date already exists
        if NICU.objects.filter(selectedDate=selected_date).exists():
            return Response({'error': 'Data already exists for this date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If no existing data, proceed with saving
        serializer = NICUSerializer(data=request.data)
        if serializer.is_valid():
            # Create object but don't save yet
            obj = serializer.save(commit=False)

            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Set fields manually (ModelForm cannot receive extra args)
            if not obj.created_by:
                obj.created_by = user_identifier

            obj.lastmodified_by = user_identifier

            # Save the model
            obj.save()

            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import FirstFloorRawDataSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
@permission_classes([HasRolePermission])
def firstfloor_rawdata(request):
    data = request.data

    selected_date = data.get('selectedDate')
    raw_data = data.get('raw_data', [])

    # Check if data for the selected date already exists
    if FirstFloorRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {'error': 'Data already exists for this date.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not selected_date or not raw_data:
        return Response(
            {'error': 'selectedDate and raw_data are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = FirstFloorRawDataSerializer(data=data)

    if serializer.is_valid():
        user_identifier = data.get("auth-user-id")

        obj = serializer.save(
            created_by=user_identifier,
            lastmodified_by=user_identifier
        )

        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstSuitRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def firstsuit_rawdata(request):
    data = request.data

    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if FirstSuitRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = FirstSuitRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

from .forms import SecondFloorRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def secondfloor_rawdata(request):
    data = request.data

    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if SecondFloorRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = SecondFloorRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import SecondSuitRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def secondsuit_rawdata(request):
    data = request.data

    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if SecondSuitRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = SecondSuitRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    
from .forms import ThirdFloorRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def thirdfloor_rawdata(request):
    data = request.data

    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if ThirdFloorRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ThirdFloorRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .forms import SICURawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def sicu_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response({"error": "Invalid data"}, status=400)

    if SICURawData.objects.filter(selectedDate=selected_date).exists():
        return Response({"error": "Data already exists"}, status=400)

    serializer = SICURawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response({"message": "Success"}, status=201)

    return Response(serializer.errors, status=400)

        

from .forms import MICURawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def micu_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if MICURawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = MICURawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
from .forms import NICURawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def nicu_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if NICURawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = NICURawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import EmergencyRoomRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def emergencyroom_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if EmergencyRoomRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = EmergencyRoomRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .forms import ChemoWardRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def chemoward_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if ChemoWardRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ChemoWardRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import RecoverywardRawDataSerializer
@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def recoveryward_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if RecoverywardRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = RecoverywardRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import OPDRawDataSerializer
@api_view(["POST"])
@csrf_exempt
# @permission_classes([HasRolePermission])
def opd_rawdata(request):
    data = request.data
    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if OPDRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = OPDRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from datetime import datetime
import calendar
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET'])
# @permission_classes([HasRolePermission])
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
    

from .models import OPDRawData
from .forms import OPDRawDataSerializer

@api_view(["POST"])
@csrf_exempt
@permission_classes([HasRolePermission])
def opd_rawdata(request):
    data = request.data

    selected_date = data.get("selectedDate")
    raw_data = data.get("raw_data", [])

    if not selected_date or not raw_data:
        return Response(
            {"error": "selectedDate and raw_data are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if OPDRawData.objects.filter(selectedDate=selected_date).exists():
        return Response(
            {"error": "Data already exists for this date."},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = OPDRawDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(
            created_by=data.get("auth-user-id"),
            lastmodified_by=data.get("auth-user-id")
        )
        return Response(
            {"message": "Data submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
from .models import NICURawData,MICURawData,SICURawData,EmergencyRoomRawData,RecoverywardRawData,ChemoWardRawData ,OPDRawData
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
        'OPD Raw Data': OPDRawData,

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
@permission_classes([HasRolePermission])
def HandHygenieAuditView(request):
    if request.method == 'POST':        
        serializer = HandHygenieAuditSerializer(data=request.data)
        if serializer.is_valid():
            # Get user id from request
            user_identifier = request.data.get("auth-user-id")

            # Pass extra attributes to save() instead of using commit=False
            serializer.save(
                created_by=user_identifier,
                lastmodified_by=user_identifier
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([ HasRolePermission])
def get_all_hand_hygiene_data(request):
    audits = HandHygenieAudit.objects.all()
    serializer = HandHygenieAuditSerializer(audits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

from .models import TrainingFeedBack  # make sure this is the model
from .forms import TrainingFeedBackSerializer

@api_view(['POST'])
@csrf_exempt
@permission_classes([ HasRolePermission])
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
@permission_classes([ HasRolePermission])
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
@permission_classes([ HasRolePermission])
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
@permission_classes([ HasRolePermission])
def create_mockdrill(request):
    serializer = MockDrillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


from .models import IncidentReport, SupervisorInvestigation, IncidentClassification
from .forms import IncidentReportSerializer, SupervisorInvestigationSerializer

@api_view(['POST', 'GET'])
@csrf_exempt
@permission_classes([HasRolePermission])
def IncidentReportView(request):
    if request.method == 'POST':
        # Copy data so we can mutate it
        data = request.data.copy() if hasattr(request.data, 'copy') else dict(request.data)
        
        # Generate incidentNo in view
        from datetime import datetime
        current_year = datetime.now().year
        prefix = f"INC-{current_year}-"
        
        last_incident = IncidentReport.objects.filter(incidentNo__startswith=prefix).order_by('-incidentNo').first()
        if last_incident and last_incident.incidentNo:
            try:
                last_num = int(last_incident.incidentNo.split('-')[-1])
                next_num = last_num + 1
            except (ValueError, IndexError):
                next_num = 1
        else:
            next_num = 1
            
        incident_no = f"{prefix}{next_num:04d}"
        data['incidentNo'] = incident_no

        serializer = IncidentReportSerializer(data=data)
        if serializer.is_valid():
            user_identifier = data.get("auth-user-id")
            serializer.save(
                created_by=user_identifier,
                lastmodified_by=user_identifier
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        incidents = IncidentReport.objects.all()
        start_date = request.GET.get('startDate')
        end_date = request.GET.get('endDate')
        if not start_date and not end_date:
            from datetime import datetime, timedelta
            thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            incidents = incidents.filter(incidentDate__gte=thirty_days_ago)
        else:
            if start_date:
                incidents = incidents.filter(incidentDate__gte=start_date)
            if end_date:
                incidents = incidents.filter(incidentDate__lte=end_date)
        incidents = incidents.order_by('-incidentDate')
        serializer = IncidentReportSerializer(incidents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def get_next_incident_no(request):
    from datetime import datetime
    current_year = datetime.now().year
    prefix = f"INC-{current_year}-"
    
    last_incident = IncidentReport.objects.filter(incidentNo__startswith=prefix).order_by('-incidentNo').first()
    if last_incident and last_incident.incidentNo:
        try:
            last_num = int(last_incident.incidentNo.split('-')[-1])
            next_num = last_num + 1
        except (ValueError, IndexError):
            next_num = 1
    else:
        next_num = 1
        
    incident_no = f"{prefix}{next_num:04d}"
    return Response({"nextIncidentNo": incident_no}, status=status.HTTP_200_OK)


def get_user_profile_role_and_details(user_identifier):
    """
    Queries the backend_diagnostics_profile collection in the Global database
    and determines the user's role and details (name, department, etc.)
    """
    from django.conf import settings
    import pymongo

    try:
        db_config = settings.DATABASES['default']
        host = db_config.get('CLIENT', {}).get('host', 'mongodb://localhost:27017/')
        client = pymongo.MongoClient(host)
        db = client['Global']
        profile = db['backend_diagnostics_profile'].find_one({'employeeId': str(user_identifier)})
        if profile:
            primary_role = profile.get('primaryRole') or ''
            additional_roles = profile.get('additionalRoles') or []
            
            # Combine all roles
            all_roles = [primary_role] + additional_roles
            
            # Determine role based on action / role codes:
            # SI-R-IND -> Admin
            # SI-R-INDIN -> In-Charge
            # SI-R-INDE -> Employee
            role = 'Employee'
            if any('SI-R-IND' in r and 'SI-R-INDIN' not in r and 'SI-R-INDE' not in r for r in all_roles):
                role = 'Admin'
            elif any('SI-R-INDIN' in r for r in all_roles):
                role = 'In-Charge'
            elif any('SI-R-INDE' in r for r in all_roles):
                role = 'Employee'
            else:
                # If not matched, fallback to checking if "Admin" or "In-Charge" is in the role names
                if any('ADM' in r or 'Admin' in r for r in all_roles):
                    role = 'Admin'
                elif any('IND' in r or 'In-Charge' in r or 'Incharge' in r for r in all_roles):
                    role = 'In-Charge'
            
            dept_code = profile.get('department') or ''
            dept_name = dept_code
            if dept_code:
                try:
                    dept_doc = db['backend_diagnostics_Departments'].find_one({'department_code': str(dept_code)})
                    if dept_doc and dept_doc.get('department_name'):
                        dept_name = dept_doc.get('department_name')
                except Exception as e:
                    print(f"Error querying department name: {e}")
            
            return {
                'role': role,
                'name': profile.get('employeeName') or '',
                'department': dept_name,
                'designation': profile.get('designation') or ''
            }
    except Exception as e:
        print(f"Error querying profile: {e}")
    
    # Fallback to local Register model
    try:
        from .models import Register
        user = Register.objects.get(id=str(user_identifier))
        dept_code = user.department or ''
        dept_name = dept_code
        if dept_code:
            try:
                db_config = settings.DATABASES['default']
                host = db_config.get('CLIENT', {}).get('host', 'mongodb://localhost:27017/')
                client = pymongo.MongoClient(host)
                db = client['Global']
                dept_doc = db['backend_diagnostics_Departments'].find_one({'department_code': str(dept_code)})
                if dept_doc and dept_doc.get('department_name'):
                    dept_name = dept_doc.get('department_name')
                    print(f"Department name: {dept_name}")
            except Exception:
                pass
        return {
            'role': user.role,
            'name': user.name,
            'department': dept_name,
            'designation': ''
        }
    except Exception:
        pass
        
    return {
        'role': 'Employee',
        'name': '',
        'department': '',
        'designation': ''
    }


@api_view(['POST', 'GET'])
@csrf_exempt
@permission_classes([HasRolePermission])
def SupervisorInvestigationView(request):
    if request.method == 'POST':
        incident_id = request.data.get("incidentId")
        existing = SupervisorInvestigation.objects.filter(incidentId=incident_id).first()
        
        user_identifier = request.data.get("auth-user-id")
        profile_data = get_user_profile_role_and_details(user_identifier)
        
        # Determine user role from JWT token or fallback to profile database role
        user_role = None
        import jwt
        auth_header = request.headers.get('Authorization') or request.META.get('HTTP_AUTHORIZATION') or ''
        if auth_header:
            token = auth_header.split(' ')[-1] if ' ' in auth_header else auth_header
            try:
                payload = jwt.decode(token, options={"verify_signature": False})
                allowed_actions = payload.get('allowed-actions') or payload.get('allowedActions') or payload.get('allowed_actions') or []
                if 'SI-R-IND' in allowed_actions:
                    user_role = 'Admin'
                elif 'SI-R-INDIN' in allowed_actions:
                    user_role = 'In-Charge'
                elif 'SI-R-INDE' in allowed_actions:
                    user_role = 'Employee'
            except Exception as e:
                print(f"Error decoding JWT token for role: {e}")
        
        if not user_role:
            user_role = profile_data.get('role', '')
        
        # Enforce role-based field restrictions
        quality_fields = [
            'qualityReceivedBy', 'qualityReceivedDeptDesignation', 'qualityReceivedDateTime', 
            'qualityClassification', 'qualityRemarks', 'qualityVerifiedByHead', 'qualityVerifiedDateTime',
            'qualityReceivedSignatureEmpId'
        ]
        incharge_fields = [
            'why1', 'why2', 'why3', 'why4', 'why5',
            'investigationName', 'investigationDeptDesignation', 'investigationSignatureEmpId', 'investigationDateTime',
            'correctiveAction', 'correctiveName', 'correctiveDeptDesignation', 'correctiveSignatureEmpId', 'correctiveDateTime',
            'preventiveAction', 'preventiveName', 'preventiveDeptDesignation', 'preventiveSignatureEmpId', 'preventiveDateTime',
            'rcaImage'
        ]
        
        # Make request.data mutable if it has _mutable attribute
        if hasattr(request.data, '_mutable'):
            request.data._mutable = True
            
        # Check if the user is the assigned in-charge for any of this incident's classification items
        is_assigned = False
        import json
        incident = IncidentReport.objects.filter(incidentNo=incident_id).first()
        if incident:
            classifications = incident.classifications
            parsed_class = {}
            if classifications:
                if isinstance(classifications, str):
                    try:
                        parsed_class = json.loads(classifications)
                    except Exception:
                        parsed_class = {}
                elif isinstance(classifications, dict):
                    parsed_class = classifications
            
            for cat_title, items in parsed_class.items():
                if not isinstance(items, list) or len(items) == 0:
                    continue
                matched_class = IncidentClassification.objects.filter(category_key=cat_title).first()
                if not matched_class:
                    matched_class = IncidentClassification.objects.filter(title=cat_title).first()
                
                if matched_class:
                    item_incharges = matched_class.item_incharges or {}
                    for item in items:
                        item_assigned = item_incharges.get(item) or {}
                        if item_assigned.get('incharge_id'):
                            if str(item_assigned.get('incharge_id')) == str(user_identifier):
                                is_assigned = True
                                break
                        else:
                            if matched_class.incharge_id and str(matched_class.incharge_id) == str(user_identifier):
                                is_assigned = True
                                break
                    if is_assigned:
                        break

        if user_role == 'Admin':
            # Admins can edit Quality fields always, but can edit RCA fields only if assigned
            if not is_assigned:
                for field in incharge_fields:
                    if field in request.data:
                        request.data.pop(field)
            if not existing:
                request.data.setdefault('qualityClassification', 'No harm')
        elif user_role == 'In-Charge':
            # In-Charge cannot modify Quality Department fields
            for field in quality_fields:
                if field in request.data:
                    request.data.pop(field)
            # In-Charge can edit RCA fields only if assigned
            if not is_assigned:
                for field in incharge_fields:
                    if field in request.data:
                        request.data.pop(field)
            if not existing:
                request.data['qualityClassification'] = 'No harm'
        else:
            # Other roles cannot modify Quality fields or RCA fields
            for field in quality_fields:
                if field in request.data:
                    request.data.pop(field)
            for field in incharge_fields:
                if field in request.data:
                    request.data.pop(field)
            if not existing:
                request.data['qualityClassification'] = 'No harm'

        if existing:
            serializer = SupervisorInvestigationSerializer(existing, data=request.data, partial=True)
        else:
            serializer = SupervisorInvestigationSerializer(data=request.data)
            
        if serializer.is_valid():
            user_identifier = request.data.get("auth-user-id")
            
            profile_data = get_user_profile_role_and_details(user_identifier)
            u_name = profile_data['name']
            u_dept = profile_data['department'] or ''

            extra_kwargs = {}
            if user_role == 'Admin':
                extra_kwargs['qualityReceivedSignatureEmpId'] = request.data.get('qualityReceivedSignatureEmpId') or user_identifier
            
            if not existing:
                from datetime import datetime
                current_year = datetime.now().year
                prefix = f"INV-{current_year}-"
                last_inv = SupervisorInvestigation.objects.filter(id__startswith=prefix).order_by('-id').first()
                if last_inv and last_inv.id:
                    try:
                        last_num = int(last_inv.id.split('-')[-1])
                        next_num = last_num + 1
                    except (ValueError, IndexError):
                        next_num = 1
                else:
                    next_num = 1
                new_id = f"{prefix}{next_num:04d}"
                extra_kwargs['id'] = new_id

            serializer.save(
                created_by=user_identifier,
                lastmodified_by=user_identifier,
                investigationName=request.data.get('investigationName') or u_name,
                investigationSignatureEmpId=request.data.get('investigationSignatureEmpId') or user_identifier,
                investigationDeptDesignation=request.data.get('investigationDeptDesignation') or u_dept,
                correctiveName=request.data.get('correctiveName') or u_name,
                correctiveSignatureEmpId=request.data.get('correctiveSignatureEmpId') or user_identifier,
                correctiveDeptDesignation=request.data.get('correctiveDeptDesignation') or u_dept,
                preventiveName=request.data.get('preventiveName') or u_name,
                preventiveSignatureEmpId=request.data.get('preventiveSignatureEmpId') or user_identifier,
                preventiveDeptDesignation=request.data.get('preventiveDeptDesignation') or u_dept,
                **extra_kwargs
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        start_date = request.GET.get('startDate')
        end_date = request.GET.get('endDate')
        
        matching_incidents = IncidentReport.objects.all()
        if not start_date and not end_date:
            from datetime import datetime, timedelta
            thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            matching_incidents = matching_incidents.filter(incidentDate__gte=thirty_days_ago)
        else:
            if start_date:
                matching_incidents = matching_incidents.filter(incidentDate__gte=start_date)
            if end_date:
                matching_incidents = matching_incidents.filter(incidentDate__lte=end_date)
                
        incident_ids = list(matching_incidents.values_list('incidentNo', flat=True))
        
        investigations = SupervisorInvestigation.objects.filter(incidentId__in=incident_ids)
        serializer = SupervisorInvestigationSerializer(investigations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET', 'DELETE'])
@csrf_exempt
@permission_classes([HasRolePermission])
def IncidentClassificationView(request):
    from .models import IncidentClassification
    from .forms import IncidentClassificationSerializer
    
    DEFAULT_CLASSIFICATIONS = [
        {
            "category_key": "clinical",
            "title": "Clinical Practice / Procedure",
            "items": [
                "Incomplete Documentation",
                "Missing Documentation",
                "Wrong Documentation",
                "Missing files",
                "Medical Records Unavailable",
                "Confidentiality",
                "Procedures not followed"
            ]
        },
        {
            "category_key": "safety",
            "title": "Safety / Security",
            "items": [
                "Infant Abduction",
                "Electric Shock",
                "Theft",
                "Structural Damage",
                "Chemical Spillage",
                "Mercury Spillage",
                "Blood Body Fluid Spillage",
                "Violent Behavior",
                "Fire/Smoke Incident",
                "Property Missing",
                "Unauthorized entry",
                "Patient Missing",
                "Physical Assault",
                "Protocol not followed"
            ]
        },
        {
            "category_key": "patient",
            "title": "Patient Related",
            "items": [
                "Dissatisfaction",
                "Thrombophlebitis",
                "Bed sore",
                "Hematoma",
                "Fall",
                "Diarrhoeal Dermatitis",
                "Skin Peeling",
                "Identification error"
            ]
        },
        {
            "category_key": "equipment",
            "title": "Equipment / Supplies",
            "items": [
                "Improper Handling",
                "Not available",
                "Missing/Damaged",
                "Failure/Malfunction",
                "Wrong Equipment/Supply",
                "Improper Storage"
            ]
        },
        {
            "category_key": "staff",
            "title": "Staff / Employee",
            "items": [
                "Infection control related",
                "Blood / Body fluid exposure",
                "Needle Stick/Prick",
                "Vehicular Accidents",
                "Fall",
                "Improper waste disposal"
            ]
        },
        {
            "category_key": "investigation",
            "title": "Investigation",
            "items": [
                "Wrong Report",
                "Wrong Sample",
                "Missing Sample",
                "Inadequate preservative",
                "Sample Interchanged",
                "Report Interchanged",
                "Wrong Label",
                "Incomplete Request Form"
            ]
        },
        {
            "category_key": "diet",
            "title": "Diet Related",
            "items": [
                "Wrong Diet Indent",
                "Wrong Diet",
                "Missed Diet",
                "Food Hygiene",
                "Delayed Diet"
            ]
        },
        {
            "category_key": "medication",
            "title": "Medication Related",
            "items": [
                "Administration Error",
                "Prescription Error",
                "Dispensing Error",
                "Transcription Error",
                "Verbal order policy not followed",
                "Narcotic Policy not followed",
                "Inappropriate Crash Cart Management",
                "Expiry Policy not followed"
            ]
        }
    ]

    if request.method == 'POST':
        class_id = request.data.get('id')
        
        # Handle per-item incharge allocation separately (direct field update)
        item_incharges = request.data.get('item_incharges')
        
        if class_id:
            try:
                instance = IncidentClassification.objects.get(id=str(class_id))
                
                # If only updating item_incharges (and optionally incharge_id/name), do direct field update
                if item_incharges is not None:
                    if isinstance(item_incharges, str):
                        import json
                        try:
                            item_incharges = json.loads(item_incharges)
                        except Exception:
                            item_incharges = {}
                    instance.item_incharges = item_incharges
                    # Also update top-level incharge if provided
                    incharge_id = request.data.get('incharge_id')
                    incharge_name = request.data.get('incharge_name')
                    if incharge_id is not None:
                        instance.incharge_id = incharge_id
                    if incharge_name is not None:
                        instance.incharge_name = incharge_name
                    instance.lastmodified_by = request.data.get("auth-user-id")
                    instance.save()
                    serializer = IncidentClassificationSerializer(instance)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                serializer = IncidentClassificationSerializer(instance, data=request.data, partial=True)
            except IncidentClassification.DoesNotExist:
                return Response({'error': 'Classification not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Generate next classification ID (e.g. CLF001)
            import re
            max_id = 0
            for cls_obj in IncidentClassification.objects.all():
                match = re.match(r'CLF(\d+)', str(cls_obj.id))
                if match:
                    val = int(match.group(1))
                    if val > max_id:
                        max_id = val
            next_id = f"CLF{max_id + 1:03d}"
            serializer = IncidentClassificationSerializer(data=request.data)
            
        if serializer.is_valid():
            user_identifier = request.data.get("auth-user-id")
            if not class_id:
                serializer.save(
                    id=next_id,
                    created_by=user_identifier,
                    lastmodified_by=user_identifier
                )
            else:
                serializer.save(
                    created_by=user_identifier,
                    lastmodified_by=user_identifier
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        classifications = IncidentClassification.objects.all()
        if not classifications.exists():
            for i, default_class in enumerate(DEFAULT_CLASSIFICATIONS, 1):
                IncidentClassification.objects.create(
                    id=f"CLF{i:03d}",
                    category_key=default_class["category_key"],
                    title=default_class["title"],
                    items=default_class["items"]
                )
            classifications = IncidentClassification.objects.all()
            
        serializer = IncidentClassificationSerializer(classifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        class_id = request.GET.get('id') or request.data.get('id')
        if not class_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = IncidentClassification.objects.get(id=str(class_id))
            instance.delete()
            return Response({'message': 'Classification deleted successfully'}, status=status.HTTP_200_OK)
        except IncidentClassification.DoesNotExist:
            return Response({'error': 'Classification not found'}, status=status.HTTP_404_NOT_FOUND)


from django.db.models import Q
@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_incharges(request):
    from django.conf import settings
    import pymongo
    
    try:
        db_config = settings.DATABASES['default']
        host = db_config.get('CLIENT', {}).get('host', 'mongodb://localhost:27017/')
        client = pymongo.MongoClient(host)
        db = client['Global']
        
        query = {
            '$or': [
                {'primaryRole': {'$regex': 'SI-R-INDIN|In-Charge|Incharge|IND|Admin|SI-R-IND', '$options': 'i'}},
                {'additionalRoles': {'$regex': 'SI-R-INDIN|In-Charge|Incharge|IND|Admin|SI-R-IND', '$options': 'i'}}
            ]
        }
        profiles = db['backend_diagnostics_profile'].find(query)
        data = []
        for p in profiles:
            data.append({
                'id': p.get('employeeId'),
                'name': p.get('employeeName') or '',
                'department': p.get('department') or ''
            })
        if data:
            return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"Error querying in-charges from Global DB: {e}")
        
    # Fallback to local Register model
    from .models import Register
    incharges = Register.objects.filter(
        Q(role__icontains="In-Charge") | Q(role__icontains="Incharge") | Q(role__icontains="Admin")
    )
    data = [{'id': u.id, 'name': u.name, 'department': u.department} for u in incharges]
    return Response(data, status=status.HTTP_200_OK)
