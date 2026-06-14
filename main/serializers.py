from rest_framework import serializers
from .models import Company, Building, Worker, Comment


class BuildingSerializerForCompany(serializers.ModelSerializer):
    workers = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    class Meta:
        model = Building
        exclude = ["company",]



class CompanySerializer(serializers.ModelSerializer):
    buildings = BuildingSerializerForCompany(many=True)

    class Meta:
        model = Company
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        buildings = validated_data.pop("buildings")
        company = Company.objects.create(**validated_data)
        for building_data in buildings:
            workers = building_data.pop("workers", [])
            building = Building.objects.create(company=company, **building_data)
            if workers:
                building.workers.set(workers)
            
        return company
    
    def update(self, instance, validated_data):
        buildings = validated_data.pop('buildings', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()

        if buildings:
            instance.buildings.all().delete()

            for building_data in buildings:
                workers = building_data.pop("workers", [])
                building = Building.objects.create(company=instance, **building_data)
                if workers:
                    building.workers.set(workers)
        
        return instance


class BuildingSerializerForWorker(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Building
        exclude = ["workers",]



class WorkerSerializer(serializers.ModelSerializer):
    buildings = BuildingSerializerForWorker(many=True)

    class Meta:
        model = Worker
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        buildings = validated_data.pop("buildings", None)
        worker = Worker.objects.create(**validated_data)
        if buildings:
            for building_data in buildings:
                building = Building.objects.create(**building_data)
                building.workers.set([worker])
        return worker
    
    def update(self, instance, validated_data):
        buildings = validated_data.pop("buildings", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if buildings:
            for building in instance.buildings.all():
                building.workers.clear()


            for building_data in buildings:
                building = Building.objects.create(**building_data)
                building.workers.set([instance])

        return instance




class BuildingSerializer(serializers.ModelSerializer):
    company_write = serializers.ChoiceField(choices=Company.objects.all(), write_only=True)
    worker_write = serializers.MultipleChoiceField(choices=Worker.objects.all(), write_only=True)

    class Meta:
        model = Building
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        company_write = validated_data.pop("company_write")
        worker_write = validated_data.pop("worker_write")

        building = Building.objects.create(company=company_write, **validated_data)
        building.workers.set(worker_write)
        return building
    
    def update(self, instance, validated_data):
        instance.company = validated_data.pop("company_write", instance.company)
        worker_write = validated_data.pop("worker_write", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if worker_write:
            instance.workers.set(worker_write)
        return instance
        


    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'