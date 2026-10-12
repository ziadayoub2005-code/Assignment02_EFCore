using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.Models
{
    internal class Department
    {
        //[Key]
        public int Id { get; set; }
        public string Name { get; set; }

        //NP : Dept has many employees
        public List<Employee> Employees { get; set; }
    }
}
