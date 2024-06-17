from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# --------------------------------- DATA LIST --------------------------------- #

# ========= SIA MERCUBUANA ACCOUNT ========= #
username = "41523010XXX" # REPLACE WITH STUDENT IDENTIFICATION NUMBER (NIM)
password = "123456789"  # REPLACE WITH YOUR SIA PASSWORD


# ========= JUMLAH MATA KULIAH YANG DIAMBIL ========= #
matkul1 = '//*[@id="questionsdosentbl"]/tbody/tr[1]/td[4]/a'
matkul2 = '//*[@id="questionsdosentbl"]/tbody/tr[2]/td[4]/a'
matkul3 = '//*[@id="questionsdosentbl"]/tbody/tr[3]/td[4]/a'
matkul4 = '//*[@id="questionsdosentbl"]/tbody/tr[4]/td[4]/a'
matkul5 = '//*[@id="questionsdosentbl"]/tbody/tr[5]/td[4]/a'
matkul6 = '//*[@id="questionsdosentbl"]/tbody/tr[6]/td[4]/a'
matkul7 = '//*[@id="questionsdosentbl"]/tbody/tr[7]/td[4]/a'
matkul8 = '//*[@id="questionsdosentbl"]/tbody/tr[8]/td[4]/a'
matkul9 = '//*[@id="questionsdosentbl"]/tbody/tr[9]/td[4]/a'
# If the courses taken are less than 9, please delete the line of code above. Because if you take 24 credits, the default is 9 courses.


# ========= CETAK HASIL KHS ========= #
view_khs = '//*[@id="main_form"]/div/div[3]/div[2]/div[2]/div[1]/table/tbody/tr/td[4]/button'


# ========= DELAY TIME ========== #
delay = 0.3 #CUSTOMIZE THE DELAY TIME OF EACH PROCESS YOU WANT.


# ========= SURVEY ANSWERS ========= #
# ('TABLE FOR EXPECTATION SURVEY ANSWERS')   ('TABLE FOR SATISFACTION SURVEY ANSWERS')
#   "#h1.harapan" = Sangat Penting           "#k4.kepuasan" = Sangat Puas
#   "#h2.harapan" = Penting                  "#k3.kepuasan" = Puas
#   "#h3.harapan" = Cukup Penting            "#k2.kepuasan" = Cukup Puas
#   "#h4.harapan" = Ttdak Penting            "#k.kepuasan" = Tidak Puas

checkboxes = [
    "#h1.harapan178", "#k4.kepuasan178", # 1. Keberagaman suku, agama, ras, gender, dan disabilitas yang harmoni di UMB.
    "#h1.harapan179", "#k4.kepuasan179", # 2. Sarana dan prasarana fisik maupun jaringan internet yang baik di UMB
    "#h1.harapan175", "#k4.kepuasan175", # 3. Kegiatan akademik berjalan kondusif di UMB.
    "#h1.harapan176", "#k4.kepuasan176", # 4. Kegiatan ilmiah dan pengabdian kepada masyarakat diselenggarakan secara rutin di UMB (mis: bakti sosial dan seminar) melibatkan mahasiswa di UMB
    "#h1.harapan177", "#k4.kepuasan177", # 5. Pelayanan tenaga kependidikan yang baik di UMB.
    "#h1.harapan184", "#k4.kepuasan184", # 6. Sistem perkuliahan online cepat dan mudah diakses
    "#h1.harapan185", "#k4.kepuasan185", # 7. Dosen menginformasikan tata tertib perkuliahan dan memberikan kecukupan bahan/materi pembelajaran di kelas
    "#h1.harapan258", "#k4.kepuasan258", # 8. Informasi, sarana dan prasarana dalam menunjang kegiatan yang sesuai dengan uraian jabatan serta tugas pokok dan fungsi didapatkan dengan mudah
    "#h1.harapan186", "#k4.kepuasan186", # 9. Ketersediaan ruang kelas dan fasilitasnya seperti komputer, internet, mic, AC, Spidol, dan projector yang berfungsi dengan baik.
    "#h1.harapan180", "#k4.kepuasan180", # 10. Dosen bersedia membantu mahasiswa dalam memecahkan masalah dan menanggapi pertanyaan serta komentar mahasiswa.
    "#h1.harapan254", "#k4.kepuasan254", # 11. Ketersediaan prosedur layanan dalam menunjang tugas pokok dan fungsi, administrasi dan layanan kebutuhan informasi secara online dan offline dengan jelas dan handal
    "#h1.harapan257", "#k4.kepuasan257", # 12. Layanan manajemen di UMB dilakukan dengan prima (professional) sesuai dengan prosedur
    "#h1.harapan183", "#k4.kepuasan183", # 13. Dosen secara konsisten memberikan materi dan penilaian secara terbuka serta terencana
    "#h1.harapan256", "#k4.kepuasan256", # 14. Pimpinan dan atau penanggung jawab yang berwenang menguasai dan transparan dalam menunjang keterlaksanaan tugas pokok dan fungsi
    "#h1.harapan182", "#k4.kepuasan182", # 15. Dosen peduli dan memotivasi mahasiswa untuk melakukan yang terbaik.
    "#h1.harapan181", "#k4.kepuasan181", # 16. Dosen menguasai materi yang diberikan serta bersifat adil dan tidak memihak dalam memberikan penilaian.
    "#h1.harapan255", "#k4.kepuasan255", # 17. Dalam pelaksanaan setiap tugas pokok dan fungsi, senantiasa mendapatkan bimbingan dan arahan manajemen dengan cepat dan tanggap terhadap permasalahan
    "#h1.harapan233", "#k4.kepuasan233", # 18. Layanan sarana dan pra-sarana menyiapkan ruang kelas yang baik dan menyiapkan sistem pendingin (AC) di semua kelas sehingga memberikan kenyamanan dalam proses belajar mengajar
    "#h1.harapan232", "#k4.kepuasan232", # 19. Layanan sarana dan pra-sarana menyiapkan ruang kelas dengan pencahayaan dan menyiapkan fasilitas audio visual serta teknologi informasi yang baik
    "#h1.harapan234", "#k4.kepuasan234", # 20. Layanan sarana dan pra-sarana menyiapkan ruang toilet bersih dan nyaman, tempat untuk beribadah, parkir yang tersedia, serta kantin yang bersih, rapi dan nyaman
    "#h1.harapan236", "#k4.kepuasan236", # 21. Staf layanan sarana dan prasarana memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan235", "#k4.kepuasan235", # 22. Layanan sarana dan prasarana memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan238", "#k4.kepuasan238", # 23. Staf layanan sarana dan prasarana memiliki sikap sopan, santun, dan ramah
    "#h1.harapan237", "#k4.kepuasan237", # 24. Staf layanan sarana dan prasarana menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan226", "#k4.kepuasan226", # 25. Perpustakaan sudah memenuhi ketersediaan buku wajib dan referensi yang digunakan dalam proses belajar mengajar
    "#h1.harapan223", "#k4.kepuasan223", # 26. Staf perpustakaan memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan222", "#k4.kepuasan222", # 27. Perpustakaan memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan225", "#k4.kepuasan225", # 28. Staf perpustakaan memiliki sikap sopan, santun, dan ramah
    "#h1.harapan224", "#k4.kepuasan224", # 29. Staf perpustakaan menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan253", "#k4.kepuasan253", # 30. Layanan penerimaan mahasiswa tersedia sarana dan prasarana yang baik serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan250", "#k4.kepuasan250", # 31. Staf layanan penerimaan mahasiswa memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan249", "#k4.kepuasan249", # 32. Prosedur dan sistem informasi layanan penerimaan mahasiswa jelas dan handal
    "#h1.harapan252", "#k4.kepuasan252", # 33. Staf layanan penerimaan mahasiswa memiliki sikap sopan, santun, dan ramah
    "#h1.harapan251", "#k4.kepuasan251", # 34. Staf layanan penerimaan mahasiswa menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan201", "#k4.kepuasan201", # 35. Layanan penalaran, minat dan bakat tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan.
    "#h1.harapan198", "#k4.kepuasan198", # 36. Staf layanan penalaran, minat dan bakat memberikan pelayanan dengan cepat dan tanggap.
    "#h1.harapan197", "#k4.kepuasan197", # 37. Informasi dan prosedur layanan pengembangan minat dan bakat mahasiswa jelas dan mudah dipahami.
    "#h1.harapan200", "#k4.kepuasan200", # 38. Staf layanan penalaran, minat dan bakat berperilaku sopan, santun, dan ramah.
    "#h1.harapan199", "#k4.kepuasan199", # 39. Staf layanan penalaran, minat dan bakat menguasai dan transparan dalam memberikan pelayanan.
    "#h1.harapan248", "#k4.kepuasan248", # 40. Layanan Lembaga Sertifikasi Profesi tersedia kelengkapan sarana dan prasarana yang baik serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan245", "#k4.kepuasan245", # 41. Staf Layanan Lembaga Sertifikasi Profesi memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan244", "#k4.kepuasan244", # 42. Prosedur dan sistem informasi Layanan Lembaga Sertifikasi Profesi jelas dan handal
    "#h1.harapan247", "#k4.kepuasan247", # 43. Staf Layanan Lembaga Sertifikasi Profesi memiliki sikap sopan, santun, dan ramah
    "#h1.harapan246", "#k4.kepuasan246", # 44. Staf Layanan Lembaga Sertifikasi Profesi menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan191", "#k4.kepuasan191", # 45. Layanan kewirausahaan tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan.
    "#h1.harapan188", "#k4.kepuasan188", # 46. Staf layanan kewirausahaan memberikan pelayanan dengan cepat dan tanggap.
    "#h1.harapan187", "#k4.kepuasan187", # 47. Prosedur dan sistem informasi layanan kewirausahaan mahasiswa jelas dan handal dipahami.
    "#h1.harapan190", "#k4.kepuasan190", # 48. Staf layanan kewirausahaan berperilaku sopan, santun, dan ramah.
    "#h1.harapan189", "#k4.kepuasan189", # 49. Staf layanan kewirausahaan menguasai dan transparan dalam memberikan pelayanan.
    "#h1.harapan216", "#k4.kepuasan216", # 50. Petugas tenaga kesehatan berperilaku sopan, santun, dan ramah
    "#h1.harapan213", "#k4.kepuasan213", # 51. Penanganan layanan kesehatan dilakukan oleh tenaga medis (dokter) yang handal
    "#h1.harapan212", "#k4.kepuasan212", # 52. Layanan kesehatan tersedia dan tersosialisasi dengan baik
    "#h1.harapan215", "#k4.kepuasan215", # 53. Petugas tenaga kesehatan selalu siaga pada jam operasional
    "#h1.harapan214", "#k4.kepuasan214", # 54. Informasi dan prosedur layanan kesehatan jelas dan mudah dipahami
    "#h1.harapan221", "#k4.kepuasan221", # 55. Layanan bimbingan karir tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan218", "#k4.kepuasan218", # 56. Staf layanan bimbingan karir memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan217", "#k4.kepuasan217", # 57. Prosedur dan sistem informasi layanan bimbingan karir jelas dan mudah dipahami
    "#h1.harapan220", "#k4.kepuasan220", # 58. Staf layanan bimbingan karir berperilaku sopan, santun, dan ramah	
    "#h1.harapan219", "#k4.kepuasan219", # 59. Staf layanan bimbingan karir menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan206", "#k4.kepuasan206", # 60. Tenaga ahli bimbingan konseling berperilaku sopan, santun, dan ramah
    "#h1.harapan203", "#k4.kepuasan203", # 61. Penanganan layanan bimbingan dan konseling ditangani oleh tenaga ahli sesuai dengan permasalahan anda
    "#h1.harapan202", "#k4.kepuasan202", # 62. Layanan bimbingan dan konseling tersedia dan tersosialisasi dengan baik
    "#h1.harapan205", "#k4.kepuasan205", # 63. Tenaga ahli bimbingan konseling memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan204", "#k4.kepuasan204", # 64. Informasi dan prosedur layanan bimbingan konseling jelas dan mudah dipahami
    "#h1.harapan211", "#k4.kepuasan211", # 65. Staf layanan beasiswa berperilaku sopan, santun, dan ramah
    "#h1.harapan208", "#k4.kepuasan208", # 66. Seleksi beasiswa dilakukan secara transparan
    "#h1.harapan207", "#k4.kepuasan207", # 67. Layanan beasiswa tersedia dan tersosialisasi dengan baik
    "#h1.harapan210", "#k4.kepuasan210", # 68. Staf layanan beasiswa memberikan pelayanan dengan cepat dan tanggap terhadap keluhan	
    "#h1.harapan209", "#k4.kepuasan209", # 69. Informasi dan prosedur layanan beasiswa jelas dan mudah dipahami
    "#h1.harapan243", "#k4.kepuasan243", # 70. Bagian keuangan tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan240", "#k4.kepuasan240", # 71. Staf bagian keuangan memberikan pelayanan dengan cepat dan tanggap terhadap keluhan
    "#h1.harapan239", "#k4.kepuasan239", # 72. Prosedur dan sistem informasi bagian keuangan bekerja dengan jelas dan handal
    "#h1.harapan242", "#k4.kepuasan242", # 73. Staf bagian keuangan memiliki sikap sopan, santun, dan ramah
    "#h1.harapan241", "#k4.kepuasan241", # 74. Staf bagian keuangan menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan231", "#k4.kepuasan231", # 75. Administrasi Akademik tersedia kelengkapan sarana dan prasarana serta saluran pengaduan terkait layanan
    "#h1.harapan228", "#k4.kepuasan228", # 76. Staf administrasi akademik memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan227", "#k4.kepuasan227", # 77. Prosedur dan sistem informasi administrasi akademik jelas dan mudah
    "#h1.harapan230", "#k4.kepuasan230", # 78. Staf administrasi Administrasi memiliki sikap sopan, santun, dan ramah
    "#h1.harapan229", "#k4.kepuasan229"  # 79. Staf administrasi akademik menguasai dan transparan dalam memberikan pelayanan
] # CUSTOMIZE YOUR SURVEY ANSWERS WITH THE TABLE ABOVE VARIABLE CHECKBOXES


# ========= ADVICE FOR THE CAMPUS ========= #
advice1 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice2 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice3 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice4 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice5 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice6 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice7 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice8 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice9 = "GANTI DAN SESUAIKAN DENGAN SARAN ANDA DISINI" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS


# ========= SCROLL BAR MOVING DISTANCE ========= #
auto_scroll = "window.scrollBy(0, 30);"


# ========= SUCCESS AND FAILED MESSAGE ========= #
success = "All checkboxes processed successfully."
failed = "Some checkboxes could not be clicked."


# ========= URL & TARGET ========= #
sia = "http://sia.mercubuana.ac.id"
survey = "https://survey-bkp.mercubuana.ac.id"
target_username = "username"
target_password = "password"
login = '/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/input'
sign_in = '/html/body/div/div[2]/div[2]/form/div[3]/div[2]/button'


# ========= FUNCTION FOR SURVEY PROCESS ========= #
def proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed):
    all_clicked = True  # Flag to check if all checkboxes are clicked

    for checkbox in checkboxes:
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


# --------------------------------- MAIN PROGRAM --------------------------------- #

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

# Student Survey button
student_survey__button = driver.find_element(
    By.XPATH,
    "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[4]/a"
)
student_survey__button.click()
time.sleep(delay)

# --------------- FIRST COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul1)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice1, delay, success, failed)

# --------------- SECOND COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul2)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice2, delay, success, failed)

# --------------- THIRD COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul3)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice3, delay, success, failed)

# --------------- FOURTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul4)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice4, delay, success, failed)

# --------------- FIFTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul5)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice5, delay, success, failed)

# --------------- SIXTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul6)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice6, delay, success, failed)

# --------------- SEVENTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul7)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice7, delay, success, failed)

# --------------- EIGHTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul8)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice8, delay, success, failed)

# --------------- NINTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul9)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice9, delay, success, failed)


# ========= Open SIA again to view KHS ========= #
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
pop_up_button = driver.find_element(
    By.XPATH, 
    "/html/body/div[6]/div[1]/button"
)
pop_up_button.click()
time.sleep(delay)

# Click the Student Details button
detail_student_button = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/form/div/div[1]/div/table/tbody/tr/td[2]/div/ul/li[2]/a",
)
detail_student_button.click()
time.sleep(delay)

# Click the View KHS button
khs_button = driver.find_element(
    By.XPATH,
    '//*[@id="khs_lst"]/a'
)
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

# Click the View KHS button
view_khs = driver.find_element(By.XPATH, view_khs)
view_khs.click()

# Leaving the browser open for 1 hour
time.sleep(3600)