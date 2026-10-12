using LibrarySystem.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace LibrarySystem.ConfigurationClasses
{
    public class BorrowerConfiguration : IEntityTypeConfiguration<Borrower>
    {
        public void Configure(EntityTypeBuilder<Borrower> builder)
        {
            builder.ToTable("Borrowers");

            builder.HasKey(b => b.Id);

            builder.Property(b => b.Id)
                   .UseIdentityColumn();

            builder.Property(b => b.Name)
                   .IsRequired()
                   .HasMaxLength(100);

            builder.Property(b => b.MembershipDate)
                   .HasDefaultValueSql("GETDATE()")
                   .IsRequired();
        }
    }
}
