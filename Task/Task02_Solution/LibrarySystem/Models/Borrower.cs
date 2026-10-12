using System;
using System.Collections.Generic;

namespace LibrarySystem.Models
{
    public class Borrower
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime MembershipDate { get; set; }

        // Navigation Property: Many-to-Many with Book (via Loan)
        public ICollection<Loan> Loans { get; set; } = new HashSet<Loan>();
    }
}
