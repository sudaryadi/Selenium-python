from selenium.webdriver.common.by import By


class Registration:
    menu_forms_xpath = "/html/body/div[2]/div/div/div[2]/div/div[2]"
    submenu_practiceForm_xpath = "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div"
    txt_firstName_id = "firstName"
    txt_lastName_id = "lastName"
    txt_email_id = "userEmail"
    radio_male_xpath = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]"
    txt_mobile_id = "userNumber"
    txt_DoB_id = "dateOfBirth"
    txt_subjects_id = "subjectsContainer"
    check_reading_id = "hobbies-checkbox-2"
    btn_uploadPicture_id = "uploadPicture"
    txt_address_id = "currentAddress"
    list_state_id = "react-select-3-input"
    item_rajasthan_xpath = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]/div[1]"
    list_city_id = "react-select-4-input"
    item_jaipur_xpath = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[10]/div[3]/div/div/div[1]/div[1]"
    btn_submit_id = "submit"

    def __init__(self, setup):
        self.driver = setup

    def select_forms(self):
        self.driver.find_element(By.XPATH, self.menu_forms_xpath).click()

    def select_practice_form(self):
        self.driver.find_element(By.XPATH, self.submenu_practiceForm_xpath).click()

    def input_first_name(self, first):
        self.driver.find_element(By.ID, self.txt_firstName_id).send_keys(first)

    def input_last_name(self, last):
        self.driver.find_element(By.ID, self.txt_lastName_id).send_keys(last)

    def input_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def select_gender_male(self):
        self.driver.find_element(By.XPATH, self.radio_male_xpath).click()

    def input_phone_number(self, mobile):
        self.driver.find_element(By.ID, self.txt_mobile_id).send_keys(mobile)

    def input_dob(self, birthdate):
        self.driver.find_element(By.ID, self.txt_DoB_id).send_keys(birthdate)

    def input_subjects(self, subjects):
        self.driver.find_element(By.ID, self.txt_subjects_id).send_keys(subjects)

    def select_hobbies(self):
        self.driver.find_element(By.ID, self.check_reading_id).click()

    def input_picture(self, picture):
        self.driver.find_element(By.ID, self.btn_uploadPicture_id).send_keys(picture)

    def input_address(self, address):
        self.driver.find_element(By.ID, self.txt_address_id).send_keys(address)

    def select_stat(self):
        self.driver.find_element(By.ID, self.list_state_id).click()
        self.driver.find_element(By.XPATH, self.item_rajasthan_xpath).click()

    def select_city(self):
        self.driver.find_element(By.ID, self.list_city_id).click()
        self.driver.find_element(By.XPATH, self.item_jaipur_xpath).click()

    def click_submit(self):
        self.driver.find_element(By.ID, self.btn_submit_id).click()
