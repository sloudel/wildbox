from rest_framework import serializers

from .models import Url

# TODO bulk create/update
# class UrlListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         url_objects = [Url(**item) for item in validated_data]
#         return Url.objects.bulk_create(url_objects)
    
#     def update(self, instance, validated_data):
#         url_mapping = {url_object.id: url_object for url_object in instance}
#         data_mapping = {item['id']: item for item in validated_data}

#         # create or update
#         ret = []
#         for url_id, data in data_mapping.items():
#             url_object = url_mapping.get(url_id, None)
#             if url_object is None:
#                 ret.append(self.child.create(data))
#             else:
#                 ret.append(self.child.update(url_object, data))

#         # delete
#         for url_id, url_object in url_mapping.items():
#             if url_id not in data_mapping:
#                 url_object.delete()

#         return ret

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        # list_serializer_class = UrlListSerializer
        fields = [
            'id', 'url', 'status_code', 'is_ok', 'created_date', 'modified_date'
        ]
        extra_kwargs = {'url': {'required': False}}
