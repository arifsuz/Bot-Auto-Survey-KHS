from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# DATA LIST 

# Jawaban Survey
checkboxes = [
    "harapan178", "kepuasan178", "harapan179", "kepuasan179", "harapan175", "kepuasan175",
    "harapan176", "kepuasan176", "harapan177", "kepuasan177", "harapan184", "kepuasan184",
    "harapan185", "kepuasan185", "harapan258", "kepuasan258", "harapan186", "kepuasan186",
    "harapan180", "kepuasan180", "harapan254", "kepuasan254", "harapan257", "kepuasan257",
    "harapan183", "kepuasan183", "harapan256", "kepuasan256", "harapan182", "kepuasan182",
    "harapan181", "kepuasan181", "harapan255", "kepuasan255", "harapan233", "kepuasan233",
    "harapan232", "kepuasan232", "harapan234", "kepuasan234", "harapan236", "kepuasan236",
    "harapan235", "kepuasan235", "harapan238", "kepuasan238", "harapan237", "kepuasan237",
    "harapan226", "kepuasan226", "harapan223", "kepuasan223", "harapan222", "kepuasan222",
    "harapan225", "kepuasan225", "harapan224", "kepuasan224", "harapan253", "kepuasan253",
    "harapan250", "kepuasan250", "harapan249", "kepuasan249", "harapan252", "kepuasan252",
    "harapan251", "kepuasan251", "harapan201", "kepuasan201", "harapan198", "kepuasan198",
    "harapan197", "kepuasan197", "harapan200", "kepuasan200", "harapan199", "kepuasan199", 
    "harapan248", "kepuasan248", "harapan245", "kepuasan245", "harapan244", "kepuasan244", 
    "harapan247", "kepuasan247", "harapan246", "kepuasan246", "harapan191", "kepuasan191", 
    "harapan188", "kepuasan188", "harapan187", "kepuasan187", "harapan190", "kepuasan190", 
    "harapan189", "kepuasan189", "harapan216", "kepuasan216", "harapan213", "kepuasan213", 
    "harapan212", "kepuasan212", "harapan215", "kepuasan215", "harapan214", "kepuasan214", 
    "harapan221", "kepuasan221", "harapan218", "kepuasan218", "harapan217", "kepuasan217", 
    "harapan220", "kepuasan220", "harapan219", "kepuasan219", "harapan206", "kepuasan206", 
    "harapan203", "kepuasan203", "harapan202", "kepuasan202", "harapan205", "kepuasan205", 
    "harapan204", "kepuasan204", "harapan211", "kepuasan211", "harapan208", "kepuasan208", 
    "harapan207", "kepuasan207", "harapan210", "kepuasan210", "harapan209", "kepuasan209", 
    "harapan243", "kepuasan243", "harapan240", "kepuasan240", "harapan239", "kepuasan239", 
    "harapan242", "kepuasan242", "harapan241", "kepuasan241", "harapan231", "kepuasan231", 
    "harapan228", "kepuasan228", "harapan227", "kepuasan227", "harapan230", "kepuasan230",
    "harapan229", "kepuasan229"
]

# Inisialisasi driver Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Mengakses URL
driver.get("http://sia.mercubuana.ac.id")
time.sleep(1)

# Enter Username SIA Mercubuana
username = driver.find_element(By.NAME, "username")
username.send_keys("41523010147")
time.sleep(1)

# Enter Password SIA Mercubuana
password = driver.find_element(By.NAME, "password")
password.send_keys("0123456789")
time.sleep(1)

# login button
login_button = driver.find_element(
    By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/input"
)
login_button.click()
time.sleep(1)

# Closing the Pop Up
pop_up_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/button")
pop_up_button.click()
time.sleep(1)

# Click the Student Details button
detail_student_button = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/form/div/div[1]/div/table/tbody/tr/td[2]/div/ul/li[2]/a",
)
detail_student_button.click()
time.sleep(1)

# Click the View KHS button
khs_button = driver.find_element(By.XPATH, '//*[@id="khs_lst"]/a')
khs_button.click()
time.sleep(1)

# Finding the dropdown
dropdown = Select(driver.find_element(By.XPATH, '//*[@id="periode"]'))
time.sleep(1)

# Choose an option for even 2023 (Semester 2)
dropdown.select_by_visible_text("Genap 2023")
time.sleep(1)

# Login button to fill out the survey
survey_button = driver.find_element(
    By.XPATH,
    '//*[@id="main_form"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[4]/center/font/a',
)
survey_button.click()
time.sleep(1)

# Enter Username Survey BKP Mercubuana
username_survey = driver.find_element(By.NAME, "username")
username_survey.send_keys("41523010147")
time.sleep(1)

# Enter Pssword Survey BKP Mercubuana
password_survey = driver.find_element(By.NAME, "password")
password_survey.send_keys("0123456789")
time.sleep(1)

# Sing In button
sign_in__button = driver.find_element(
    By.XPATH, "/html/body/div/div[2]/div[2]/form/div[3]/div[2]/button"
)
sign_in__button.click()
time.sleep(1)

# Student Survey button
student_survey__button = driver.find_element(
    By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[4]/a"
)
student_survey__button.click()
time.sleep(1)

# Click the Fill out Survey button
survey__button = driver.find_element(
    By.XPATH, '//*[@id="questionsdosentbl"]/tbody/tr[1]/td[4]/a'
)
survey__button.click()
time.sleep(1)

all_clicked = True  # Flag to check if all checkboxes are clicked

for checkbox in checkboxes:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, checkbox))
        )
        ActionChains(driver).move_to_element(element).perform()
        element.click()
        time.sleep(0.5)
        
        # Auto scroll
        driver.execute_script("window.scrollBy(0, 30);")
        time.sleep(0.5)
        
    except Exception as e:
        print(f"Error clicking checkbox {checkbox}: {e}")
        all_clicked = False  # Set flag to False if any click fails

# Check if all checkboxes were clicked successfully
if all_clicked:
    print("All checkboxes processed successfully.")
else:
    print("Some checkboxes could not be clicked.")


# Inputting Suggestions
saran = driver.find_element(
    By.NAME,
    "saran"
)
saran.send_keys(
    "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem"
)
time.sleep(1)

# Submit Survey
sumbit_survey = driver.find_element(
    By.NAME,
    "save-answer"
)
sumbit_survey.click()
time.sleep(1)

# Closing the browser
driver.quit()