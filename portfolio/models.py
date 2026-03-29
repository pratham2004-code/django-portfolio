from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name
    class Meta: verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    def __str__(self): return f"{self.name} ({self.category.name})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_link = models.URLField(blank=True, null=True)
    def __str__(self): return self.title
    def get_tech_list(self): return [tech.strip() for tech in self.tech_stack.split(',')]

class Education(models.Model):
    institution = models.CharField(max_length=250)
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    def __str__(self): return self.institution

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Message from {self.name}"