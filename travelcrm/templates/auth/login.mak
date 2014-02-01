<%inherit file="travelcrm:templates/auth/_layout.mak"/>
<div class="easyui-dialog dl30" title="${_(u'Autorization')}"
    data-options="
    	closable:false,
    	minimizable:false,
    	maximizable:false,
    	collapsible:false,
    	draggable:true,
    	resizable:false,
    	iconCls:'fa fa-user'
    ">
    ${h.tags.form(auth_url, class_="_ajax", autocomplete="off")}
        <div class="form-field">
            <div class="dl10">
            	${h.tags.title(_(u"username"), False, "username")}
            </div>
            <div class="ml10 tr">
            	${h.tags.text("username", None, class_="text w15")}
            </div>
        </div>
        <div class="form-field">
            <div class="dl10">
            	${h.tags.title(_(u"password"), False, "password")}
            </div>
            <div class="ml10 tr">
                ${h.tags.password("password", None, class_="text w15")}
            </div>
        </div>
        <div class="form-field">
        	${h.tags.link_to(_(u"Forgot password?"), forgot_url)}
        </div>
        <div class="form-buttons">
            <div class="dl20 status-bar">
                <i class="fa fa-info-circle fa-lg"></i> ${_(u"Please, enter username and password")}
            </div>
            <div class="ml20 tr">
            	${h.tags.submit('login', _(u"Login"), class_="button")}
            </div>
        </div>
    ${h.tags.end_form()}
</div>