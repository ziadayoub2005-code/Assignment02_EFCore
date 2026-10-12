using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.Models
{
    internal class Course
    {
        public int Id { get; set; }
        public string Name { get; set; }

        // NP 
        // public List<Student> Students { get; set; }

        // New NP 
        public List<StudentCourse> CourseStudents { get; set; }
    }
}
