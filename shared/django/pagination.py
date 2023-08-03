from rest_framework.pagination import PageNumberPagination


class JobVacancyPagination(PageNumberPagination):
    page_size = 15
    