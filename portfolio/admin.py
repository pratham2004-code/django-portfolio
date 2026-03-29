from django.contrib import admin
from .models import SkillCategory, Skill, Project, Education, ContactMessage

admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(ContactMessage)

