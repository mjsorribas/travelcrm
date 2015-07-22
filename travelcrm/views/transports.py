# -*-coding: utf-8-*-

import logging

from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound

from ..models import DBSession
from ..models.transport import Transport
from ..lib.utils.common_utils import translate as _

from ..forms.transports import (
    TransportForm, 
    TransportSearchForm
)


log = logging.getLogger(__name__)


@view_defaults(
    context='..resources.transports.TransportsResource',
)
class TransportsView(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(
        request_method='GET',
        renderer='travelcrm:templates/transports/index.mako',
        permission='view'
    )
    def index(self):
        return {}

    @view_config(
        name='list',
        xhr='True',
        request_method='POST',
        renderer='json',
        permission='view'
    )
    def list(self):
        form = TransportSearchForm(self.request, self.context)
        form.validate()
        qb = form.submit()
        return {
            'total': qb.get_count(),
            'rows': qb.get_serialized()
        }

    @view_config(
        name='view',
        request_method='GET',
        renderer='travelcrm:templates/transports/form.mako',
        permission='view'
    )
    def view(self):
        if self.request.params.get('rid'):
            resource_id = self.request.params.get('rid')
            transport = Transport.by_resource_id(resource_id)
            return HTTPFound(
                location=self.request.resource_url(
                    self.context, 'view', query={'id': transport.id}
                )
            )
        result = self.edit()
        result.update({
            'title': _(u"View Transport"),
            'readonly': True,
        })
        return result

    @view_config(
        name='add',
        request_method='GET',
        renderer='travelcrm:templates/transports/form.mako',
        permission='add'
    )
    def add(self):
        return {'title': _(u'Add Transport')}

    @view_config(
        name='add',
        request_method='POST',
        renderer='json',
        permission='add'
    )
    def _add(self):
        form = TransportForm(self.request)
        if form.validate():
            transport = form.submit()
            DBSession.add(transport)
            DBSession.flush()
            return {
                'success_message': _(u'Saved'),
                'response': transport.id
            }
        else:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': form.errors
            }

    @view_config(
        name='edit',
        request_method='GET',
        renderer='travelcrm:templates/transports/form.mako',
        permission='edit'
    )
    def edit(self):
        transport = Transport.get(self.request.params.get('id'))
        return {'item': transport, 'title': _(u'Edit Transport')}

    @view_config(
        name='edit',
        request_method='POST',
        renderer='json',
        permission='edit'
    )
    def _edit(self):
        transport = Transport.get(self.request.params.get('id'))
        form = TransportForm(self.request)
        if form.validate():
            form.submit(transport)
            return {
                'success_message': _(u'Saved'),
                'response': transport.id
            }
        else:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': form.errors
            }

    @view_config(
        name='delete',
        request_method='GET',
        renderer='travelcrm:templates/transports/delete.mako',
        permission='delete'
    )
    def delete(self):
        return {
            'title': _(u'Delete Transports'),
            'rid': self.request.params.get('rid')
        }

    @view_config(
        name='delete',
        request_method='POST',
        renderer='json',
        permission='delete'
    )
    def _delete(self):
        errors = False
        ids = self.request.params.getall('id')
        if ids:
            try:
                (
                    DBSession.query(Transport)
                    .filter(Transport.id.in_(ids))
                    .delete()
                )
            except:
                errors=True
                DBSession.rollback()
        if errors:
            return {
                'error_message': _(
                    u'Some objects could not be delete'
                ),
            }
        return {'success_message': _(u'Deleted')}