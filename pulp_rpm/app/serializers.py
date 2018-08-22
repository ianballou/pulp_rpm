from pulpcore.plugin.serializers import ContentSerializer, RemoteSerializer, PublisherSerializer

from pulp_rpm.app.models import Package, RpmRemote, RpmPublisher


class PackageSerializer(ContentSerializer):
    """
    A Serializer for Package.

    Add serializers for the new fields defined in Package and add those fields to the Meta class
    keeping fields from the parent class as well. Provide help_text.

    For example::

    field1 = serializers.TextField(help_text="field1 description")
    field2 = serializers.IntegerField(help_text="field2 description")
    field3 = serializers.CharField(help_text="field3 description")

    class Meta:
        fields = ContentSerializer.Meta.fields + ('field1', 'field2', 'field3')
        model = Package
    """

    class Meta:
        fields = ContentSerializer.Meta.fields
        model = Package


class RpmRemoteSerializer(RemoteSerializer):
    """
    A Serializer for RpmRemote.

    Add any new fields if defined on RpmRemote.
    Similar to the example above, in PackageSerializer.
    Additional validators can be added to the parent validators list

    For example::

    class Meta:
        validators = RemoteSerializer.Meta.validators + [myValidator1, myValidator2]
    """

    class Meta:
        fields = RemoteSerializer.Meta.fields
        model = RpmRemote


class RpmPublisherSerializer(PublisherSerializer):
    """
    A Serializer for RpmPublisher.

    Add any new fields if defined on RpmPublisher.
    Similar to the example above, in PackageSerializer.
    Additional validators can be added to the parent validators list

    For example::

    class Meta:
        validators = PublisherSerializer.Meta.validators + [myValidator1, myValidator2]
    """

    class Meta:
        fields = PublisherSerializer.Meta.fields
        model = RpmPublisher
