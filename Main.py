from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task #deneme yapıyorum
    def get_user_info(self):
        self.client.get("/v2/user/ismailAydemir2")

    @task
    def get_login(self):
        params_payload = {
            "username": "ismailAydemirrrrr",
            "password": "Deneme1"
        }
        self.client.get("/v2/user/login",params=params_payload)

    @task
    def post_user_create(self, null=None):
        body_payload = {
            "id": 1457843,
            "username": "ismailAydemir2",
            "firstName":"ismail2",
            "lastName":"aydemir2",
            "email":"ismailaydemir2@gmail.com",
            "password":"Deneme1",
            "phone":null,
            "userStatus":1,
        }
        headers_payload = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.client.post("/v2/user", json=body_payload, headers=headers_payload)

    @task
    def post_update_user(self):
        body_payload = {
            "id": 145784334,
            "username": "Yeni",
            "firstName": "yeniisim",
            "lastName": "yenisoyisim",
            "email": "aydemir232@gmail.com",
            "password": "123456",
            "phone":"14255487487",
            "userStatus": 0,
        }
        headers_payload = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.client.put("/v2/user/ismailTest", json=body_payload, headers=headers_payload)

    @task
    def delete_user(self):
        self.client.delete("/v2/user/ismailAydemir2")

    @task
    def get_logout(self):
        self.client.get("/v2/user/logout")

    @task
    def post_create_witharray(self):
        body_payload =[ {
            "id": 145784334,
            "username": "Yeni",
            "firstName": "yeniisim",
            "lastName": "yenisoyisim",
            "email": "aydemir232@gmail.com",
            "password": "123456",
            "phone": "14255487487",
            "userStatus": 1,
        },

        {
            "id": 145784334,
            "username": "Yeni2",
            "firstName": "yeniisim2",
            "lastName": "yenisoyisim2",
            "email": "aydemir23235@gmail.com",
            "password": "1234567",
            "phone": "14255487481",
            "userStatus": 0,
        }
        ]
        headers_payload = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.client.post("/v2/user/createWithArray", json=body_payload, headers=headers_payload)

    @task
    def post_create_withlist(self):
        body_payload =[ {
            "id": 145784334,
            "username": "Yeni",
            "firstName": "Ğaaa",
            "lastName": "Zart",
            "email": "aydemir232@gmail.com",
            "password": "123456",
            "phone": "14255487487",
            "userStatus": 1,
        },

        {
            "id": 145784334,
            "username": "Yeni2",
            "firstName": "Ğaaa2",
            "lastName": "Zart2",
            "email": "aydemir23235@gmail.com",
            "password": "1234567",
            "phone": "14255487481",
            "userStatus": 0,
        }
            ]
        headers_payload = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.client.post("/v2/user/createWithList", json=body_payload, headers=headers_payload)