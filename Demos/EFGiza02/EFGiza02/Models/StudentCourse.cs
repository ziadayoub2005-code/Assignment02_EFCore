using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.Models
{
    // represent relationship 
    internal class StudentCourse
    {
        // 0 : by default create extra Column 
        // 1 Create extra Column (Fk)
        // 2 Data annotations
        // 3 Configure realtionShip(Fluent API - Code based) - Composite PK

        //[ForeignKey("Stduent")]
        public int? StdId { get; set; }
        //[ForeignKey("Course")]
        public int? CrsID { get; set; }

        // Extra Column 
        public int Grade { get; set; }

        // NP 
        public Student Stduent { get; set; }
        // NP 
        public Course Course { get; set; }
    }
}
