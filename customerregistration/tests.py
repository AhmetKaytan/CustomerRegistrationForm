from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from customerregistration.models import Customer
from customerregistration.forms import CustomerForm

class customerFieldTest(TestCase):

    def setUp(self) -> None:
        self.Customer= Customer(tc_no = '01234567891', name = 'Ahmet', surname = 'Kaytan', 
        phone_no = '05055320023', city = 'İzmir', district = 'Karabağlar')
    
    def test_field_tc(self):
        field_label=self.Customer.Meta.get_field('tc_no').verbose_name
        self.assertEqual(field_label, 'tc_no')

    def test_field_name(self):
        field_label=self.Customer.Meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_field_surname(self):
        field_label=self.Customer.Meta.get_field('surname').verbose_name
        self.assertEqual(field_label, 'surname')
    
    def test_object_name(self):
        expected_object= f'{self.customer.name}, {self.customer.surname}'
        self.assertEqual(str(self.Customer),expected_object)

    
class mainPageTest(TestCase):

    def test_main_page_staus_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_page_surl_name(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')


class detailCustomerPageTest():

    def setUp(self) -> None:
        self.Customer= Customer(tc_no = '01234567891', name = 'Ahmet', surname = 'Kaytan', 
        phone_no = '05055320023', city = 'İzmir', district = 'Karabağlar')

    def test_detail_customer_page_status_code(self):
        response = self.client.get('/detail/')
        self.assertEqual(response.status_code, 404)

    def test_detail_page_url_name(self):
        response = self.client.get(reverse('detail', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('detail', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')


class newCustomerFormTest(TestCase):
    
    def test_valid_data(self):
        data = {'tc_no':'01234567891', 'name':'Ahmet', 'surname':'Kaytan', 'phone_no':'05055320023', 'city':'İzmir', 'district':'Karabağlar'}
        form = CustomerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = CustomerForm({'name':'Ahmet', 'surname':'Kaytan', 'phone_no':'05055320023', 'city':'İzmir', 'district':'Karabağlar'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'tc_no' : ['This field is necessary']})

    def test_form_error(self):
        form = CustomerForm({'tc_no':'0', 'name':'Ahmet', 'surname':'Kaytan', 'phone_no':'05055320023', 'city':'İzmir', 'district':'Karabağlar'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'__all__': ['Information is incorrect!']})

class loginTest(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(username = 'test', password = 'testing')

    def test_login(self):
        self.client.login(username = 'test', password = 'testing')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response)