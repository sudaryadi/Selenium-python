from pageObjects.registrationForm import Registration
from time import sleep


class TestRegister:
    base_url = "https://demoqa.com/"
    first = "Uchiha"
    last = "Senju"
    email = "senju@gmail.com"
    male = "male"
    mobile = "08992995299"
    birthdate = "15 November 1993"
    subjects = "Ilmu Komputer"
    picture = "images/img.png"
    address = "Bandung"

    def test_filling_registration_form(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # import method dari folder page objects #
        self.reg = Registration(self.driver)
        sleep(3)
        self.reg.select_forms()
        sleep(3)
        self.reg.select_practice_form()
        sleep(3)
        self.reg.input_first_name(self.first)
        self.reg.input_last_name(self.last)
        sleep(3)
        self.reg.input_email(self.email)
        sleep(3)
        self.reg.select_gender_male()
        sleep(3)
        self.reg.input_phone_number(self.mobile)
        sleep(3)
        self.reg.input_dob(self.birthdate)
        sleep(3)
        self.reg.input_subjects(self.subjects)
        sleep(3)
        self.reg.select_hobbies()
        sleep(3)
        self.reg.input_picture(self.picture)
        sleep(3)
        self.reg.input_address(self.address)
        sleep(3)
        self.reg.select_stat()
        sleep(3)
        self.reg.select_city()
        sleep(3)
        self.reg.click_submit()
