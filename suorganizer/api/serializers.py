from rest_framework import serializers
from organizer.models import Startup

class StartupSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Startup
        fields = ('name', 'slug', 'description',
            'founded_date', 'contact', 'website', 'tags')
        # lookup_field = 'slug'