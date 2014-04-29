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
                ${h.tags.title(_(u"bank"), True, "bank_id")}
            </div>
            <div class="ml15">
                ${h.fields.banks_combobox_field(request, item.bank_id if item else None)}
                ${h.common.error_container(name='bank_id')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"price currency"), True, "currency_id")}
            </div>
            <div class="ml15">
                ${h.fields.currencies_combobox_field(request, item.currency_id if item else None)}
                ${h.common.error_container(name='currency_id')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"beneficiary"), True, "beneficiary")}
            </div>
            <div class="ml15">
                ${h.tags.text("beneficiary", item.beneficiary if item else None, class_="text w20")}
                ${h.common.error_container(name='beneficiary')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"account"), True, "account")}
            </div>
            <div class="ml15">
                ${h.tags.text("account", item.account if item else None, class_="text w20")}
                ${h.common.error_container(name='account')}
            </div>
        </div>
        <div class="form-field mb05">
            <div class="dl15">
                ${h.tags.title(_(u"swift code"), True, "swift_code")}
            </div>
            <div class="ml15">
                ${h.tags.text("swift_code", item.swift_code if item else None, class_="text w20")}
                ${h.common.error_container(name='swift_code')}
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