from django.contrib import admin

from groups.models import Group, Element


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    class Meta:
        model = Group
        fields = '__all__'


class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'name')
    class Meta:
        model = Element
        fields = '__all__'


admin.site.register(Group, GroupAdmin)
admin.site.register(Element, ElementAdmin)