import factory

from shop.models import Category, Product, Order


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Faker('word')


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product

    name = factory.Faker('word')
    cost = 10


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Order

