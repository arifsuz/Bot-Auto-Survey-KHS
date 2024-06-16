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

# ========= DELAY TIME ========== #
delay = 0.5 #CUSTOMIZE THE DELAY TIME OF EACH PROCESS YOU WANT.

# ========= SURVEY ANSWERS ========= #

# ('TABLE FOR EXPECTATION SURVEY ANSWERS')   ('TABLE FOR SATISFACTION SURVEY ANSWERS')
#   "#h1.harapan" = Sangat Penting           "#k1.kepuasan" = Sangat Puas
#   "#h2.harapan" = Penting                  "#k2.kepuasan" = Puas
#   "#h3.harapan" = Cukup Penting            "#k3.kepuasan" = Cukup Puas
#   "#h4.harapan" = Ttdak Penting            "#k4.kepuasan" = Tidak Puas

checkboxes = [
    "#h1.harapan178", "#k1.kepuasan178", # Keberagaman suku, agama, ras, gender, dan disabilitas yang harmoni di UMB.
    "#h1.harapan179", "#k1.kepuasan179", # Sarana dan prasarana fisik maupun jaringan internet yang baik di UMB
    "#h1.harapan175", "#k1.kepuasan175", # Kegiatan akademik berjalan kondusif di UMB.
    "#h1.harapan176", "#k1.kepuasan176", # Kegiatan ilmiah dan pengabdian kepada masyarakat diselenggarakan secara rutin di UMB (mis: bakti sosial dan seminar) melibatkan mahasiswa di UMB
    "#h1.harapan177", "#k1.kepuasan177", # Pelayanan tenaga kependidikan yang baik di UMB.
    "#h1.harapan184", "#k1.kepuasan184", # Sistem perkuliahan online cepat dan mudah diakses
    "#h1.harapan185", "#k1.kepuasan185", # Dosen menginformasikan tata tertib perkuliahan dan memberikan kecukupan bahan/materi pembelajaran di kelas
    "#h1.harapan186", "#k1.kepuasan186", # Informasi, sarana dan prasarana dalam menunjang kegiatan yang sesuai dengan uraian jabatan serta tugas pokok dan fungsi didapatkan dengan mudah
    "#h1.harapan180", "#k1.kepuasan180", # Ketersediaan ruang kelas dan fasilitasnya seperti komputer, internet, mic, AC, Spidol, dan projector yang berfungsi dengan baik.
    "#h1.harapan258", "#k1.kepuasan258", # Dosen bersedia membantu mahasiswa dalam memecahkan masalah dan menanggapi pertanyaan serta komentar mahasiswa.
    "#h1.harapan254", "#k1.kepuasan254", # Ketersediaan prosedur layanan dalam menunjang tugas pokok dan fungsi, administrasi dan layanan kebutuhan informasi secara online dan offline dengan jelas dan handal
    "#h1.harapan257", "#k1.kepuasan257", # Layanan manajemen di UMB dilakukan dengan prima (professional) sesuai dengan prosedur
    "#h1.harapan183", "#k1.kepuasan183", # Dosen secara konsisten memberikan materi dan penilaian secara terbuka serta terencana
    "#h1.harapan256", "#k1.kepuasan256", # Pimpinan dan atau penanggung jawab yang berwenang menguasai dan transparan dalam menunjang keterlaksanaan tugas pokok dan fungsi
    "#h1.harapan182", "#k1.kepuasan182", # Dosen peduli dan memotivasi mahasiswa untuk melakukan yang terbaik.
    "#h1.harapan181", "#k1.kepuasan181", # Dosen menguasai materi yang diberikan serta bersifat adil dan tidak memihak dalam memberikan penilaian.
    "#h1.harapan255", "#k1.kepuasan255", # Dalam pelaksanaan setiap tugas pokok dan fungsi, senantiasa mendapatkan bimbingan dan arahan manajemen dengan cepat dan tanggap terhadap permasalahan
    "#h1.harapan233", "#k1.kepuasan233", # Layanan sarana dan pra-sarana menyiapkan ruang kelas yang baik dan menyiapkan sistem pendingin (AC) di semua kelas sehingga memberikan kenyamanan dalam proses belajar mengajar
    "#h1.harapan232", "#k1.kepuasan232", # Layanan sarana dan pra-sarana menyiapkan ruang kelas dengan pencahayaan dan menyiapkan fasilitas audio visual serta teknologi informasi yang baik
    "#h1.harapan234", "#k1.kepuasan234", # Layanan sarana dan pra-sarana menyiapkan ruang toilet bersih dan nyaman, tempat untuk beribadah, parkir yang tersedia, serta kantin yang bersih, rapi dan nyaman
    "#h1.harapan236", "#k1.kepuasan236", # Staf layanan sarana dan prasarana memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan235", "#k1.kepuasan235", # Layanan sarana dan prasarana memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan238", "#k1.kepuasan238", # Staf layanan sarana dan prasarana memiliki sikap sopan, santun, dan ramah
    "#h1.harapan237", "#k1.kepuasan237", # Staf layanan sarana dan prasarana menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan226", "#k1.kepuasan226", # Perpustakaan sudah memenuhi ketersediaan buku wajib dan referensi yang digunakan dalam proses belajar mengajar
    "#h1.harapan223", "#k1.kepuasan223", # Staf perpustakaan memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan222", "#k1.kepuasan222", # Perpustakaan memiliki prosedur pelayanan yang jelas dan mudah
    "#h1.harapan225", "#k1.kepuasan225", # Staf perpustakaan memiliki sikap sopan, santun, dan ramah
    "#h1.harapan224", "#k1.kepuasan224", # Staf perpustakaan menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan253", "#k1.kepuasan253", # Layanan penerimaan mahasiswa tersedia sarana dan prasarana yang baik serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan250", "#k1.kepuasan250", # Staf layanan penerimaan mahasiswa memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan249", "#k1.kepuasan249", # Prosedur dan sistem informasi layanan penerimaan mahasiswa jelas dan handal
    "#h1.harapan252", "#k1.kepuasan252", # Staf layanan penerimaan mahasiswa memiliki sikap sopan, santun, dan ramah
    "#h1.harapan251", "#k1.kepuasan251", # Staf layanan penerimaan mahasiswa menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan201", "#k1.kepuasan201", # Layanan penalaran, minat dan bakat tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan.
    "#h1.harapan198", "#k1.kepuasan198", # Staf layanan penalaran, minat dan bakat memberikan pelayanan dengan cepat dan tanggap.
    "#h1.harapan197", "#k1.kepuasan197", # Informasi dan prosedur layanan pengembangan minat dan bakat mahasiswa jelas dan mudah dipahami.
    "#h1.harapan200", "#k1.kepuasan200", # Staf layanan penalaran, minat dan bakat berperilaku sopan, santun, dan ramah.
    "#h1.harapan199", "#k1.kepuasan199", # Staf layanan penalaran, minat dan bakat menguasai dan transparan dalam memberikan pelayanan.
    "#h1.harapan248", "#k1.kepuasan248", # Layanan Lembaga Sertifikasi Profesi tersedia kelengkapan sarana dan prasarana yang baik serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan245", "#k1.kepuasan245", # Staf Layanan Lembaga Sertifikasi Profesi memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan244", "#k1.kepuasan244", # Prosedur dan sistem informasi Layanan Lembaga Sertifikasi Profesi jelas dan handal
    "#h1.harapan247", "#k1.kepuasan247", # Staf Layanan Lembaga Sertifikasi Profesi memiliki sikap sopan, santun, dan ramah
    "#h1.harapan246", "#k1.kepuasan246", # Staf Layanan Lembaga Sertifikasi Profesi menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan191", "#k1.kepuasan191", # Layanan kewirausahaan tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan.
    "#h1.harapan188", "#k1.kepuasan188", # Staf layanan kewirausahaan memberikan pelayanan dengan cepat dan tanggap.
    "#h1.harapan187", "#k1.kepuasan187", # Prosedur dan sistem informasi layanan kewirausahaan mahasiswa jelas dan handal dipahami.
    "#h1.harapan190", "#k1.kepuasan190", # Staf layanan kewirausahaan berperilaku sopan, santun, dan ramah.
    "#h1.harapan189", "#k1.kepuasan189", # Staf layanan kewirausahaan menguasai dan transparan dalam memberikan pelayanan.
    "#h1.harapan216", "#k1.kepuasan216", # Petugas tenaga kesehatan berperilaku sopan, santun, dan ramah
    "#h1.harapan213", "#k1.kepuasan213", # Penanganan layanan kesehatan dilakukan oleh tenaga medis (dokter) yang handal
    "#h1.harapan212", "#k1.kepuasan212", # Layanan kesehatan tersedia dan tersosialisasi dengan baik
    "#h1.harapan215", "#k1.kepuasan215", # Petugas tenaga kesehatan selalu siaga pada jam operasional
    "#h1.harapan214", "#k1.kepuasan214", # Informasi dan prosedur layanan kesehatan jelas dan mudah dipahami
    "#h1.harapan221", "#k1.kepuasan221", # Layanan bimbingan karir tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan218", "#k1.kepuasan218", # Staf layanan bimbingan karir memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan217", "#k1.kepuasan217", # Prosedur dan sistem informasi layanan bimbingan karir jelas dan mudah dipahami
    "#h1.harapan220", "#k1.kepuasan220", # Staf layanan bimbingan karir berperilaku sopan, santun, dan ramah	
    "#h1.harapan219", "#k1.kepuasan219", # Staf layanan bimbingan karir menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan206", "#k1.kepuasan206", # Tenaga ahli bimbingan konseling berperilaku sopan, santun, dan ramah
    "#h1.harapan203", "#k1.kepuasan203", # Penanganan layanan bimbingan dan konseling ditangani oleh tenaga ahli sesuai dengan permasalahan anda
    "#h1.harapan202", "#k1.kepuasan202", # Layanan bimbingan dan konseling tersedia dan tersosialisasi dengan baik
    "#h1.harapan205", "#k1.kepuasan205", # Tenaga ahli bimbingan konseling memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan204", "#k1.kepuasan204", # Informasi dan prosedur layanan bimbingan konseling jelas dan mudah dipahami
    "#h1.harapan211", "#k1.kepuasan211", # Staf layanan beasiswa berperilaku sopan, santun, dan ramah
    "#h1.harapan208", "#k1.kepuasan208", # Seleksi beasiswa dilakukan secara transparan
    "#h1.harapan207", "#k1.kepuasan207", # Layanan beasiswa tersedia dan tersosialisasi dengan baik
    "#h1.harapan210", "#k1.kepuasan210", # Staf layanan beasiswa memberikan pelayanan dengan cepat dan tanggap terhadap keluhan	
    "#h1.harapan209", "#k1.kepuasan209", # Informasi dan prosedur layanan beasiswa jelas dan mudah dipahami
    "#h1.harapan243", "#k1.kepuasan243", # Bagian keuangan tersedia kelengkapan sarana dan prasarana serta tersedia saluran pengaduan terkait layanan
    "#h1.harapan240", "#k1.kepuasan240", # Staf bagian keuangan memberikan pelayanan dengan cepat dan tanggap terhadap keluhan
    "#h1.harapan239", "#k1.kepuasan239", # Prosedur dan sistem informasi bagian keuangan bekerja dengan jelas dan handal
    "#h1.harapan242", "#k1.kepuasan242", # Staf bagian keuangan memiliki sikap sopan, santun, dan ramah
    "#h1.harapan241", "#k1.kepuasan241", # Staf bagian keuangan menguasai dan transparan dalam memberikan pelayanan
    "#h1.harapan231", "#k1.kepuasan231", # Administrasi Akademik tersedia kelengkapan sarana dan prasarana serta saluran pengaduan terkait layanan
    "#h1.harapan228", "#k1.kepuasan228", # Staf administrasi akademik memberikan pelayanan dengan cepat dan tanggap
    "#h1.harapan227", "#k1.kepuasan227", # Prosedur dan sistem informasi administrasi akademik jelas dan mudah
    "#h1.harapan230", "#k1.kepuasan230", # Staf administrasi Administrasi memiliki sikap sopan, santun, dan ramah
    "#h1.harapan229", "#k1.kepuasan229"  # Staf administrasi akademik menguasai dan transparan dalam memberikan pelayanan
] # CUSTOMIZE YOUR SURVEY ANSWERS WITH THE TABLE ABOVE VARIABLE CHECKBOXES

advice = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS

# --------------------------------- MAIN PROGRAM --------------------------------- #

# Inisialisasi driver Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Mengakses URL
driver.get("http://sia.mercubuana.ac.id")
time.sleep(delay)

# Enter Username SIA Mercubuana
username_sia = driver.find_element(By.NAME, "username")
username_sia.send_keys(username)
time.sleep(delay)

# Enter Password SIA Mercubuana
password_sia = driver.find_element(By.NAME, "password")
password_sia.send_keys(password)
time.sleep(delay)

# login button
login_button = driver.find_element(
    By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/input"
)
login_button.click()
time.sleep(delay)

# Closing the Pop Up
pop_up_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/button")
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
khs_button = driver.find_element(By.XPATH, '//*[@id="khs_lst"]/a')
khs_button.click()
time.sleep(delay)

# Finding the dropdown
dropdown = Select(driver.find_element(By.XPATH, '//*[@id="periode"]'))
time.sleep(delay)

# Choose an option for even 2023 (Semester 2)
dropdown.select_by_visible_text("Genap 2023")
time.sleep(delay)

# Login button to fill out the survey
survey_button = driver.find_element(
    By.XPATH,
    '//*[@id="main_form"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[4]/center/font/a',
)
survey_button.click()
time.sleep(delay)

# Enter Username Survey BKP Mercubuana
username_survey = driver.find_element(By.NAME, "username")
username_survey.send_keys(username)
time.sleep(delay)

# Enter Pssword Survey BKP Mercubuana
password_survey = driver.find_element(By.NAME, "password")
password_survey.send_keys(password)
time.sleep(delay)

# Sing In button
sign_in__button = driver.find_element(
    By.XPATH, "/html/body/div/div[2]/div[2]/form/div[3]/div[2]/button"
)
sign_in__button.click()
time.sleep(delay)

# Student Survey button
student_survey__button = driver.find_element(
    By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[4]/a"
)
student_survey__button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(
    By.XPATH, '//*[@id="questionsdosentbl"]/tbody/tr[1]/td[4]/a'
)
survey__button.click()
time.sleep(delay)

all_clicked = True  # Flag to check if all checkboxes are clicked

for checkbox in checkboxes:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, checkbox))
        )
        ActionChains(driver).move_to_element(element).perform()
        element.click()
        
        # Auto scroll
        driver.execute_script("window.scrollBy(0, 30);")
        
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
saran.send_keys(advice)
time.sleep(delay)

# Submit Survey
sumbit_survey = driver.find_element(
    By.NAME,
    "save-answer"
)
sumbit_survey.click()
time.sleep(delay)

# Closing the browser
driver.quit()