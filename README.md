> **Note from the Developer:** 
> "بصراحة مكنش في وقت وكنت عايز أنام جداً، فكتبت الـ README دي بمساعدة الـ AI عشان تطلع منظمة ومظبوطة تلحق التقييم!" 😴✨

---

# Library Management Analysis Project

## 📌 Project Overview
This project focuses on analyzing a local library's dataset containing information about books, members, and borrowing records. Using **Pandas** and **NumPy**, the analysis uncovers insights to improve library services, understand borrowing frequencies, evaluate membership behavior, and optimize inventory management.

## 📊 Dataset Structure
The project utilizes three interrelated datasets located in the root directory:
* `books.csv`: Contains details about book titles, authors, genres, publication years, and inventory copies.
* `members.csv`: Includes information about library members, registration dates, and membership categories.
* `borrowings.csv`: Records transaction logs of which member borrowed which book, along with loan and return dates.

## 🛠️ Requirements & Technical Tasks Implemented
1.  **Data Exploration:** Initial schema evaluation using Pandas (`.info()`, `.head()`).
2.  **Probability Calculations:**
    * Probability of randomly selecting a borrowed book from a specific genre (*Science Fiction*).
    * Probability of selecting a specific membership type (*Student*).
    * Joint probability satisfying multiple complex conditions (Year *2025* AND language *English*).
3.  **Pandas Data Analysis:**
    * Identified highest and lowest borrowed genres.
    * Determined most active borrowing members and popular authors.
    * Analyzed publication year distributions and monthly transactional trends.
    * Isolated stale inventory (books never borrowed).
    * Computed average loan periods broken down by genre.
4.  **NumPy Performance Vectorization:**
    * Converted Pandas Series into efficient numerical NumPy arrays.
    * Identified range bounds (`min`/`max`) for book page configurations.
    * Leveraged Boolean indexing masks for subset filtering.
    * Applied fast vectorized scaling operators to evaluate loan metrics in hours.

## 🚀 How to Run the Project
1. Clone this repository:
   ```bash
   git clone [https://github.com/1saif-web/IEEE-pandas-NumPy-task.git](https://github.com/1saif-web/IEEE-pandas-NumPy-task.git)
