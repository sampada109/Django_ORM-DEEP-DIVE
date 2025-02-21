from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sales
from django.utils import timezone
from django.db import connection
from pprint import pprint
import random
from datetime import datetime, timedelta
from django.db.models import Sum, Max, Avg


# Inserting Values in Resturant 
'''
def run():
    Restaurant.objects.create(
        name = "China Town",
        date_opened = timezone.now(),
        latitude = 32.34,
        longitude = 22.17,
        restaurant_type = Restaurant.TypeChoices.CHINESE
    )
    Restaurant.objects.create(
        name = "Mr Pizza",
        date_opened = timezone.now(),
        latitude = 120.31,
        longitude = 115.17,
        restaurant_type = Restaurant.TypeChoices.ITALIAN
    )
    Restaurant.objects.create(
        name = "Taki Tako",
        date_opened = timezone.now(),
        latitude = 105.34,
        longitude = 90.19,
        restaurant_type = Restaurant.TypeChoices.MEXICAN
    )
    pprint(connection.queries)
'''


# RETRIVING
'''
def run():
    rest = Restaurant.objects.filter(longitude__gte=90)
    print(rest)
'''


# Users
'''
def run():
    users = [
        User(username="Jack Hawkins"),
        User(username="Alice Smith"),
        User(username="Bob Johnson"),
        User(username="Charlie Brown"),
    ]
    # Use bulk_create to add all users at once
    User.objects.bulk_create(users)
'''


# Ratings
'''
def run():
    def generate_random_rating(num):
        ratings = []
        for _ in range(num):
            rest_id = random.randint(1,4)
            user_id = random.randint(2,5)
            rating = random.randint(1,5)
            ratings.append((rest_id, user_id, rating))
        return ratings
    
    restaurant_ratings = generate_random_rating(6)

    for rest_id, user_id, rating in restaurant_ratings:
        rest = Restaurant.objects.get(id=rest_id)
        user = User.objects.get(id=user_id)
        Rating.objects.create(
            user = user,
            restaurant = rest,
            rating = rating
        )
'''


# Sales
'''
def run():
    def generate_random_date():
        start = datetime(2024, 5, 1, 00, 00, 00)
        end = datetime(2025, 2, 27, 00, 00, 00)
        return start + (end - start) * random.random()
    
    def generate_random_sales(num):
        sales = []
        for _ in range(num):
            rest_id = random.randint(1,4)
            income = round(random.uniform(100.00, 500.00), 2)
            date = generate_random_date()
            sales.append((rest_id, income, date.strftime('%Y-%m-%d %H:%M:%S')))
        return sales
    rest_sales = generate_random_sales(5)

    for rest_id, income, date in rest_sales:
        rest = Restaurant.objects.get(id=rest_id)
        Sales.objects.create(
            restaurant = rest,
            income = income,
            datetime = date
        )
'''


# Some Operations
'''
def run():
    # sales = Sales.objects.filter(income__gte=250)
    # for i in sales:
    #     print(i.restaurant)
    # pprint(connection.queries)

    # reverse retrival
    # rest = Restaurant.objects.all()
    # for i in rest:
    #     print(i.sales.all())
    # pprint(connection.queries)

    # aggregate sales Sum
    # total_sales = Sales.objects.aggregate(Sum('income'))
    # print(total_sales)

    # average sales
    # avg_sale = Sales.objects.aggregate(Avg('income'))
    # print(avg_sale)

    # max sales of rest
    # max_sale = Sales.objects.aggregate(Max('income'))
    # print(max_sale)

    # each restaurant total sales
    # rest_sales = Sales.objects.values('restaurant').annotate(Sum('income')).order_by('income')
    # pprint(rest_sales)
    # pprint(connection.queries)
    rest_sales = Restaurant.objects.annotate(total_sales=Sum('sales__income')).order_by('-total_sales')
    for i in rest_sales:
        formatted_sales = f"{i.total_sales:.2f}" if i.total_sales is not None else "0.00"
        pprint({i.name: formatted_sales})
    pprint(connection.queries)
'''