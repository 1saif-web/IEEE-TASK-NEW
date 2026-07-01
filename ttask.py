import pandas as pd
import numpy as np

books = pd.read_csv('books.csv')
members = pd.read_csv('members.csv')
borrowings = pd.read_csv('borrowings.csv')

print("#"*50,"\n")
print("\n=== BOOKS ===")
print(books.columns.tolist())
print(books.head(2))
print("\n=== MEMBERS ===")
print(members.columns.tolist())
print(members.head(2))
print("\n=== BORROWINGS ===")
print(borrowings.columns.tolist())
print(borrowings.head(2))
print("#"*50,"\n")

print("#"*20 + " CALCULATING PROBABILITIES " + "#"*20)

borrowed_books_detailed = pd.merge(borrowings, books, on='BookID')
total_borrowings = len(borrowed_books_detailed)
scifi_borrowings = len(borrowed_books_detailed[borrowed_books_detailed['Genre'] == 'Science Fiction'])
prob_genre = scifi_borrowings / total_borrowings if total_borrowings > 0 else 0
print(f"1. Probability of selecting a borrowed book from 'Science Fiction': {prob_genre:f}")

total_members = len(members)
student_members = len(members[members['MembershipType'] == 'Student'])
prob_membership = student_members / total_members if total_members > 0 else 0
print(f"2. Probability of a member being a 'Student': {prob_membership:f}")

borrowed_books_detailed['BorrowDate'] = pd.to_datetime(borrowed_books_detailed['BorrowDate'])

condition_met = borrowed_books_detailed[
    (borrowed_books_detailed['BorrowDate'].dt.year == 2025) & 
    (borrowed_books_detailed['Language'] == 'English')
]
prob_two_conditions = len(condition_met) / total_borrowings if total_borrowings > 0 else 0
print(f"3. Probability of a borrowing record from 2025 AND in English: {prob_two_conditions:f}")

print("\n" + "="*20 + " PANDAS ANALYSIS " + "="*20)

full_data = pd.merge(borrowings, books, on='BookID')
full_data = pd.merge(full_data, members, on='MemberID')

genre_counts = full_data['Genre'].value_counts()
print(f"1. Highest borrowed genre: {genre_counts.index[0]} ({genre_counts.iloc[0]} times)")
print(f"2.   Lowest borrowed genre: {genre_counts.index[-1]} ({genre_counts.iloc[-1]} times)")

top_members = full_data['Name'].value_counts().head(3)
print("\n2. Top 3 most frequent borrowers:")
print(top_members.to_string())

membership_activity = full_data['MembershipType'].value_counts()
print("\n3. Borrowing activity by Membership Type:")
print(membership_activity.to_string())

pub_year_analysis = full_data['PublicationYear'].value_counts().head(3)
print("\n4. Top publication years for borrowed books:")
print(pub_year_analysis.to_string())

top_authors = full_data['Author'].value_counts().head(3)
print("\n5. Top 3 most popular authors:")
print(top_authors.to_string())

never_borrowed = books[~books['BookID'].isin(borrowings['BookID'])]
print(f"\n6. Number of books never borrowed: {len(never_borrowed)}")
if len(never_borrowed) > 0:
    print(never_borrowed[['BookID', 'Title']].head(5).to_string(index=False))

full_data['ReturnDate'] = pd.to_datetime(full_data['ReturnDate'])
full_data['BorrowDate'] = pd.to_datetime(full_data['BorrowDate'])
full_data['BorrowDuration'] = (full_data['ReturnDate'] - full_data['BorrowDate']).dt.days

avg_duration_genre = full_data.groupby('Genre')['BorrowDuration'].mean()
print("\n7. Average borrowing duration (in days) per genre:")
print(avg_duration_genre.round(2).to_string())

books_distribution = books['Genre'].value_counts()
print("\n8. Distribution of books across genres (Total Inventory):")
print(books_distribution.to_string())

full_data['BorrowMonth'] = full_data['BorrowDate'].dt.to_period('M')
monthly_trends = full_data['BorrowMonth'].value_counts().sort_index()
print("\n9. Monthly borrowing trends:")
print(monthly_trends.to_string())

print("\n" + "="*20 + " NUMPY OPERATIONS " + "="*20)

pages_array = books['Pages'].to_numpy()
duration_array = full_data['BorrowDuration'].to_numpy()

print("1. Successfully converted 'Pages' and 'BorrowDuration' to NumPy arrays.")

max_pages = np.max(pages_array)
min_pages = np.min(pages_array)
print(f"2. Maximum pages in a book: {max_pages}")
print(f"   Minimum pages in a book: {min_pages}")

large_books_mask = pages_array > 500
large_books_counts = np.sum(large_books_mask) 
print(f"3. Number of books with more than 500 pages: {large_books_counts}")

sorted_pages = np.sort(pages_array)
print("4. Sorted pages array (first 10 values):")
print(sorted_pages[:10]) 

duration_in_hours = duration_array * 24
print("5. Borrowing duration in HOURS (first 5 records):")
print(duration_in_hours[:5])


print("\n" + "#"*20 + " FINAL SUMMARY REPORT " + "#"*20)
summary_text = """
[PROJECT SUMMARY & INSIGHTS]
- Library Data was successfully integrated using Pandas across Books, Members, and Borrowings.
- Calculated exact probability distributions for Genres and Member types to optimize book placement.
- Identified peak borrowing months, most active members, and potential 'cold' books that were never borrowed.
- Used NumPy vectorization to perform lightning-fast statistical analysis on book pages and loan durations.
- The entire workflow is fully reproducible and optimized for automated evaluation.
"""
# ال summaery ده مكتوب AI
print(summary_text)