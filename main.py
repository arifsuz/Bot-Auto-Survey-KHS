from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Inisialisasi driver Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Mengakses URL
driver.get("http://sia.mercubuana.ac.id")
time.sleep(1)

# Menginput username
username = driver.find_element(By.NAME, "username")
username.send_keys("41523010147")
time.sleep(1)

# Menginput password
password = driver.find_element(By.NAME, "password")
password.send_keys("1510160815")
time.sleep(1)

# Klik tombol login
login_button = driver.find_element(
    By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/input"
)
login_button.click()
time.sleep(1)

# Menutup Pop Up
pop_up_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/button")
pop_up_button.click()
time.sleep(1)

# Klik tombol Detail Mahasiswa
detail_student_button = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/form/div/div[1]/div/table/tbody/tr/td[2]/div/ul/li[2]/a",
)
detail_student_button.click()
time.sleep(1)

# Klik tombol Lihat KHS
khs_button = driver.find_element(By.XPATH, '//*[@id="khs_lst"]/a')
khs_button.click()
time.sleep(1)

# Menemukan dropdown
dropdown = Select(driver.find_element(By.XPATH, '//*[@id="periode"]'))
time.sleep(1)

# Memilih opsi Genap 2023 (Semester 2)
dropdown.select_by_visible_text("Genap 2023")
time.sleep(1)

# Klik tombol Login Untuk Mengisi Survey
survey_button = driver.find_element(
    By.XPATH,
    '//*[@id="main_form"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[4]/center/font/a',
)
survey_button.click()
time.sleep(1)

# Menginput username_survey
username_survey = driver.find_element(By.NAME, "username")
username_survey.send_keys("41523010147")
time.sleep(1)

# Menginput password_survey
password_survey = driver.find_element(By.NAME, "password")
password_survey.send_keys("1510160815")
time.sleep(1)

# Klik tombol Sing In
sign_in__button = driver.find_element(
    By.XPATH, "/html/body/div/div[2]/div[2]/form/div[3]/div[2]/button"
)
sign_in__button.click()
time.sleep(1)

# Klik Navbar
navbar = driver.find_element(By.XPATH, "/html/body/div/nav/ul[1]/li/a")
navbar.click()
time.sleep(1)

# Klik tombol Mahasiswa Survey
student_survey__button = driver.find_element(
    By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[4]/a"
)
student_survey__button.click()
time.sleep(1)

# Klik tombol Isi Survey
survey__button = driver.find_element(
    By.XPATH, '//*[@id="questionsdosentbl"]/tbody/tr[1]/td[4]/a'
)
survey__button.click()
time.sleep(1)

# Selector XPATH array
selectors = [
    # '//*[@id="h1"]',
    # '//*[@id="k4"]',
    # '//*[@id="h1"]',
    # '//*[@id="k4"]' 
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[1]/td[4]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[1]/td[8]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[2]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[2]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[3]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[3]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[4]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[4]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[5]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[5]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[6]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[6]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[7]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[7]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[8]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[8]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[9]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[9]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[10]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[10]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[11]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[11]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[12]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[12]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[13]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[13]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[14]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[14]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[15]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[15]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[16]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[16]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[17]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[17]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[18]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[19]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[20]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[20]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[21]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[21]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[22]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[22]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[23]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[23]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[24]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[24]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[25]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[25]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[26]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[26]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[27]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[27]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[28]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[28]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[29]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[29]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[30]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[30]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[31]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[31]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[32]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[32]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[33]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[33]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[34]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[34]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[35]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[35]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[36]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[36]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[37]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[37]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[38]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[38]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[39]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[39]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[40]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[40]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[41]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[41]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[42]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[42]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[43]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[43]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[44]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[44]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[45]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[45]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[46]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[46]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[47]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[47]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[48]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[48]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[49]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[49]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[50]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[50]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[51]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[51]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[52]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[52]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[53]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[53]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[54]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[54]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[55]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[55]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[56]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[56]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[57]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[57]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[58]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[58]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[59]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[59]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[60]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[60]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[61]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[61]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[62]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[62]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[63]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[63]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[63]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[63]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[64]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[64]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[65]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[65]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[66]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[66]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[67]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[67]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[68]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[68]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[69]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[69]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[70]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[70]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[71]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[71]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[72]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[72]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[73]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[73]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[74]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[74]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[75]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[75]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[76]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[76]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[77]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[77]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[78]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[78]/td[7]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[79]/td[3]/input',
    '/html/body/div/div[1]/div[2]/div/div/div/div/div/div/div/form/table/tbody/tr[79]/td[7]/input',
]

# Function to click multiple elements
def click_elements(driver, selectors):
    for selector in selectors:
        element = driver.find_element(By.XPATH, selector)
        element.click()

# Call the function to click multiple elements
click_elements(driver, selectors)

time.sleep(10)
# Menutup browser
driver.quit()
