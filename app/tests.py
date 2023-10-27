from django.test import SimpleTestCase


# Create your tests here.


class TestNearHundred(SimpleTestCase):
    def test_NearHundred_89(self):
        response = self.client.get("/near-hundred/89/")
        self.assertContains(response, "False")

    def test_NearHundred_90(self):
        response = self.client.get("/near-hundred/90/")
        self.assertContains(response, "True")

    def test_NearHundred_93(self):
        response = self.client.get("/near-hundred/93/")
        self.assertContains(response, "True")


class TestStringSplosion(SimpleTestCase):
    def test_StringSplosion_Code(self):
        response = self.client.get("/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_StringSplosion_abc(self):
        response = self.client.get("/string-splosion/abc/")
        self.assertContains(response, "aababc")

    def test_StringSplosion_ab(self):
        response = self.client.get("/string-splosion/ab/")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_CatDog_catdog(self):
        response = self.client.get("/cat-dog/catdog/")
        self.assertContains(response, "True")

    def test_CatDog_catcat(self):
        response = self.client.get("/cat-dog/catcat/")
        self.assertContains(response, "False")

    def test_CatDog_1cat1cadodog(self):
        response = self.client.get("/cat-dog/1cat1cadodog/")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_LoneSum123(self):
        response = self.client.get("/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_LoneSum323(self):
        response = self.client.get("/lone-sum/3/2/3/")
        self.assertContains(response, "2")

    def test_LoneSum333(self):
        response = self.client.get("/lone-sum/3/3/3/")
        self.assertContains(response, "0")
