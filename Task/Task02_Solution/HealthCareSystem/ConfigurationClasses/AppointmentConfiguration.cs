using HealthCareSystem.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace HealthCareSystem.ConfigurationClasses
{
    public class AppointmentConfiguration : IEntityTypeConfiguration<Appointment>
    {
        public void Configure(EntityTypeBuilder<Appointment> builder)
        {
            builder.ToTable("Appointments");

            // Composite Primary Key (PatientId, DoctorId, AppointmentDate)
            // Includes AppointmentDate to allow repeated appointments between the same patient and doctor
            builder.HasKey(a => new { a.PatientId, a.DoctorId, a.AppointmentDate });

            builder.Property(a => a.AppointmentDate)
                   .IsRequired();

            // Many-to-Many through Appointment:
            // Relationship 1: Patient to Appointment
            builder.HasOne(a => a.Patient)
                   .WithMany(p => p.Appointments)
                   .HasForeignKey(a => a.PatientId)
                   .OnDelete(DeleteBehavior.Cascade);

            // Relationship 2: Doctor to Appointment
            builder.HasOne(a => a.Doctor)
                   .WithMany(d => d.Appointments)
                   .HasForeignKey(a => a.DoctorId)
                   .OnDelete(DeleteBehavior.Cascade);
        }
    }
}
