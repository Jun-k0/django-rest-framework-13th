from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Profile, Upload, Comment, Like, Upload_file

# rest_framework - RESTful한 api를 만들기 위해
# serialize - json형식으로 소통

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'userid', 'userpw', 'nickname', 'user_image']


class Upload_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_file
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'profile', 'upload']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'profile', 'upload']


class UploadSerializer(serializers.ModelSerializer):
    upload_files = Upload_fileSerializer(many=True)  # related_name !!
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = Upload
        fields = ['id', 'profile', 'description', 'thumbnail', 'upload_files', 'comments', 'likes']
    def validate(self, data):
        if 'Test' not in data['description']:
            raise ValidationError('Validation Error!')
        return data