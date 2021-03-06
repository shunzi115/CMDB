#!/usr/bin/env python
#coding:utf-8
from django import forms
from cmdb_auth.models import user_auth_cmdb,auth_group


class cmdb_form(forms.ModelForm):
    enable = forms.TypedChoiceField(
                    coerce=lambda x: x == 'True',
                    choices=((True,'启用'),(False,'禁用')),
                    required=True,initial=True,
                    widget=forms.RadioSelect,
                    label=u'是否启用'
    )
    class Meta:
        model = auth_group
        fields = ["group_name","group_user","enable"]

class auth_add(forms.ModelForm):
    class Meta:
        model = user_auth_cmdb
        fields = ["select_host", "add_host", "bat_add_host", "edit_host", "update_host", "delete_host",  "add_user",
                  "edit_user", "edit_pass", "delete_user", "add_department", "group_name", "add_idc", "edit_idc",
                  "del_idc", "setup_system", "upload_system", "salt_keys", "auth_log", "project_auth", "add_project",
                  "edit_project", "delete_project", "add_line_auth", "select_idc", "auth_project", "auth_highstate",
                  "cmdb_log", "server_audit"
                  ]


class auth_add_user(forms.ModelForm):
    class Meta:
        model = auth_group
        fields = ["group_user"]