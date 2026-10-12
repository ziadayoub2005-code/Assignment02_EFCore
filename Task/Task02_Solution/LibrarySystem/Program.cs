using System;
using System.Linq;
using LibrarySystem.DbContexts;
using LibrarySystem.Models;
using Microsoft.EntityFrameworkCore;

namespace LibrarySystem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("==================================================");
            Console.WriteLine("       Project 2: Library System (EF Core 5.0)    ");
            Console.WriteLine("==================================================");

            using var context = new LibraryDbContext();

            Console.WriteLine("\n[1] Mapped Entities & Relationships:");
            Console.WriteLine(" - Author   (1) <---> (*) Book     (One-to-Many)");
            Console.WriteLine(" - Book     (*) <---> (*) Borrower (Many-to-Many through Loan)");

            Console.WriteLine("\n[2] Key Configurations:");
            Console.WriteLine(" - Composite PK on Loan: (BookId, BorrowerId)");
            Console.WriteLine(" - Foreign Key Properties: AuthorId, BookId, BorrowerId");
            Console.WriteLine(" - Navigation Properties on both ends of each relationship.");

            Console.WriteLine("\n[3] Model Validation:");
            var entityTypes = context.Model.GetEntityTypes();
            foreach (var entity in entityTypes)
            {
                Console.WriteLine($"\n Entity: {entity.ClrType.Name}");
                foreach (var nav in entity.GetNavigations())
                {
                    Console.WriteLine($"   -> Navigation Property: {nav.Name} (IsCollection: {nav.IsCollection})");
                }
            }

            Console.WriteLine("\nLibrary System configured successfully!");
        }
    }
}
