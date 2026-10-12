using System;
using System.Linq;
using HealthCareSystem.DbContexts;
using HealthCareSystem.Models;
using Microsoft.EntityFrameworkCore;

namespace HealthCareSystem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("==================================================");
            Console.WriteLine("     Project 3: Health Care System (EF Core 5.0)  ");
            Console.WriteLine("==================================================");

            using var context = new HealthCareDbContext();

            Console.WriteLine("\n[1] Mapped Entities & Relationships:");
            Console.WriteLine(" - Patient (*) <---> (*) Doctor (Many-to-Many through Appointment)");

            Console.WriteLine("\n[2] Key Configurations:");
            Console.WriteLine(" - Composite PK on Appointment: (PatientId, DoctorId, AppointmentDate)");
            Console.WriteLine(" - Foreign Key Properties: PatientId, DoctorId");
            Console.WriteLine(" - Navigation Properties on both ends of the relationship.");

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

            Console.WriteLine("\nHealth Care System configured successfully!");
        }
    }
}
