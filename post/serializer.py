from .models import Post #모델을 기반으로 직렬화 시키기 위함
from rest_framework import serializers #레스트 프레임워크로부터 inport

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post #post 모델안의
        fields = ('id', 'title', 'body') #모든 필드들을 상속 받을 것임

        read_only_fields = ('title',) #write_only_fields = ('',) 튜플의 형태
