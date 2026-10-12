using System.Collections.Generic;

namespace LibrarySystem.Models
{
    public class Book
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string ISBN { get; set; }
        public int AuthorId { get; set; }

        // Navigation Property: Many Books belong to One Author
        public Author Author { get; set; }

        // Navigation Property: Many-to-Many with Borrower (via Loan)
        public ICollection<Loan> Loans { get; set; } = new HashSet<Loan>();
    }
}
