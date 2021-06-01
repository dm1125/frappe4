# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Test",
			"color": "test",
			"icon": "test",
			"type": "module",
			"label": _("Test")
		}
	]
