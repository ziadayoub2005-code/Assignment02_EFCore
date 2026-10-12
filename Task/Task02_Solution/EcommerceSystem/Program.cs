using System;
using System.Linq;
using EcommerceSystem.DbContexts;
using EcommerceSystem.Models;
using Microsoft.EntityFrameworkCore;

namespace EcommerceSystem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("==================================================");
            Console.WriteLine("      Project 1: E-commerce System (EF Core 5.0)   ");
            Console.WriteLine("==================================================");

            using var context = new EcommerceDbContext();

            Console.WriteLine("\n[1] Mapped Entities & Relationships:");
            Console.WriteLine(" - Category (1) <---> (*) Product (One-to-Many)");
            Console.WriteLine(" - Customer (1) <---> (*) Order   (One-to-Many)");
            Console.WriteLine(" - Order    (*) <---> (*) Product (Many-to-Many through OrderDetail)");

            Console.WriteLine("\n[2] Key Configurations:");
            Console.WriteLine(" - Composite PK on OrderDetail: (OrderId, ProductId)");
            Console.WriteLine(" - Foreign Key Properties: CategoryId, CustomerId, OrderId, ProductId");
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

            Console.WriteLine("\nE-commerce System configured successfully!");
        }
    }
}
