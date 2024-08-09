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
# ========= SSO MERCUBUANA ACCOUNT ========= #
username = "41523010XXX" # REPLACE WITH STUDENT IDENTIFICATION NUMBER (NIM)
password = "123456789"  # REPLACE WITH YOUR SIA PASSWORD
# ========================================== #
```

2. You can adjust the number of credits taken by adjusting how many courses there are in the current semester with the example below.
```
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
```
The code above declares 9 variables for courses, if the courses you take are less than 9 you can delete the unused variables. And you need to delete the program that is in `MAIN PROGRAM` which has the title COURSE ORDER and adjust with jhapus accordingly.
```
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
# ===================================================================================  #


# =================================== NINTH COURSE ===================================  #
survey_course_button = driver.find_element(By.XPATH, course)
survey_course_button.click()
time.sleep(delay)

# Click the Fill out Survey button
survey__button = driver.find_element(By.XPATH, course9)
survey__button.click()
time.sleep(delay)
# Run the survey process by calling the survey process function
proses_survey(driver, course_checkboxes, auto_scroll, advice9, delay, success, failed)
# ===================================================================================  #
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
```
```
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
# ============================================================================================================= #
```
Make sure you have adjusted each of the questions above.

5. Adjust the advice you want to give in the suggestion pool provided by changing the value of the `advice` variable in the `main.py` program as in the code excerpt below
```
advice1 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice2 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice3 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice4 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice5 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice6 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice7 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice8 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
advice9 = "SARAN UNTUK KAMPUS MERCUBUANA: \n 1. Menambahkan fasilitas yang lebih baik \n 2. Memperbaiki sistem" # CUSTOMIZE YOUR ADVICE FOR THE CAMPUS
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