from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# ---------------------------------------------------- DATA LIST ---------------------------------------------------- #

# ========= SSO MERCUBUANA ACCOUNT ========= #
username = "41523010XXX" # REPLACE WITH STUDENT IDENTIFICATION NUMBER (NIM)
password = "123456789"  # REPLACE WITH YOUR SIA PASSWORD
# ========================================== #


# ================================ URL & TARGET ================================  #
sia = "http://sia.mercubuana.ac.id"
survey = "https://survey-bkp.mercubuana.ac.id/mahasiswa/question"
target_username = "username"
target_password = "password"
login = '/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/input'
sign_in = '/html/body/div/div[2]/div[2]/form/div[3]/div[2]/button'
pop_up = "/html/body/div[6]/div[1]/button"
student_details = "/html/body/div[1]/div[1]/form/div/div[1]/div/table/tbody/tr/td[2]/div/ul/li[2]/a"
khs_button = '//*[@id="khs_lst"]/a'
view_khs = '//*[@id="main_form"]/div/div[3]/div[2]/div[2]/div[1]/table/tbody/tr/td[4]/button'
# ================================================================================= #


# ================================ SURVEY ANSWERS  ================================  #
# ('TABLE FOR EXPECTATION SURVEY ANSWERS')   ('TABLE FOR SATISFACTION SURVEY ANSWERS')
#   "#h1.harapan" = Sangat Penting           "#k4.kepuasan" = Sangat Puas
#   "#h2.harapan" = Penting                  "#k3.kepuasan" = Puas
#   "#h3.harapan" = Cukup Penting            "#k2.kepuasan" = Cukup Puas
#   "#h4.harapan" = Ttdak Penting            "#k.kepuasan" = Tidak Puas
# ================================================================================= #


# ================================================== SERVICE UNIT  ==================================================  #
checkboxes_service_unit = [
    "#h1.harapan286",  "#k4.kepuasan286", # 1. Layanan Fakultas/Program Studi tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan283",  "#k4.kepuasan283", # 2. Staf Layanan Fakultas/Program Studi memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan282",  "#k4.kepuasan282", # 3. Layanan Tata Usaha Fakultas/Program Studi memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan285",  "#k4.kepuasan285", # 4. Staf layanan Fakultas/Program Studi memiliki sikap sopan, santun, dan ramah
    "#h1.harapan284",  "#k4.kepuasan284", # 5. Staf layanan Fakultas/Program Studi menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan281",  "#k4.kepuasan281", # 6. Layanan Biro Teknologi Informasi tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan278",  "#k4.kepuasan278", # 7. Staf Biro Teknologi Informasi memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan277",  "#k4.kepuasan277", # 8. Layanan Biro Teknologi Informasi memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan280",  "#k4.kepuasan280", # 9. Staf Biro Teknologi Informasi memiliki sikap sopan, santun, dan ramah
    "#h1.harapan279",  "#k4.kepuasan279", # 10. Staf Biro Teknologi Informasi menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan276",  "#k4.kepuasan276", # 11. Layanan operasional kepuasan pengguna tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan273",  "#k4.kepuasan273", # 12. Staf layanan operasional kepuasan pengguna memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan272",  "#k4.kepuasan272", # 13. Layanan operasional kepuasan pengguna memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan275",  "#k4.kepuasan275", # 14. Staf layanan operasional kepuasan pengguna memiliki sikap sopan, santun, dan ramah
    "#h1.harapan274",  "#k4.kepuasan274", # 15. Staf layanan operasional kepuasan pengguna menguasai dan transparan dalam memberikan pelayanan
]
# CUSTOMIZE YOUR SURVEY ANSWERS WITH THE TABLE ABOVE VARIABLE CHECKBOXES

advice_layanan_unit = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
# ========================================================================================================================= #


# =================================== ACADEMIC AND LEARNING ATMOSPHERE  ===================================  #
course_checkboxes = [
    "#h1.harapan263", "#k4.kepuasan263", # 1. Keberagaman suku, agama, ras, gender, dan disabilitas yang harmoni di UMB.
    "#h1.harapan260", "#k4.kepuasan260", # 2. Kegiatan akademik berjalan kondusif di UMB.
    "#h1.harapan261", "#k4.kepuasan261", # 3. Kegiatan ilmiah dan pengabdian kepada masyarakat diselenggarakan secara rutin di UMB (mis: bakti sosial dan seminar) melibatkan mahasiswa di UMB.
    "#h1.harapan262", "#k4.kepuasan262", # 4. Pelayanan tenaga kependidikan yang baik di UMB.
    "#h1.harapan264", "#k4.kepuasan264", # 5. Sarana dan prasarana fisik maupun jaringan internet yang baik di UMB.
    "#h1.harapan270", "#k4.kepuasan270", # 6. Dosen menginformasikan tata tertib perkuliahan dan memberikan kecukupan bahan/materi pembelajaran di kelas.
    "#h1.harapan271", "#k4.kepuasan271", # 7. Ketersediaan ruang kelas dan fasilitasnya seperti komputer, internet, mic, AC, Spidol, dan projector yang berfungsi dengan baik.
    "#h1.harapan269", "#k4.kepuasan269", # 8. Sistem perkuliahan online cepat dan mudah diakses.
    "#h1.harapan265", "#k4.kepuasan265", # 9. Dosen bersedia membantu mahasiswa dalam memecahkan masalah dan menanggapi pertanyaan serta komentar mahasiswa.
    "#h1.harapan268", "#k4.kepuasan268", # 10.Dosen secara konsisten memberikan materi dan penilaian secara terbuka serta terencana.
    "#h1.harapan267", "#k4.kepuasan267", # 11.Dosen peduli dan memotivasi mahasiswa untuk melakukan yang terbaik.
    "#h1.harapan266", "#k4.kepuasan266", # 12.Dosen menguasai materi yang diberikan serta bersifat adil dan tidak memihak dalam memberikan penilaian.
] # CUSTOMIZE YOUR SURVEY ANSWERS WITH THE TABLE ABOVE VARIABLE CHECKBOXES

advice1 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice2 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice3 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice4 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice5 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice6 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice7 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice8 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice9 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
# ============================================================================================================= #


# ---------------------------------------------------- FUNCTION & TARGET DATA ---------------------------------------------------- #

# =================================== TARGET XPATH  ===================================  #
delay = 0.3 #CUSTOMIZE THE DELAY TIME OF EACH PROCESS YOU WANT.
auto_scroll = "window.scrollBy(0, 30);"
success = "All checkboxes processed successfully."
failed = "Some checkboxes could not be clicked."
layan_unit = '/html/body/div/div[1]/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]/form/button'
course = '/html/body/div/div[1]/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[3]/form/button'
# =================================================================================== #


# =================================== COURSES TAKEN ===================================  #
course1 = '//*[@id="questionsdosentbl"]/tbody/tr[1]/td[4]/a'
course2 = '//*[@id="questionsdosentbl"]/tbody/tr[2]/td[4]/a'
course3 = '//*[@id="questionsdosentbl"]/tbody/tr[3]/td[4]/a'
course4 = '//*[@id="questionsdosentbl"]/tbody/tr[4]/td[4]/a' 
course5 = '//*[@id="questionsdosentbl"]/tbody/tr[5]/td[4]/a' 
course6 = '//*[@id="questionsdosentbl"]/tbody/tr[6]/td[4]/a' 
course7 = '//*[@id="questionsdosentbl"]/tbody/tr[7]/td[4]/a' 
course8 = '//*[@id="questionsdosentbl"]/tbody/tr[8]/td[4]/a' 
course9 = '//*[@id="questionsdosentbl"]/tbody/tr[9]/td[4]/a'
# If the courses taken are less than 9, please delete the line of code above. Because if you take 24 credits, the default is 9 courses.
# =================================================================================== #


# =================================== FUNCTION FOR SURVEYING SERVICE UNIT ===================================  #
def survey_unit_layanan(driver, checkboxes_unit_layanan, auto_scroll, advice, delay, success, failed):
    all_clicked = True  # Flag to check if all checkboxes are clicked

    for checkbox in checkboxes_unit_layanan:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, checkbox))
            )
            ActionChains(driver).move_to_element(element).perform()
            element.click()
            
            # Auto scroll
            driver.execute_script(auto_scroll)
            
        except Exception as e:
            print(f"Error clicking checkbox {checkbox}: {e}")
            all_clicked = False  # Set flag to False if any click fails

    # Check if all checkboxes were clicked successfully
    if all_clicked:
        print(success)
    else:
        print(failed)

    # Inputting Suggestions
    saran = driver.find_element(By.NAME, "saran")
    saran.send_keys(advice)
    time.sleep(delay)

    # Submit Survey
    submit_survey = driver.find_element(By.NAME, "save-data")
    submit_survey.click()
    time.sleep(delay)
# =================================================================================== #


# =================================== FUNCTION FOR COURSE SURVEY ===================================  #
def proses_survey(driver, checkboxes_matakuliah, auto_scroll, advice, delay, success, failed):
    all_clicked = True  # Flag to check if all checkboxes are clicked

    for checkbox in checkboxes_matakuliah:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, checkbox))
            )
            ActionChains(driver).move_to_element(element).perform()
            element.click()
            
            # Auto scroll
            driver.execute_script(auto_scroll)
            
        except Exception as e:
            print(f"Error clicking checkbox {checkbox}: {e}")
            all_clicked = False  # Set flag to False if any click fails

    # Check if all checkboxes were clicked successfully
    if all_clicked:
        print(success)
    else:
        print(failed)

    # Inputting Suggestions
    saran = driver.find_element(By.NAME, "saran")
    saran.send_keys(advice)
    time.sleep(delay)

    # Submit Survey
    submit_survey = driver.find_element(By.NAME, "save-answer")
    submit_survey.click()
    time.sleep(delay)
# =================================================================================== #


# ---------------------------------------------------- MAIN PROGRAM ---------------------------------------------------- #

# Inisialisasi driver Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Mengakses URL
driver.get(survey)
time.sleep(delay)

# Enter Username Survey BKP Mercubuana
username_survey = driver.find_element(By.NAME, target_username)
username_survey.send_keys(username)
time.sleep(delay)

# Enter Pssword Survey BKP Mercubuana
password_survey = driver.find_element(By.NAME, target_password)
password_survey.send_keys(password)
time.sleep(delay)

# Sing In button
sign_in__button = driver.find_element(By.XPATH, sign_in)
sign_in__button.click()
time.sleep(delay)


# =================================== SERVICE UNIT ===================================  #
unit_Layanan__button = driver.find_element(By.XPATH, layan_unit)
unit_Layanan__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
survey_unit_layanan(driver, checkboxes_service_unit, auto_scroll, advice_layanan_unit, delay, success, failed)
# ===================================================================================  #


# =================================== FIRST COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course1)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice1, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== SECOND COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course2)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice2, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== THIRD COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course3)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice3, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== FOURTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course4)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice4, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== FIFTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course5)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice5, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== SIXTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course6)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice6, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== SEVENTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course7)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice7, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== EIGHTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course8)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice8, delay, success, failed)
# Auto scroll
driver.execute_script(auto_scroll)
# ===================================================================================  #


# =================================== NINTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

driver.execute_script("window.scrollBy(0, 100)")
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course9)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice9, delay, success, failed)
# ===================================================================================  #


# ============== Open SIA again to view KHS ============== #
# Mengakses URL
driver.get(sia)
time.sleep(delay)

# Enter Username SIA Mercubuana
username_sia = driver.find_element(By.NAME, target_username)
username_sia.send_keys(username)
time.sleep(delay)

# Enter Password SIA Mercubuana
password_sia = driver.find_element(By.NAME, target_password)
password_sia.send_keys(password)
time.sleep(delay)

# login button
login_button = driver.find_element(By.XPATH, login)
login_button.click()
time.sleep(delay)

# Closing the Pop Up
pop_up_button = driver.find_element(By.XPATH, pop_up)
pop_up_button.click()
time.sleep(delay)

# Click the Student Details button
detail_student_button = driver.find_element(By.XPATH, student_details)
detail_student_button.click()
time.sleep(delay)

# Click the KHS button
khs_button = driver.find_element(By.XPATH, khs_button)
khs_button.click()
time.sleep(delay)

# Finding the dropdown
dropdown = Select(
    driver.find_element
    (
        By.XPATH,
        '//*[@id="periode"]'
    )
)
time.sleep(delay)

# Choose an option for even 2023 (Semester 2)
dropdown.select_by_visible_text("Genap 2023")
time.sleep(delay)

# # Click the View KHS button
# view_khs = driver.find_element(By.XPATH, view_khs)
# view_khs.click()

# Leaving the browser open for 1 hour
time.sleep(3600)