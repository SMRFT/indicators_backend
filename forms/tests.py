from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock
import json
from rest_framework import status

from .models import FirstFloor, Lab, RecoveryWard, IncidentReport
from .forms import FirstFloorSerializer, IncidentReportSerializer
from .views import handle_ward_data_submission, IncidentReportView, get_next_incident_no
from .formula_aggregations import get_aggregated_formula_data, sum_field

class WardSubmissionTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('forms.views.FirstFloor.objects.filter')
    def test_handle_ward_data_submission_already_exists(self, mock_filter):
        mock_filter.return_value.exists.return_value = True
        
        request = self.factory.post('/FirstFloor/', data=json.dumps({
            'selectedDate': '2026-07-16',
            'auth-user-id': 'test-user'
        }), content_type='application/json')
        
        request.data = {
            'selectedDate': '2026-07-16',
            'auth-user-id': 'test-user'
        }
        
        response = handle_ward_data_submission(request, FirstFloor, FirstFloorSerializer)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Data already exists for this date.'})

    @patch('forms.views.FirstFloor.objects.filter')
    @patch('forms.forms.FirstFloorSerializer')
    def test_handle_ward_data_submission_success(self, mock_serializer_class, mock_filter):
        mock_filter.return_value.exists.return_value = False
        
        mock_serializer = MagicMock()
        mock_serializer.is_valid.return_value = True
        
        mock_instance = MagicMock()
        mock_instance.created_by = None
        mock_serializer.save.return_value = mock_instance
        
        mock_serializer_class.return_value = mock_serializer
        
        request = self.factory.post('/FirstFloor/', data=json.dumps({
            'selectedDate': '2026-07-16',
            'auth-user-id': 'test-user'
        }), content_type='application/json')
        request.data = {
            'selectedDate': '2026-07-16',
            'auth-user-id': 'test-user'
        }
        
        response = handle_ward_data_submission(request, FirstFloor, mock_serializer_class)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(mock_instance.created_by, 'test-user')
        self.assertEqual(mock_instance.lastmodified_by, 'test-user')

class FormulaAggregationTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_sum_field_helper(self):
        # Create temporary records in the test database
        FirstFloor.objects.create(
            selectedDate='2026-07-16',
            totalNumberOfAdmissions='25'
        )
        FirstFloor.objects.create(
            selectedDate='2026-07-17',
            totalNumberOfAdmissions='30'
        )
        # Verify the sum matches
        val = sum_field(FirstFloor, 2026, 7, 'totalNumberOfAdmissions')
        self.assertEqual(val, 55.0)

    @patch('pyauth.auth.HasRolePermission.has_permission')
    def test_get_aggregated_formula_data_missing_params(self, mock_has_perm):
        mock_has_perm.return_value = True
        request = self.factory.get('/formula-aggregated-data/')
        request.GET = {}
        response = get_aggregated_formula_data(request)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing year or month', response.content)

class IncidentManagementTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('forms.views.IncidentReport.objects.filter')
    def test_get_next_incident_no_empty(self, mock_filter):
        mock_filter.return_value.order_by.return_value.first.return_value = None
        
        request = self.factory.get('/get-next-incident-no/')
        response = get_next_incident_no(request)
        
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertTrue(data['nextIncidentNo'].startswith('INC-'))

    @patch('forms.views.IncidentReport.objects.filter')
    def test_get_next_incident_no_existing(self, mock_filter):
        from datetime import datetime
        current_year = datetime.now().year
        mock_incident = MagicMock()
        mock_incident.incidentNo = f"INC-{current_year}-0005"
        mock_filter.return_value.order_by.return_value.first.return_value = mock_incident
        
        request = self.factory.get('/get-next-incident-no/')
        response = get_next_incident_no(request)
        
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['nextIncidentNo'], f"INC-{current_year}-0006")

    @patch('forms.views.IncidentReport.objects.all')
    @patch('pyauth.auth.HasRolePermission.has_permission')
    def test_get_incidents_list(self, mock_has_perm, mock_all):
        mock_has_perm.return_value = True
        
        mock_incidents = [
            MagicMock(incidentDate='2026-07-16', incidentNo='INC-2026-0001'),
            MagicMock(incidentDate='2026-07-17', incidentNo='INC-2026-0002')
        ]
        mock_qs = MagicMock()
        mock_qs.filter.return_value = mock_qs
        mock_qs.order_by.return_value = mock_incidents
        mock_all.return_value = mock_qs

        request = self.factory.get('/IncidentReport/', {'startDate': '2026-07-15'})
        response = IncidentReportView(request)
        self.assertEqual(response.status_code, 200)
