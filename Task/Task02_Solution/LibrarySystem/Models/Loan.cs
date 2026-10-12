using System;

namespace LibrarySystem.Models
{
    public class Loan
    {
        public int BookId { get; set; }
        public int BorrowerId { get; set; }
        public DateTime LoanDate { get; set; }
        public DateTime? ReturnDate { get; set; }

        // Navigation Properties
        public Book Book { get; set; }
        public Borrower Borrower { get; set; }
    }
}
