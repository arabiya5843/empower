from rest_framework.viewsets import ModelViewSet

from apps.employment.models import JobVacancy
from apps.employment.serializers import JobVacancySerializer


# Create a view set for JobVacancy model
class JobVacancyViewSet(ModelViewSet):
    # Define the queryset to retrieve all JobVacancy objects from the database
    queryset = JobVacancy.objects.all()

    # Use the JobVacancySerializer to serialize and deserialize JobVacancy data
    serializer_class = JobVacancySerializer
