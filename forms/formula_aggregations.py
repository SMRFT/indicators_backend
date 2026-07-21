# formula_aggregations.py
# Backend aggregation service for SMRFT quality KPI formulas

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from pyauth.auth import HasRolePermission
from .models import (
    FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit, Lab, CT, MRI, Xray,
    OPD, OT, Physiotherapy, Dialysis, EmergencyRoom, ChemoWard, RecoveryWard,
    SICU, MICU, NICU, Pharmacy, MockDrill, HandHygenieAudit, MRD
)

def sum_field(model_class, year, month, *field_names):
    """Sums one or more fields in a model for the given year and month prefix."""
    month_str = f"{int(month):02}"
    prefix = f"{year}-{month_str}"
    
    # We query only the requested fields to minimize database overhead
    query_fields = list(field_names)
    queryset = model_class.objects.filter(selectedDate__startswith=prefix).values_list(*query_fields)
    
    total = 0.0
    for row in queryset:
        for val in row:
            if val:
                try:
                    total += float(val)
                except ValueError:
                    pass
    return total

@api_view(['GET'])
@permission_classes([HasRolePermission])
def get_aggregated_formula_data(request):
    year = request.GET.get('year')
    month = request.GET.get('month')

    if not year or not month:
        return JsonResponse({'error': 'Missing year or month'}, status=400)

    try:
        year = int(year)
        month = int(month)
    except ValueError:
        return JsonResponse({'error': 'Invalid year or month format'}, status=400)

    # 1. Gather all individual metric totals using optimized database queries
    ward_models = [FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit, SICU, MICU, NICU, ChemoWard, RecoveryWard]
    
    # Sum of Initial Assessment times
    totalSumOfTime = 0.0
    for m in ward_models:
        # Check casing of the field (RecoveryWard uses sumofTimeTakenforInitialAssessment)
        field_name = 'sumofTimeTakenforInitialAssessment' if m == RecoveryWard else 'sumOfTimeTakenforInitialAssessment'
        totalSumOfTime += sum_field(m, year, month, field_name)

    # Total Admissions
    totalAdmissions = sum(sum_field(m, year, month, 'totalNumberOfAdmissions') for m in ward_models)

    # Initial Assessment record count details
    zeroRecords = 0
    validRecords = 0
    for m in ward_models:
        field_name = 'sumofTimeTakenforInitialAssessment' if m == RecoveryWard else 'sumOfTimeTakenforInitialAssessment'
        month_str = f"{int(month):02}"
        prefix = f"{year}-{month_str}"
        queryset = m.objects.filter(selectedDate__startswith=prefix).values_list(field_name, 'totalNumberOfAdmissions')
        for time_val, adm_val in queryset:
            try:
                time_f = float(time_val) if time_val else 0.0
                adm_f = float(adm_val) if adm_val else 0.0
                if time_f == 0 or adm_f == 0:
                    zeroRecords += 1
                else:
                    validRecords += 1
            except ValueError:
                pass

    # Lab quality indicators
    totalReportingErrors = sum_field(Lab, year, month, 'numberOfReportingErrors')
    totalTestsPerformed = sum_field(Lab, year, month, 'numberOfTestsPerformed')
    totalStaffAdhering = sum_field(Lab, year, month, 'numberOfStaffAdheringToSafety')
    totalStaffAudited = sum_field(Lab, year, month, 'numberOfStaffAudited')

    # Medication errors
    medication_models = [FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit, SICU, MICU, NICU, ChemoWard, RecoveryWard]
    totalMedicationErrors = sum(sum_field(m, year, month, 'totalNumberOfMedicationErrors') for m in medication_models)
    totalOpportunityMedicationErrors = sum(sum_field(m, year, month, 'totalNumberOfOpportunitiesOfMedicationErrors') for m in medication_models)

    # Adverse drug reactions
    totalAdverseDrug = sum(sum_field(m, year, month, 'numberOfPatientsDevelopingAdverseDrugReactions') for m in medication_models)
    totalInpatients = sum(sum_field(m, year, month, 'numberOfInPatients') for m in [RecoveryWard]) # matches Formula.js filter logic

    # Operating Theatre metrics
    totalUplannedOT = sum_field(OT, year, month, 'numberOfUnplannedReturnToOTOrReexploration')
    totalUnderwentSurgery = sum_field(OT, year, month, 'numberOfPatientsWhoUnderwentSurgeriesInTheOT')
    totalSurgeryProcedureFollowed = sum_field(OT, year, month, 'numberOfSurgeriesWhereProceduresWereFollowed')
    totalProphylacticAntibiotics = sum_field(OT, year, month, 'numberOfPatientsWhoDidReceiveAppropriateProphylacticAntibiotic')
    totalSurgeriesRescheduled = sum_field(OT, year, month, 'numberOfCasesReScheduledOrCanceled')
    totalSurgeriesPlanned = sum_field(OT, year, month, 'numberOfSurgeriesPlannedInTheOt')

    # Transfusion metrics
    transfusion_models = [FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit, SICU, MICU, NICU, RecoveryWard, ChemoWard]
    totalUnitsTransfused = sum(sum_field(m, year, month, 'numberOfUnitsTransfused') for m in transfusion_models)
    
    # OT uses plural field, others use singular
    totalTransusionReaction = sum_field(OT, year, month, 'numberOfTransfusionReactions') + sum(
        sum_field(m, year, month, 'numberOfTransfusionReaction') for m in transfusion_models
    )

    # ICU Mortality
    totalActualDeath = sum(sum_field(m, year, month, 'actualDeathsInICU') for m in [MICU, NICU, SICU])
    totalPredictedDeath = sum(sum_field(m, year, month, 'predictedDeathsInICU') for m in [MICU, NICU, SICU])

    # Emergency Room metrics
    totalreturnsToEmergency = sum_field(EmergencyRoom, year, month, 'numberOfReturnsToEmergencyWithin72hoursWithSimilarPresentingComplaints')
    totalpatientsToEmergency = sum_field(EmergencyRoom, year, month, 'numberOfPatientsWhoHaveComeToTheEmergency')

    # Patient Safety metrics (Falls & Pressure Ulcers)
    safety_models = [FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit, SICU, MICU, NICU, ChemoWard, RecoveryWard]
    totalPatientFalls = sum(sum_field(m, year, month, 'numberOfPatientFalls') for m in safety_models)
    totalPressureUlcer = sum(sum_field(m, year, month, 'numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer') for m in safety_models)

    # Catheter & Central Line indicators
    infection_models = [FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit, SICU, MICU, NICU, ChemoWard]
    totalCatheterInMonth = sum(sum_field(m, year, month, 'numberOfUrinaryCatheterAssociatedUtisInThatMonth') for m in infection_models)
    totalCatheterDaysInMonth = sum(sum_field(m, year, month, 'numberOfUrinaryCatheterDaysInThatMonth') for m in infection_models)
    totalCentrallineBloodStreamInfectionInMonth = sum(sum_field(m, year, month, 'numberCentralLineAssociatedBloodStreamInfectionsInAMonth') for m in infection_models)
    totalCentrallineDaysInMonth = sum(sum_field(m, year, month, 'numberOfCentralLineDaysInThatMonth') for m in infection_models)
    totalSurgicalsiteInfectionInAMonth = sum(sum_field(m, year, month, 'numberOfSurgicalSiteInfectionsInAGivenMonth') for m in infection_models)

    # ICU Ventilator metrics
    totalVentilatorPneumonia = sum(sum_field(m, year, month, 'numberOfVentilatorAssociatedPneumonia') for m in [MICU, NICU, SICU])
    totalVentilatorDaysInMonth = sum(sum_field(m, year, month, 'numberOfVentilatorDays') for m in [MICU, NICU, SICU])

    # Blood components time
    totalBBCCrossMatched = sum(sum_field(m, year, month, 'numberOfBedsOccupied') for m in [FirstFloor, SecondFloor, ThirdFloor, FirstSuit, SecondSuit])
    totalSumOfTimeBBC = sum(sum_field(m, year, month, 'sumOfTimeTakenForBloodAndBloodComponents') for m in transfusion_models)

    # Beds & Nurse ratios
    totalBedsOccupied = sum(sum_field(m, year, month, 'numberOfBedsOccupied') for m in safety_models)
    totalNursingStaff = sum(sum_field(m, year, month, 'numberOfNursingStaff') for m in safety_models)

    # Outpatients metrics
    totalOPConsultationTime = sum_field(OPD, year, month, 'sumOfTimeTakenForConsultation')
    totalOP = sum_field(OPD, year, month, 'totalNumberOfOutPatients')

    # Diagnostics waiting time
    totalDiagnosticsWaitingTime = sum_field(Lab, year, month, 'waitingTimeForDiagnostics')
    totalDiagnosticsPatients = sum_field(Lab, year, month, 'numberOfPatientsReportedInDiagnostics')

    # Discharges
    totalDischargeTime = sum(sum_field(m, year, month, 'sumOfTimeTakenForDischargeInsurance', 'sumOfTimeTakenForDischargePay') for m in safety_models)
    totalDischargePatients = sum(sum_field(m, year, month, 'numberOfPatientsDischargedInsurance', 'numberOfPatientsDischargedPay') for m in safety_models)

    # Incident reporting
    totalNearMissReported = sum(sum_field(m, year, month, 'numberOfNearMissReported') for m in safety_models)
    totalIncidentsReported = sum(sum_field(m, year, month, 'numberOfIncidentsReported') for m in safety_models)
    totalParenteralExposures = sum(sum_field(m, year, month, 'numberOfParenteralExposures') for m in safety_models)

    # Handover compliance
    totalHandoverDone = sum(sum_field(m, year, month, 'totalNumberOfHandoversDoneAppropriately') for m in safety_models)
    totalHandoverOpportunity = sum(sum_field(m, year, month, 'totalNumberOfHandoverOpportunities') for m in safety_models)

    # Pharmacy & Stock indicators
    totalStockOutEmergencyDrugs = sum_field(Pharmacy, year, month, 'numberOfStockOutEmergencyDrugs')
    totalPrescriptionInCapitalLetters = sum_field(Pharmacy, year, month, 'totalNumberOfPrescriptionInCapitalLetters')
    totalNumberOfPrescriptions = sum_field(Pharmacy, year, month, 'totalNumberOfPrescriptions')

    # Mock drills & hand hygiene audit
    totalNumberOfVariationsObservedInMockDrill = sum_field(MockDrill, year, month, 'totalNumberOfVariationsObservedInMockDrill')
    totalNumberOfActionsPerformed = sum_field(HandHygenieAudit, year, month, 'totalNumberOfActionsPerformed')
    totalNumberOfHandHygieneOpportunities = sum_field(HandHygenieAudit, year, month, 'totalNumberOfHandHygieneOpportunities')

    # MRD records
    totalNumberOfMedicalRecords = sum_field(MRD, year, month, 'numberOfMedicalRecords')
    totalNumberOfDischargeAndDeath = sum_field(MRD, year, month, 'numberOfDischarge', 'numberOfDeath')

    # 2. Perform math equations for KPI rates
    averageTime = f"{(totalSumOfTime / totalAdmissions):.2f}" if totalAdmissions > 0 else "0.00"
    errorRate = f"{((totalReportingErrors / totalTestsPerformed) * 1000):.2f}" if totalTestsPerformed > 0 else "0.00"
    adherenceRate = f"{((totalStaffAdhering / totalStaffAudited) * 100):.2f}" if totalStaffAudited > 0 else "0.00"
    medicationError = f"{((totalMedicationErrors / totalOpportunityMedicationErrors) * 100):.2f}" if totalOpportunityMedicationErrors > 0 else "0.00"
    adversedrugrate = f"{((totalAdverseDrug / totalInpatients) * 100):.2f}" if totalInpatients > 0 else "0.00"
    unplannedOTRate = f"{((totalUplannedOT / totalUnderwentSurgery) * 100):.2f}" if totalUnderwentSurgery > 0 else "0.00"
    correctsurgery = f"{((totalSurgeryProcedureFollowed / totalUnderwentSurgery) * 100):.2f}" if totalUnderwentSurgery > 0 else "0.00"
    transfusionRate = f"{((totalTransusionReaction / totalUnitsTransfused) * 100):.2f}" if totalUnitsTransfused > 0 else "0.00"
    StandMortalityRate = f"{((totalActualDeath / totalPredictedDeath) * 100):.2f}" if totalPredictedDeath > 0 else "0.00"
    EmergencyPatientRate = f"{((totalreturnsToEmergency / totalpatientsToEmergency) * 100):.2f}" if totalpatientsToEmergency > 0 else "0.00"
    PressureUlcerRate = f"{((totalPressureUlcer / totalInpatients) * 100):.2f}" if totalInpatients > 0 else "0.00"
    UTIRate = f"{((totalCatheterInMonth / totalCatheterDaysInMonth) * 100):.2f}" if totalCatheterDaysInMonth > 0 else "0.00"
    PneumoniaRate = f"{((totalVentilatorPneumonia / totalVentilatorDaysInMonth) * 100):.2f}" if totalVentilatorDaysInMonth > 0 else "0.00"
    CentrallineInfectionRate = f"{((totalCentrallineBloodStreamInfectionInMonth / totalCentrallineDaysInMonth) * 100):.2f}" if totalCentrallineDaysInMonth > 0 else "0.00"
    SurgicalsiteInfectionRate = f"{((totalSurgicalsiteInfectionInAMonth / totalUnderwentSurgery) * 100):.2f}" if totalUnderwentSurgery > 0 else "0.00"
    ProphylacticRate = f"{((totalProphylacticAntibiotics / totalUnderwentSurgery) * 100):.2f}" if totalUnderwentSurgery > 0 else "0.00"
    SurgeryRescheduledRate = f"{((totalSurgeriesRescheduled / totalSurgeriesPlanned) * 100):.2f}" if totalSurgeriesPlanned > 0 else "0.00"
    BBCRate = f"{(totalSumOfTimeBBC / totalBBCCrossMatched):.2f}" if totalBBCCrossMatched > 0 else "0.00"
    NursePatientRatio = f"{(totalNursingStaff / totalBedsOccupied):.2f}" if totalBedsOccupied > 0 else "0.00"
    OPWaitingTimeRate = f"{(totalOPConsultationTime / totalOP):.2f}" if totalOP > 0 else "0.00"
    DiagnosticsWaitingTimeRate = f"{(totalDiagnosticsWaitingTime / totalDiagnosticsPatients):.2f}" if totalDiagnosticsPatients > 0 else "0.00"
    DischargeTimeRate = f"{(totalDischargeTime / totalDischargePatients):.2f}" if totalDischargePatients > 0 else "0.00"
    PatientFallRate = f"{(totalPatientFalls / totalInpatients):.2f}" if totalInpatients > 0 else "0.00"
    NearMissesRate = f"{((totalNearMissReported / totalIncidentsReported) * 100):.2f}" if totalIncidentsReported > 0 else "0.00"
    NeedleStickInjuryRate = f"{(totalParenteralExposures / totalInpatients):.2f}" if totalInpatients > 0 else "0.00"
    HandoverRate = f"{((totalHandoverDone / totalHandoverOpportunity) * 100):.2f}" if totalHandoverOpportunity > 0 else "0.00"
    MedicationPrescriptionCapitalRate = f"{((totalPrescriptionInCapitalLetters / totalNumberOfPrescriptions) * 100):.2f}" if totalNumberOfPrescriptions > 0 else "0.00"
    HandHygenieRate = f"{((totalNumberOfActionsPerformed / totalNumberOfHandHygieneOpportunities) * 100):.2f}" if totalNumberOfHandHygieneOpportunities > 0 else "0.00"
    ImproperConsentRate = f"{((totalNumberOfMedicalRecords / totalNumberOfDischargeAndDeath) * 100):.2f}" if totalNumberOfDischargeAndDeath > 0 else "0.00"

    aggregated_data = {
        'totalSumOfTime': totalSumOfTime,
        'totalAdmissions': totalAdmissions,
        'averageTime': averageTime,
        'validRecords': validRecords,
        'zeroRecords': zeroRecords,
        'totalRecords': validRecords + zeroRecords,
        'totalReportingErrors': totalReportingErrors,
        'totalTestsPerformed': totalTestsPerformed,
        'errorRate': errorRate,
        'totalStaffAdhering': totalStaffAdhering,
        'totalStaffAudited': totalStaffAudited,
        'adherenceRate': adherenceRate,
        'totalMedicationErrors': totalMedicationErrors,
        'totalOpportunityMedicationErrors': totalOpportunityMedicationErrors,
        'medicationError': medicationError,
        'totalInpatients': totalInpatients,
        'adversedrugrate': adversedrugrate,
        'totalUplannedOT': totalUplannedOT,
        'totalUnderwentSurgery': totalUnderwentSurgery,
        'unplannedOTRate': unplannedOTRate,
        'totalSurgeryProcedureFollowed': totalSurgeryProcedureFollowed,
        'correctsurgery': correctsurgery,
        'totalTransusionReaction': totalTransusionReaction,
        'totalUnitsTransfused': totalUnitsTransfused,
        'transfusionRate': transfusionRate,
        'totalActualDeath': totalActualDeath,
        'totalPredictedDeath': totalPredictedDeath,
        'StandMortalityRate': StandMortalityRate,
        'totalreturnsToEmergency': totalreturnsToEmergency,
        'totalpatientsToEmergency': totalpatientsToEmergency,
        'EmergencyPatientRate': EmergencyPatientRate,
        'totalPressureUlcer': totalPressureUlcer,
        'PressureUlcerRate': PressureUlcerRate,
        'totalCatheterInMonth': totalCatheterInMonth,
        'totalCatheterDaysInMonth': totalCatheterDaysInMonth,
        'UTIRate': UTIRate,
        'totalVentilatorPneumonia': totalVentilatorPneumonia,
        'totalVentilatorDaysInMonth': totalVentilatorDaysInMonth,
        'PneumoniaRate': PneumoniaRate,
        'totalCentrallineBloodStreamInfectionInMonth': totalCentrallineBloodStreamInfectionInMonth,
        'totalCentrallineDaysInMonth': totalCentrallineDaysInMonth,
        'CentrallineInfectionRate': CentrallineInfectionRate,
        'totalSurgicalsiteInfectionInAMonth': totalSurgicalsiteInfectionInAMonth,
        'SurgicalsiteInfectionRate': SurgicalsiteInfectionRate,
        'totalProphylacticAntibiotics': totalProphylacticAntibiotics,
        'ProphylacticRate': ProphylacticRate,
        'totalSurgeriesRescheduled': totalSurgeriesRescheduled,
        'totalSurgeriesPlanned': totalSurgeriesPlanned,
        'SurgeryRescheduledRate': SurgeryRescheduledRate,
        'totalBBCCrossMatched': totalBBCCrossMatched,
        'totalSumOfTimeBBC': totalSumOfTimeBBC,
        'BBCRate': BBCRate,
        'totalNursingStaff': totalNursingStaff,
        'totalBedsOccupied': totalBedsOccupied,
        'NursePatientRatio': NursePatientRatio,
        'totalOPConsultationTime': totalOPConsultationTime,
        'totalOP': totalOP,
        'OPWaitingTimeRate': OPWaitingTimeRate,
        'totalDiagnosticsWaitingTime': totalDiagnosticsWaitingTime,
        'totalDiagnosticsPatients': totalDiagnosticsPatients,
        'DiagnosticsWaitingTimeRate': DiagnosticsWaitingTimeRate,
        'totalDischargeTime': totalDischargeTime,
        'totalDischargePatients': totalDischargePatients,
        'DischargeTimeRate': DischargeTimeRate,
        'totalPatientFalls': totalPatientFalls,
        'PatientFallRate': PatientFallRate,
        'totalNearMissReported': totalNearMissReported,
        'totalIncidentsReported': totalIncidentsReported,
        'NearMissesRate': NearMissesRate,
        'totalParenteralExposures': totalParenteralExposures,
        'NeedleStickInjuryRate': NeedleStickInjuryRate,
        'totalHandoverDone': totalHandoverDone,
        'totalHandoverOpportunity': totalHandoverOpportunity,
        'HandoverRate': HandoverRate,
        'totalStockOutEmergencyDrugs': totalStockOutEmergencyDrugs,
        'totalNumberOfVariationsObservedInMockDrill': totalNumberOfVariationsObservedInMockDrill,
        'totalPrescriptionInCapitalLetters': totalPrescriptionInCapitalLetters,
        'totalNumberOfPrescriptions': totalNumberOfPrescriptions,
        'MedicationPrescriptionCapitalRate': MedicationPrescriptionCapitalRate,
        'totalNumberOfActionsPerformed': totalNumberOfActionsPerformed,
        'totalNumberOfHandHygieneOpportunities': totalNumberOfHandHygieneOpportunities,
        'HandHygenieRate': HandHygenieRate,
        'totalNumberOfMedicalRecords': totalNumberOfMedicalRecords,
        'totalNumberOfDischargeAndDeath': totalNumberOfDischargeAndDeath,
        'ImproperConsentRate': ImproperConsentRate
    }

    return JsonResponse(aggregated_data)
