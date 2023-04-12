from django.shortcuts import render
from django.db import connection
from django.db import reset_queries

from .models import PetSitter, Pet

# Create your views here.
# 데코레이터를 사용한 code
def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        # 함수 실행 전 실행
        reset_queries() 
        # original func
        origin_func(*args, **kwargs)
        # 함수 실행 후 
        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
    
    return wrapper


# ==== main 로직 전후로 수행해야 하는 걸 더 simple하게 쓰려면 ? -> decorator
# decorator 사용하지 않는 경우
# def get_pet_data():
#     # 함수를 실행시켰을 때 어떤 식으로 SQL이 나가는지 출력하는 for문 
#     reset_queries()

#     # 내가 원하는 ORM
#     pets = Pet.objects.all()
#     for pet in pets:
#         print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')

#     # 함수를 실행시켰을 때 어떤 식으로 SQL이 나가는지 출력하는 for문 
#     query_info = connection.queries
#     for query in query_info:
#         print(query['sql'])

# 데코레이터 사용
# @get_sql_queries
# def get_pet_data():
#     pets = Pet.objects.all()
#     for pet in pets:
#         print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')


# Eager Loading
def get_pet_data():
    # pets = Pet.objects.all()
    pets = Pet.objects.all().select_related('pet_sitter')
    for pet in pets:
        print(pet.name, pet.pet_sitter.first_name)

    query_info = connection.queries
    for query in query_info:
        print(query['sql'])