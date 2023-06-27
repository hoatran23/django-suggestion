from asyncio import format_helpers
from django.contrib import admin
from django.apps import apps
from django.urls import reverse
from .models import *
from django.utils.html import format_html

# @admin.register(Combinationdata)
# class CombinationdataAdmin(admin.ModelAdmin):
#     # list_display = [field.name for field in Combinationdata._meta.get_fields()]
#     # search_fields = [field.name for field in Combinationdata._meta.get_fields()]
#     list_display = []
#     search_fields = []
#     readonly_fields = ["createddate", "modifieddate"]
#     search_fields = [
#         "mastercropid",
#         "growingmethodid__growingmethodname",
#         "parentcropid__name",
#         "parentcroptypeid__croptypename",
#         "mastercropid__varietyname",
#         "croptypeid__name",
#     ]
#     list_filter = ["createddate", "parentcropid", "mastercropid", "growingmethodid"]
#     for field in Combinationdata._meta.get_fields():
#         list_display.append(field.name)
#         # search_fields.append(field.name)

# @admin.register(Cropcategory)
# class CropcategoryAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Cropcategory._meta.get_fields()]

def format_params(params):
    if '&' in params:
        params = params.replace('&', '%26')
    return params

post_models = apps.get_app_config('core').get_models()
for model in post_models:
    try:
        @admin.register(model)
        class DetailAdmin(admin.ModelAdmin):
            list_display = []
            list_display_links = []
            readonly_fields = []
            list_filter = []
            # search_fields = []

            if (model._meta.model_name == "combinationdata"):
                # raw_id_fields = ['parentcroptypeid']
                search_fields = [
                    "growingmethodid__growingmethodname",
                    "parentcropid__name",
                    "parentcroptypeid__croptypename",
                    "mastercropid__varietyname",
                    "croptypeid__name",
                ]
                
                list_display_links.append(model._meta.fields[0].name)
                list_display.append("Suggestions")

                def Suggestions(self, obj):
                    url = reverse('chatbot:chatbot', args=[self.model._meta.model_name])
                    parentcropid = format_params(str(obj.parentcropid))
                    mastercropid = format_params(str(obj.mastercropid))
                    growingmethodid = format_params(str(obj.growingmethodid))

                    link = "<a target='_blank' href='{}?parentcropid={}&mastercropid={}&growingmethodid={}'>Get Suggest</a>".format(
                        url, parentcropid, mastercropid, growingmethodid)
                    return format_html(link)
    
            for f in model._meta.fields:
                field_name = f.name
                # list_display_links.append(field_name)
                list_display.append(field_name)
                # if (model._meta.model_name != "combinationdata"):
                #     search_fields.append(field_name)

                if field_name in ("createddate", "modifieddate"):
                    readonly_fields.append(field_name)
                if field_name in ("createddate", "parentcropid", "mastercropid", "growingmethodid"):
                    list_filter.append(field_name)
                
        # admin.site.register(model, DetailAdmin)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.index_title = "Combination Data Admin"
admin.site.site_header = "Tend Admin"
admin.site.site_title = "Tend Combination Data Admin Portal"