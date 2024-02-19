from django.utils import timezone
from django.forms import ChoiceField
from rest_framework import serializers

from .models import PublishedManager, Subject, User


# class SubjectSerializer(serializers.Serializer):
#     class SubjectSerializer(serializers.Serializer):
#         title = serializers.CharField(max_length=100)
#         author = serializers.ForeignKey(User, 
#                                 on_delete=models.CASCADE, 
#                                 related_name='subject_name')
#         slug = serializers.SlugField(max_length=100)
#         body = serializers.TextField()
#         publish = serializers.DateField(default=timezone.now)
#         created = serializers.DateField(auto_now_add=True)
#         status = serializers.CharField(max_length=10,
#                                 choices=Status.choices,
#                                 default=Status.PUBLISHED)
#         liked = serializers.ManyToManyField(User, blank=True, through='Like')
#         category = serializers.ForeignKey('Category', blank=True, on_delete=models.PROTECT)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'