from django import template
from ..models import Storeroom
from django.db.models import Count, Q
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType

# @register.inclusion_tag("inventory/StoreroomList.html")
# def StoreroomList():
# 	return {
# 		"Storeroom": Storeroom.objects.all()
# 	}