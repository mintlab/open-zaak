from django.conf import settings

from rest_framework import status
from vng_api_common.tests import get_validation_errors, reverse

from openzaak.utils.tests import APITestCaseCMIS, JWTAuthMixin

from ..models import Gebruiksrechten, ObjectInformatieObject
from .factories import (
    EnkelvoudigInformatieObjectCanonicalFactory,
    EnkelvoudigInformatieObjectFactory,
    GebruiksrechtenCMISFactory,
    GebruiksrechtenFactory,
)


class GebruiksrechtenFilterTests(JWTAuthMixin, APITestCaseCMIS):
    heeft_alle_autorisaties = True

    def test_filter_by_invalid_url(self):
        response = self.client.get(
            reverse(Gebruiksrechten), {"informatieobject": "bla"}
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error = get_validation_errors(response, "informatieobject")
        self.assertEqual(error["code"], "invalid")

    def test_filter_by_valid_url_object_does_not_exist(self):
        if settings.CMIS_ENABLED:
            eio = EnkelvoudigInformatieObjectFactory.create()
            eio_url = reverse(eio)
            GebruiksrechtenCMISFactory(informatieobject=eio_url)
        else:
            eio = EnkelvoudigInformatieObjectCanonicalFactory.create(
                latest_version__informatieobjecttype__concept=False
            )
            GebruiksrechtenFactory.create(informatieobject=eio)

        response = self.client.get(
            reverse(Gebruiksrechten), {"informatieobject": "https://google.com"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])


class ObjectInformatieObjectFilterTests(JWTAuthMixin, APITestCaseCMIS):
    heeft_alle_autorisaties = True

    def test_filter_by_invalid_url(self):
        for query_param in ["informatieobject", "object"]:
            with self.subTest(query_param=query_param):
                response = self.client.get(
                    reverse(ObjectInformatieObject), {query_param: "bla"}
                )

                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

                error = get_validation_errors(response, query_param)
                self.assertEqual(error["code"], "invalid")

    def test_filter_by_valid_url_object_does_not_exist(self):
        for query_param in ["informatieobject", "object"]:
            with self.subTest(query_param=query_param):
                response = self.client.get(
                    reverse(ObjectInformatieObject), {query_param: "https://google.com"}
                )

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data, [])
