from django.contrib import admin

from Petstagram.main_app.models import Profile, Pet, PetPhoto


class PetInLineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInLineAdmin, )


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
