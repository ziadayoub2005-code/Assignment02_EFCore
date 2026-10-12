using Microsoft.EntityFrameworkCore.Query.Internal;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.Models
{
    internal class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int? Age { get; set; }

        // NP 
        // public List<Course> Courses { get; set; }

        // New NP 
        public List<StudentCourse> StudentCourses { get; set; }
    }
}
