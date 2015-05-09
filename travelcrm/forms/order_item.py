# -*-coding: utf-8 -*-

import colander

from . import (
    Date,
    ResourceSchema,
    BaseForm,
    BaseSearchForm,
)
from ..resources.order_item import OrderItemResource
from ..models.order_item import OrderItem
from ..models.person import Person
from ..lib.qb.order_item import OrderItemQueryBuilder


class OrderItemSchema(ResourceSchema):
    service_id = colander.SchemaNode(
        colander.Integer(),
    )
    currency_id = colander.SchemaNode(
        colander.Integer(),
    )
    supplier_id = colander.SchemaNode(
        colander.Integer(),
    )
    price = colander.SchemaNode(
        colander.Money()
    )
    person_id = colander.SchemaNode(
        colander.Set(),
    )
    status = colander.SchemaNode(
        colander.String(),
    )
    status_date = colander.SchemaNode(
        Date(),
        missing=None
    )
    status_info = colander.SchemaNode(
        colander.String(),
        missing=None,
        validator=colander.Length(max=128)
    )

    def deserialize(self, cstruct):
        if (
            'person_id' in cstruct
            and not isinstance(cstruct.get('person_id'), list)
        ):
            val = cstruct['person_id']
            cstruct['person_id'] = list()
            cstruct['person_id'].append(val)

        return super(OrderItemSchema, self).deserialize(cstruct)


class OrderItemForm(BaseForm):
    _schema = OrderItemSchema

    def submit(self, order_item=None):
        context = OrderItemResource(self.request)
        if not order_item:
            order_item = OrderItem(
                resource=context.create_resource()
            )
        else:
            order_item.persons = []

        order_item.service_id = self._controls.get('service_id')
        order_item.currency_id = self._controls.get('currency_id')
        order_item.supplier_id = self._controls.get('supplier_id')
        order_item.price = self._controls.get('price')
        order_item.status = self._controls.get('status')
        order_item.status_date = self._controls.get('status_date')
        order_item.status_info = self._controls.get('status_info')
        for id in self._controls.get('person_id'):
            person = Person.get(id)
            order_item.persons.append(person)
        return order_item


class OrderItemSearchForm(BaseSearchForm):
    _qb = OrderItemQueryBuilder
