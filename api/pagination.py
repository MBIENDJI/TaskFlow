from rest_framework.pagination import PageNumberPagination


class PaginationTaskFlow(PageNumberPagination):
    """
    Pagination utilisée dans toute l'application.
    """

    page_size = 10

    page_size_query_param = "page_size"

    max_page_size = 100