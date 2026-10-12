using LibrarySystem.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace LibrarySystem.ConfigurationClasses
{
    public class LoanConfiguration : IEntityTypeConfiguration<Loan>
    {
        public void Configure(EntityTypeBuilder<Loan> builder)
        {
            builder.ToTable("Loans");

            // Composite Primary Key (BookId, BorrowerId)
            builder.HasKey(l => new { l.BookId, l.BorrowerId });

            builder.Property(l => l.LoanDate)
                   .HasDefaultValueSql("GETDATE()")
                   .IsRequired();

            builder.Property(l => l.ReturnDate)
                   .IsRequired(false);

            // Many-to-Many through Loan:
            // Relationship 1: Book to Loan
            builder.HasOne(l => l.Book)
                   .WithMany(b => b.Loans)
                   .HasForeignKey(l => l.BookId)
                   .OnDelete(DeleteBehavior.Cascade);

            // Relationship 2: Borrower to Loan
            builder.HasOne(l => l.Borrower)
                   .WithMany(b => b.Loans)
                   .HasForeignKey(l => l.BorrowerId)
                   .OnDelete(DeleteBehavior.Cascade);
        }
    }
}
