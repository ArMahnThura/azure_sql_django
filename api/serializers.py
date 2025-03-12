from rest_framework import serializers
from .models import Store 
from .models import Product 
from .models import DateRecord

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']
        
class DateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateRecord
        fields = ['date', 'updated_date']
