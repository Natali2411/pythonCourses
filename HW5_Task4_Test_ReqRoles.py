from HW5_Task4_ReqRoles import Roles
import unittest
import requests
import re

class Test_Req_Roles(unittest.TestCase):
    baseurl = 'http://pulse-rest-testing.herokuapp.com/'

    def test_add_role(self):
        r = Roles.add_dic(self,'Elizabeth','daughter', 1, 2)
        self.assertEqual(len(self.dic), 4)
        role1 = Roles.add_role(self, self.baseurl, r)
        self.assertRegex(str(role1['status_code']), re.compile(r'2+\d'))
        self.assertTrue(role1['id'])

    def test_change_role(self):
        r = requests.get(self.baseurl+"roles/")
        t = r.json()
        l = []
        for i in t:
            l.append(i['id'])
        l = sorted(l)
        par_id = l[-1]
        Roles.change_role(self, self.baseurl, str(par_id), 'Lidia', 'small daughter', 2, 2)
        ch = requests.get(self.baseurl + "roles/" + str(par_id) + '/')
        ch_js = ch.json()

        self.assertEqual(ch_js['name'], 'Lidia')
        self.assertEqual(ch_js['type'], 'small daughter')
        self.assertEqual(ch_js['level'], 2)
        self.assertEqual(ch_js['book'], 2)

    def test_delete_role(self):
        r = requests.get(self.baseurl + "roles/")
        t = r.json()
        l = []
        for i in t:
            l.append(i['id'])
        l = sorted(l)
        par_id = l[-1]
        self.assertRegex(str(Roles.delete_role(self, self.baseurl, str(par_id))), re.compile(r'2+\d'))





