import requests

class Roles():
    #baseurl = 'http://pulse-rest-testing.herokuapp.com/'

    def add_dic(self, name, type, level, book):
        self.dic = {}
        self.dic.setdefault('name', name)
        self.dic.setdefault('type', type)
        self.dic.setdefault('level', level)
        self.dic.setdefault('book', book)
        return self.dic

    def add_role(self, baseurl, data_dic):
        role_post = requests.post(baseurl + "roles/", data=data_dic)
        status_code = role_post.status_code
        role_id = role_post.json()
        id = role_id['id']
        l = {}
        l.setdefault('status_code', status_code)
        l.setdefault('id', id)
        return l

    def change_role(self, baseurl, id, name, type, level, book):
        res = requests.put(baseurl+"roles/"+str(id)+'/', data={'name': name, 'type': type, 'level': level, 'book': book})
        res_change = res.json()
        return res_change

    def delete_role(self, baseurl, id):
        r = requests.delete(baseurl + "roles/" + str(id))
        status_code = r.status_code
        return status_code