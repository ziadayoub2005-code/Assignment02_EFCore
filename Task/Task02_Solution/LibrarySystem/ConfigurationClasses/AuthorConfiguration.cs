using LibrarySystem.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace LibrarySystem.ConfigurationClasses
{
    public class AuthorConfiguration : IEntityTypeConfiguration<Author>
    {
        public void Configure(EntityTypeBuilder<Author> builder)
        {
            builder.ToTable("Authors");

            builder.HasKey(a => a.Id);

            builder.Property(a => a.Id)
                   .UseIdentityColumn();

            builder.Property(a => a.Name)
                   .IsRequired()
                   .HasMaxLength(100);

            builder.Property(a => a.BirthDate)
                   .IsRequired();

            // One-to-Many: Author to Book
            builder.HasMany(a => a.Books)
                   .WithOne(b => b.Author)
                   .HasForeignKey(b => b.AuthorId)
                   .OnDelete(DeleteBehavior.Cascade);
        }
    }
}
