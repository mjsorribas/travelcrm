<div class="dl50 easyui-dialog"
    title="${title}"
    data-options="
        modal:true,
        draggable:false,
        resizable:false,
        iconCls:'fa fa-pencil-square-o'
    ">
    ${h.tags.form(
        action or request.url, 
        class_="_ajax %s" % ('readonly' if readonly else ''), 
        autocomplete="off",
        hidden_fields=[
            ('csrf_token', request.session.get_csrf_token()),
        ]
    )}
        <div class="form-field mt05">
            <div class="dl15">
                ${h.tags.title(_(u"service"), True, "service_id")}
            </div>
            <div class="ml15">
                ${h.fields.services_combogrid_field(
                    request,
                    'service_id',
                    item.service_id if item else None,
                    show_toolbar=(not readonly if readonly else True)
                )}
                ${h.common.error_container(name='service_id')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"supplier"), True, "supplier_id")}
            </div>
            <div class="ml15">
                ${h.fields.suppliers_combogrid_field(
                    request,
                    'supplier_id',
                    item.supplier_id if item else None,
                    show_toolbar=(not readonly if readonly else True)
                )}
                ${h.common.error_container(name='supplier_id')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"price"), True, "price")}
            </div>
            <div class="ml15">
                ${h.tags.text('price', 
                    item.price if item else None, 
                    class_="easyui-textbox w20 easyui-numberbox", 
                    data_options="min:0,precision:2"
                )}
                ${h.common.error_container(name='price')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"price currency"), True, "currency_id")}
            </div>
            <div class="ml15">
                ${h.fields.currencies_combogrid_field(
                    request,
                    'currency_id',
                    item.currency_id if item else None,
                    show_toolbar=(not readonly if readonly else True)
                )}
                ${h.common.error_container(name='currency_id')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"status"), True, "status")}
            </div>
            <div class="ml15">
                ${h.fields.leads_offers_statuses_combobox_field(
                    'status',
                    item.status.key if item else None
                )}
            </div>
        </div>
        <div class="form-field mb05">
            <div class="dl15">
                ${h.tags.title(_(u"description"), True, "descr")}
            </div>
            <div class="ml15">
                ${h.tags.text('descr', item.descr if item else None, class_="easyui-textbox w20", data_options="multiline:true,height:80")}
                ${h.common.error_container(name='descr')}
            </div>
        </div>
        <div class="form-buttons">
            <div class="dl20 status-bar"></div>
            <div class="ml20 tr button-group">
                ${h.tags.submit('save', _(u"Save"), class_="button easyui-linkbutton")}
                ${h.common.reset('cancel', _(u"Cancel"), class_="button danger easyui-linkbutton")}
            </div>
        </div>
    ${h.tags.end_form()}
</div>
