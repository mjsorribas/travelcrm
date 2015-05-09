# -*coding: utf-8-*-

from collections import Iterable

from sqlalchemy import literal

from . import ResourcesQueryBuilder

from ...models.resource import Resource
from ...models.order_item import OrderItem
from ...models.calculation import Calculation
from ...models.service import Service
from ...models.currency import Currency
from ...models.supplier import Supplier

from ...lib.utils.common_utils import get_base_currency


class CalculationQueryBuilder(ResourcesQueryBuilder):

    def __init__(self, context):
        super(CalculationQueryBuilder, self).__init__(context)
        self._fields = {
            'id': Calculation.id,
            '_id': Calculation.id,
            'service': Service.name,
            'supplier': Supplier.name,
            'price': Calculation.price,
            'currency': Currency.iso_code,
            'base_price': Calculation.base_price,
            'base_currency': literal(get_base_currency())
        }
        self.build_query()

    def build_query(self):
        self.build_base_query()
        self.query = (
            self.query
            .join(Calculation, Resource.calculation)
            .join(OrderItem, Calculation.order_item)
            .join(Service, OrderItem.service)
            .join(Supplier, OrderItem.supplier)
            .join(Currency, Calculation.currency)
        )
        super(CalculationQueryBuilder, self).build_query()

    def filter_id(self, id):
        assert isinstance(id, Iterable), u"Must be iterable object"
        if id:
            self.query = self.query.filter(Calculation.id.in_(id))
