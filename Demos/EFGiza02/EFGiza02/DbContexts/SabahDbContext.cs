using EFGiza02.ConfigurationClasses;
using EFGiza02.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.DbContexts
{
    // Class represents a context for the Sabah database 
    // on sql server 
    // act as DbContext ... 
    
    // DbContext !!
    // Component based 
    // Nuget.org 
    // Js : NPM  -- .Net : NPM
    // EFCore.sqlserver
    internal class SabahDbContext : DbContext
    {
        // 2-1 Connect to DB 
        // Connection Data : server , Auth , DB
        // Connection string >> ready 
        // OnConfigure >> as Connection string >> key - value
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Server=.;Database=Sabah;Trusted_Connection=True;");
        }

        // Pa]ractice : 
        // Configuration classes >> DbSet >> Read - Common 

        // 2-2 Model Mapping
        // Collection + EF operations
        public DbSet<Employee> Employees { get; set; }
        public DbSet<Student> Students { get; set; }
        public DbSet<Course> Courses { get; set; }
        public DbSet<StudentCourse> StudentCourses { get; set; }
        // Code_based Mapping : Fluent APi 
        // Configs : Map Models 
        // OnModelCreating

        // level01 

        // Parent/Principal : contain PK
        // Child/Dependent : contain FK

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // Hard delete !!
            // business rules !!
            // Soft delete : 
            // business : flad (indicateors) - (cahnge status)
            // business : make decisiion - business (hard delete after one month !)

            // No Action : default (stop delete parent to child !!)
            // Restrict vs Noction

            // raltionship : MTM
            // PK : 
            modelBuilder.Entity<StudentCourse>()
                .HasKey(SC => new {SC.StdId,SC.CrsID});

            // Course - student Course
            modelBuilder.Entity<Course>()
                .HasMany(C => C.CourseStudents)
                .WithOne(SC => SC.Course)
                .HasForeignKey(SC => SC.CrsID)
                .OnDelete(DeleteBehavior.Restrict);

            // Student - student Course
            modelBuilder.Entity<Student>()
                .HasMany(S => S.StudentCourses)
                .WithOne(SC => SC.Stduent)
                .HasForeignKey(SC => SC.StdId)
                .OnDelete(DeleteBehavior.Restrict);



            // relationship : 
            //modelBuilder.Entity<Employee>()
            //    .HasOne(E => E.Dept)
            //    .WithMany(D => D.Employees)
            //    .HasForeignKey(E => E.DeptId)
            //    .OnDelete(DeleteBehavior.SetNull);

            



            //// table 
            //modelBuilder.Entity<Department>().ToTable("Departments");
            //// Prop Id
            //modelBuilder.Entity<Department>().HasKey(d => d.Id);
            //modelBuilder.Entity<Department>().Property(D => D.Id)
            //    .UseIdentityColumn(10, 10);
            //// Name
            //modelBuilder.Entity<Department>().Property(D => D.Name)
            //    .IsRequired(true)
            //    .HasColumnType("varchar")
            //    .HasColumnName("DeptName")
            //    .HasDefaultValue("Dept")
            //    .HasMaxLength(50);

            // level 02
            // 2019 - EF 3.1 
            // table 
            //modelBuilder.Entity<Department>(D =>
            //{
            //    D.ToTable("Departments");
            //    // Prop Id
            //    D.HasKey(d => d.Id);
            //    D.Property(D => D.Id)
            //        .UseIdentityColumn(10, 10);
            //    // Name
            //    D.Property(D => D.Name)
            //        .IsRequired(true)
            //        .HasColumnType("varchar")
            //        .HasColumnName("DeptName")
            //        .HasDefaultValue("Dept")
            //        .HasMaxLength(50);
            //});

            // level03 
            // modularity 
            // configuration classes !!
            modelBuilder.ApplyConfiguration(new DepartmentConfigurations());
            
            // one Line : Apply Configurations  : self 
        }

        

    }
}
