# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)


from .resource_mapping import RESOURCE_MAPPING


class Zeus_wrapperClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://private-anon-befeaec343-izeusv3.apiary-mock.com/cgi-bin/api/v3'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(Zeus_wrapperClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Zeus_wrapper = generate_wrapper_from_adapter(Zeus_wrapperClientAdapter)
