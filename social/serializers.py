from rest_framework import serializers
from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed, Workplace, Education

class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    workplaces = WorkplaceSerializer(many=True)
    educations = EducationSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        workplaces_data = validated_data.pop('workplaces')
        educations_data = validated_data.pop('educations')
        user_profile = UserProfile.objects.create(**validated_data)
        for workplace_data in workplaces_data:
            workplace, created = Workplace.objects.get_or_create(name=workplace_data['name'])
            user_profile.workplaces.add(workplace)
        for education_data in educations_data:
            education, created = Education.objects.get_or_create(name=education_data['name'])
            user_profile.educations.add(education)
        return user_profile

    def update(self, instance, validated_data):
        workplaces_data = validated_data.pop('workplaces')
        educations_data = validated_data.pop('educations')

        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.cover_picture = validated_data.get('cover_picture', instance.cover_picture)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.location = validated_data.get('location', instance.location)
        instance.website = validated_data.get('website', instance.website)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()

        instance.workplaces.clear()
        for workplace_data in workplaces_data:
            workplace, created = Workplace.objects.get_or_create(name=workplace_data['name'])
            instance.workplaces.add(workplace)

        instance.educations.clear()
        for education_data in educations_data:
            education, created = Education.objects.get_or_create(name=education_data['name'])
            instance.educations.add(education)

        return instance

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
