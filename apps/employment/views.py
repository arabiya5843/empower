from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.employment.models import JobVacancy
from apps.employment.serializers import MyJobVacancyModelSerializer, JobVacancyModelSerializer
from shared.django.pagination import JobVacancyPagination
from shared.django.permissions import IsEmployerAndIsOwnerOfVacancy
from shared.django.viewset import CreateUpdateDestroyListModelViewSet


# Create a view set for JobVacancy model
class MyJobVacancyModelViewSet(CreateUpdateDestroyListModelViewSet):
    # Define the queryset to retrieve all JobVacancy objects from the database
    queryset = JobVacancy.objects.all()

    # Use the JobVacancySerializer to serialize and deserialize JobVacancy data
    serializer_class = MyJobVacancyModelSerializer

    # Permission for creating JobVacancy
    permission_classes = (IsAuthenticated, IsEmployerAndIsOwnerOfVacancy)

    # Paginate
    pagination_class = JobVacancyPagination

    def get_queryset(self):
        request_user = self.request.user
        return JobVacancy.objects.filter(
            user=request_user) if request_user.is_authenticated else JobVacancy.objects.none()

    # Create a view set for JobVacancy model


class JobVacancyReadOnlyViewSet(ReadOnlyModelViewSet):
    # Use the JobVacancySerializer to serialize and deserialize JobVacancy data
    serializer_class = JobVacancyModelSerializer

    # Permission for creating JobVacancy
    permission_classes = (IsAuthenticated,)

    # Paginate
    pagination_class = JobVacancyPagination

    def get_queryset(self):
        return JobVacancy.objects.order_by('created_at')
