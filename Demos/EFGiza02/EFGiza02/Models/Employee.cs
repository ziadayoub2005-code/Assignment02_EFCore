using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFGiza02.Models
{
    // Map object : 
    // EF Core : 
    // default mapping / implicit mapping 
    // by convention 
    // 1-Convention_based Mapping

    // 1- Public , numeric , Id / EmployeeId >> PK + identity(1,1)
    // 2- string  > varchar / Char >> nvarchar(max) , allow null 
    // 3- decimal > decimal(18,2)  ,  allow null
    // 4- int > int  >  allow null 

    // Explicit mapping 
    // 2-1 attribute_based Mapping
    // 2-2 Code_based Mapping (Fluent API) [Recommended]


    // 1-Convention_based Mapping
    //internal class Employee
    //{
    //    public int Id { get; set; }
    //    public string Name { get; set; }
    //    public decimal Salary { get; set; }
    //    public int? Age { get; set; }
    //}



    // 2-1 attribute_based Mapping
    // Data annotations : validation + Mapping 
    // attributes >> decorators 
    // flags >> [ definition ] 
    // Direct Map 

    // Convention_based Mapping  +  attribute_based Mapping : Complete
    // Conflict !! => Explicit (attribute_based Mapping)

    // 2-2 Code_based Mapping (Fluent API) [Recommended]
    // why not attribute_based Mapping ?! 
    // 1-advanced Configurations
    // 2-Separation of Concern 
    // 3-Source Code No Access (change in Definition)

    // where ? 
    // DbContext

    // GP : 
    // Fluent API using Configuration class per Entity 


    // More than one Concern 
    // Employee as a model 
    // same time 
    // Mapping Configuration 
    // 1- Radability (Clean Code)
    // 2- Testing 


    [Table("Emps")]
    internal class Employee
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int EId { get; set; }
        [Required]
        [Column(TypeName = "varchar")]
        [StringLength(50)]
        public string Name { get; set; }
        [Column(TypeName = "money")]
        public decimal Salary { get; set; }

        public int? Age { get; set; }

        // explicit Mapping 
        // 0 EF by default : create extra column 
        // 1 represent Extra cloumn ! (Right Congiguration)
        // 2 Data annotation 
        // 3 Configure relationship (Fluent API - Code based)
        //[ForeignKey("Dept")]
        public int? DeptId { get; set; }

        // NP : >> Emp has a Dept
        public Department Dept { get; set; }
    }
}
