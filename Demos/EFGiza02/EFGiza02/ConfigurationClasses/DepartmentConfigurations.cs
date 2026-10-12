using EFGiza02.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.ConfigurationClasses
{
    // act as configuration class 
    // Extension
    // Implemnt / inherit 
    internal class DepartmentConfigurations : IEntityTypeConfiguration<Department>
    {
        public void Configure(EntityTypeBuilder<Department> builder)
        {
            // table
            builder.ToTable("Departments");
            // Prop Id
            builder.HasKey(d => d.Id);
            builder.Property(D => D.Id)
                .UseIdentityColumn(10, 10);
            // Name
            builder.Property(D => D.Name)
                .IsRequired(true)
                .HasColumnType("varchar")
                .HasColumnName("DeptName")
                .HasDefaultValue("Dept");

            // relationship 
           builder.HasMany(D => D.Employees)
                .WithOne(E => E.Dept)
                .HasForeignKey(E => E.DeptId)
                .OnDelete(DeleteBehavior.SetNull);
        }
    }
}
