using LibrarySystem.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace LibrarySystem.ConfigurationClasses
{
    public class BookConfiguration : IEntityTypeConfiguration<Book>
    {
        public void Configure(EntityTypeBuilder<Book> builder)
        {
            builder.ToTable("Books");

            builder.HasKey(b => b.Id);

            builder.Property(b => b.Id)
                   .UseIdentityColumn();

            builder.Property(b => b.Title)
                   .IsRequired()
                   .HasMaxLength(150);

            builder.Property(b => b.ISBN)
                   .IsRequired()
                   .HasMaxLength(20);

            // Many-to-One with Author
            builder.HasOne(b => b.Author)
                   .WithMany(a => a.Books)
                   .HasForeignKey(b => b.AuthorId)
                   .OnDelete(DeleteBehavior.Cascade);
        }
    }
}
