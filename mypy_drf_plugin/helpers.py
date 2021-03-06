# noinspection PyUnresolvedReferences
from mypy_django_plugin.helpers import get_argument_by_name, get_argument_type_by_name, get_nested_meta_node_for_current_class, \
    has_any_of_bases, is_none_expr, is_optional, iter_over_assignments, make_optional, make_required, parse_bool, \
    reparametrize_instance

FIELD_FULLNAME = 'rest_framework.fields.Field'
BASE_SERIALIZER_FULLNAME = 'rest_framework.serializers.BaseSerializer'
SERIALIZER_FULLNAME = 'rest_framework.serializers.Serializer'
MODEL_SERIALIZER_FULLNAME = 'rest_framework.serializers.ModelSerializer'
