from rest_framework import serializers
from Foods.models import Foods

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foods #序列化的模型
        fields = ["id","name","price","picture","description"]#序列化返回的字段

