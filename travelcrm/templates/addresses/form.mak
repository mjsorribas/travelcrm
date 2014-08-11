<div class="dl45 easyui-dialog"
    title="${title}"
    data-options="
        modal:true,
        draggable:false,
        resizable:false,
        iconCls:'fa fa-pencil-square-o'
    ">
    ${h.tags.form(request.url, class_="_ajax", autocomplete="off")}
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"location"), True, "location_id")}
            </div>
            <div class="ml15">
                ${h.fields.locations_combobox_field(request, item.location_id if item else None)}
                ${h.common.error_container(name='location_id')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"zip code"), True, "zip_code")}
            </div>
            <div class="ml15">
                ${h.tags.text("zip_code", item.zip_code if item else None, class_="easyui-textbox w10")}
                ${h.common.error_container(name='zip_code')}
            </div>
        </div>
        <div class="form-field mb05">
            <div class="dl15">
                ${h.tags.title(_(u"address"), True, "address")}
            </div>
            <div class="ml15">
                ${h.tags.text('address', item.address if item else None, class_="easyui-textbox w20", data_options="multiline:true,height:80")}
                ${h.common.error_container(name='address')}
            </div>
        </div>
        <div class="form-buttons">
            <div class="dl20 status-bar"></div>
            <div class="ml20 tr button-group">
                ${h.tags.submit('save', _(u"Save"), class_="button")}
                ${h.common.reset('cancel', _(u"Cancel"), class_="button danger")}
            </div>
        </div>
    ${h.tags.end_form()}
</div>
