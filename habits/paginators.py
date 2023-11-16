from rest_framework.pagination import PageNumberPagination


class HabitListPaginator(PageNumberPagination):
    page_size = 5