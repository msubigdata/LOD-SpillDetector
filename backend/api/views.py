from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class MetaAPIView(GenericAPIView):

    def get_meta_funcs(self):
        meta_funcs = filter(lambda field: str(field).startswith('meta_'), dir(self.queryset.model))
        return meta_funcs

    @staticmethod
    def execute_meta_funcs(model, meta_funcs):
        for f in meta_funcs:
            getattr(model, f)()

    def get_serialized_meta(self, model):
        serializer = self.serializer_class
        meta = serializer(model).data
        return meta

    def get(self, request, *args, **kwargs):
        model = self.queryset.model()
        meta_funcs = self.get_meta_funcs()

        # Create object, otherwise set many to many objects not impossible
        model.save()
        self.execute_meta_funcs(model, meta_funcs)
        meta = self.get_serialized_meta(model)

        # Remove created object
        model.delete()

        return Response(meta)
    