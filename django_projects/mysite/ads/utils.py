from django.db.models import Q


def generate_search_query(search_value: str):
    query = Q(title__icontains=search_value)
    query.add(Q(text__icontains=search_value), Q.OR)
    query.add(Q(tags__name__in=[search_value]), Q.OR)

    return query
