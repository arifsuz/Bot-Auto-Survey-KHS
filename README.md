# Bot-Auto-Survey-KHS
This repository contains tools for filling out surveys of courses and lecturers as well as facilities and services available at Universitas Mercu Buana. This tool specifically auto-completes surveys with commands that you can set, allowing users to specify their answers and making it easy and fast to use. This tool accommodates the answers to each section of the question according to the available answer options, Expectations, and Satisfaction, ensuring to shorten the time in answering all surveys by running the program once and having flexibility and accuracy in answering each question.

## Requirements
There are several conditions that must be met to be able to run this program including:

#### **1. [Visual Stiudio Code](https://code.visualstudio.com/download)**
There are many code editor options that you can run but I strongly recommend using the [Visual Stiudio Code](https://code.visualstudio.com/download), because the ecosystem is very good and supports programmers to write, create, manage, improve, and run a program or system from any part of a particular part in a technology used. Another reason is because [Visual Stiudio Code](https://code.visualstudio.com/download) has a very complex appearance and usability, and supports many existing tach stacks, as well as being able to provide many extensions that support and facilitate programmers.

#### **2. [Python](https://www.python.org/downloads/)**
Make sure you have installed [Python](https://www.python.org/downloads/) before, or if not you can install Python first on the official website (or you can click on the sub title above). If you have downloaded python.exe run it to perform the installation process which you can follow through the information provided. The important thing to note in installing [Python](https://www.python.org/downloads/) is to pay attention to the version because to be able to run a certain program you must use a certain version of [Python](https://www.python.org/downloads/) to be able to run the program, in this case I suggest the most recent version or at least Python 3.12 and adjust it for the operating system version you are using.

## Installation
#### **1. [Bot-Auto-Survey-KHS](https://github.com/arifsuz/Bot-Auto-Survey-KHS)**
You can download this repository in zip form and you can extract it first to open and run the program, but I strongly recommend that you just clone it to make your work easier and faster.
- Copy this command `git clone https://github.com/arifsuz/Bot-Auto-Survey-KHS.git`.
- Paste it into the command prompt or terminal and make sure the directory where you save the project is the way you want it.
- After you paste it, press the enter button to run the cloning process.
- Then open the directory with the command `cd Bot-Auto-Survey-KHS`.

#### **2. [Selenium WebDriver](https://pypi.org/project/selenium/)**
If you are starting with desktop website or mobile website test automation, then you will be using the WebDriver API. WebDriver uses the browser automation API provided by the browser vendor to control the browser and run tests. It's as if the user is actually operating the browser. Since WebDriver does not require its API to be compiled with the application code, it is not intrusive. Therefore, you test the same application that you launch directly. WebDriver drives the browser natively, as the user does, either locally or on a remote machine using a Selenium server, marking a leap forward in terms of browser automation. Selenium WebDriver refers to the language binding and code implementation of individual browser controllers. It is usually referred to simply as WebDriver. Important notes for installing : 
- Make sure you open the terminal in the directory you want or in a place that is in the same directory as this program.
- then run the `pip install Selenium` in the command line or 
- Make sure the Selenium library is installed correctly and successfully, if there are errors or problems you can visit the documentation website or can click the sub title above.

## Usage

1. Customize the code below with your SIA or SSO account.
```
# ========= SIA MERCUBUANA ACCOUNT ========= #
username = "41523010XXX" # REPLACE WITH STUDENT IDENTIFICATION NUMBER (NIM)
password = "123456789" # REPLACE WITH YOUR SIA PASSWORD
```

2. You can adjust the number of credits taken by adjusting how many courses there are in the current semester with the example below.
```
# ========= NUMBER OF COURSES TAKEN ========= #
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
```
The code above declares 9 variables for courses, if the courses you take are less than 9 you can delete the unused variables. And you need to delete the program that is in `MAIN PROGRAM` which has the title COURSE ORDER and adjust with jhapus accordingly.
```
# --------------- FIRST COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul1)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- SECOND COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul2)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- THIRD COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul3)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- FOURTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul4)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- FIFTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul5)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- SIXTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul6)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- SEVENTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul7)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- EIGHTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul8)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)

# --------------- NINTH COURSE --------------- #
# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, matkul9)
survey__button.click()
time.sleep(delay)

# Run the survey process by calling the survey process function
proses_survey(driver, checkboxes, auto_scroll, advice, delay, success, failed)
```

3. You can also set how long it takes to pause each process running in the program by setting the value of the `delay` variable which has a float value and you can change it to an integer as below.
```
# ========= DELAY TIME ========== #
delay = 0.3 #CUSTOMIZE THE DELAY TIME OF EACH PROCESS YOU WANT.
```
The time read by the program is in seconds so you can adjust it based on seconds.

4. Adjust the answers to fill out your survey by changing the `id` section or the symbol `#` in the data list or array of checkboxes below.
```
# ========= SURVEY ANSWERS ========= #
# ('TABLE FOR EXPECTATION SURVEY ANSWERS')   ('TABLE FOR SATISFACTION SURVEY ANSWERS')
#   "#h1.harapan" = Sangat Penting           "#k4.kepuasan" = Sangat Puas
#   "#h2.harapan" = Penting                  "#k3.kepuasan" = Puas
#   "#h3.harapan" = Cukup Penting            "#k2.kepuasan" = Cukup Puas
#   "#h4.harapan" = Ttdak Penting            "#k.kepuasan" = Tidak Puas
```
Above is information to adjust your answer and adjust it to the `id` of CCS SELECTOR as the target driver of this program, and you can change and readjust each of the answers in the checkboxes array below.
```
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
```
Make sure you have adjusted each of the questions above.

5. Adjust the advice you want to give in the suggestion pool provided by changing the value of the `advice` variable in the `main.py` program as in the code excerpt below
```
# ========= ADVICE FOR THE CAMPUS ========= #
advice = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
```
This suggestion will be sent to all courses, but if you want to make it different in each course then you can create a new variable and adjust it to the program to fill out the survey according to the course in `MAIN PROGRAM`

6. After the program has been adjusted to your needs, the next step is to run a program called `main.py`, namely by opening a terminal in Visual Studio Code by pressing the `Terminal>New Terminal` menu or you can use a shortcut on the keyboard by pressing the `CTRL key +SHIFT+`` simultaneously.

Then type `python main.py` in the terminal then press ENTER to run the program.


## Video Customize Guide
### 1. **Clone Repository**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/ed5b600c-eba3-4a84-8319-3b8ca17e0574

### 2. **Install Selenium**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/f05d31d2-2707-43b1-8df0-9df1ad0cf2e7

### 3. **Customizing SIA Accounts**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/2cb16290-4a7f-455c-acbf-4cb62e2722fb

### 4. **Customizing Courses**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/d0ea7321-f7ef-4676-ab2c-6da025d75695

### 5. **Set Time Delay**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/0daad78d-cacb-43fd-bd42-94c3d81612b5

### 6. **Customizing Survey Answarey**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/3a004d26-afcd-4790-835f-e506ac6becb8

### 7. **Customizing Advice Answarey**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/e8833de5-2b49-4388-ae49-eb567e42b12f

### 8. **Running Programs**

https://github.com/arifsuz/Bot-Auto-Survey-KHS/assets/149920438/08e27c3a-a8aa-497d-9183-1a28f94d5647

## Contributions

If you want to contribute to this project, you can follow these steps:

1. Fork this repository to your GitHub account.
2. Clone the forked repository to your local computer.
3. Move to the project directory with `cd <repo-name>`.
4. Create a new branch for the feature or fix you want to add with `git checkout -b <branch-name>`.
5. Make necessary changes to the code.
6. Commit your changes with a clear and descriptive message using `git commit -m "Description of changes"`.
7. Push the branch to your GitHub repository with `git push origin <branch-name>`.
8. Open the forked repository page on GitHub and create a new pull request.
9. Fill out the pull request description to clearly explain the changes you made.
10. Wait for feedback and discussion from the repository owner.

Make sure to follow the contribution rules and guidelines set by this project. This may include things like code of conduct, writing style, and code review process.

The pull request process involves proposing code changes to the main repository. Once a pull request is created, the repository owner will review your changes and decide whether or not to merge them into the main repository. Discussion and refinement may be required before the pull request can be accepted.

Be sure to understand and follow the pull request process established by this project. This may include steps such as code testing, peer code review, and documentation requirements.

Always communicate with the repository owner and project team to ensure that your contributions meet their needs and expectations.

## Authors
**Developed by :**
**Muhamad Nur Arif**
**(41523010147)**

### 🔗 Link
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://arifsuz.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arifsuz)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marif8/)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/arif_suz/)
