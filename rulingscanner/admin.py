from django.contrib import admin


from rulingscanner import models

# i tu wpisujesz nazwy modeli w ten sposób
# admin.site.register(models.Tweet)
# admin.site.register(models.Comment)
# admin.site.register(models.Message)



class TagsAdmin(admin.ModelAdmin):
    pass
class AuthorsAdmin(admin.ModelAdmin):
    pass
class RulingAdmin(admin.ModelAdmin):
    pass
class TaxTypeAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Tag, TagsAdmin)
admin.site.register(models.Authors, AuthorsAdmin)
admin.site.register(models.Ruling, RulingAdmin)
admin.site.register(models.TaxType, TaxTypeAdmin)
admin.site.register(models.Comment, CommentAdmin)

