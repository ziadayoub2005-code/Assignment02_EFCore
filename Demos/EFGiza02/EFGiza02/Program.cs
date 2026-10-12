using EFGiza02.DbContexts;
using EFGiza02.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Linq;

namespace EFGiza02
{
    internal class Program
    {
        static void Main()
        {
            // Map : 
            // Code first 
            // Map from C# to DB >> 

            // step01 : today 
            // 1-object Mapping 

            // step02 : 
            // 2-1 Query object model 
            // 2-2 Maintain relations Navigatio Property 


            // object Mapping : 
            // business / sysytem >> Data Model 
            // ERD >> entities related
            // Classes >> related classes >> Class Diagram
            // business structure >> static structure 

            // Hr system : Employee , Department , ..

            // Classes : represent system > Models / Entities 
            // Modularity : folder 

            // 1-static structure
            // Define Entity classes 

            // 2- Call DB ...
            // class act as DbContext ...
            // DbContext => More than one DB ...
            // 2-1 Connect to DB 
            // Connection Data : server , Auth , DB
            // 2-2 Model Mapping
            // Collection + EF operations

            // 3- Execute Mapping : 
            // Execute to DB - non logic 
            // Migration : 
            // Pkg : commands : EFcore.Tools
            // Packakage Manager Console PMC
            // 1- catch Change >> add-migration
            // 2- Apply Change >> update-database

            //// Migration :
            // Detect change 
            // snapshot 
            // Consistency 
            // Versioning 

            // Change Name To EmpName : 
            // 1- Change only in Migration > InConsistency
            // 2- New Change > new migration [recommended]

            // Change EmpName To Name :
            // 1- execute Down ?
            // command > No 
            // Up (update-datebase to previous migration)
            // revert / rollback / unapply migration / change
            // 2- new migration [recommended]
            // Change EmpName To Name

            // Mig01 : 1,2,3 > Mig02 : 4,5,6 > Mig03 : drop 5

            // remove-migration 
            // Unapply/revert/rollback 


            // Entity framework : 
            // 1- objects Mapping : 3 - Clean - Fluent API(Code) - Clean
            // Configuration class per model/entity (Recommended)
            // 2- query object model (Operations) (CRUD)
            // 3- ORM : Maintain Relations Using EF Core (default - FLuent API)
            // (Association(1:M,1:1,M:M) - Heirarchy - ...)

            // -- Project static Structure --  
            // -- C# Project -- 

            // C# MAnaged Code : 
            // CLR / Runtime : allocate - deallocate resources ..
            // Resources to be managed : Var - method - class - ...
            // resources not managed by CLR : Developer : 
            // 1- DbConnection - Read File - ....
            // u as developer : free/ deallocate  DbConnection !

            // try - finally - using ...
            // 1- Console app
            // 2- DK app 
            // 3- Script app

            // web app : 
            // Design Pattern : Dependency injection 
            // Service Life time - Web request - .. 

            // query object model : 
            // 1- Open Connection Database ..
            //SabahDbContext conext = new SabahDbContext();

            // 2-1 Finally block 
            //try
            //{
            //    // Queries in this connection 
            //    // cintext.Employes.Add() ;
            //}
            //finally
            //{
            //    // free/Deallocate Connection
            //    conext.Dispose();   
            //}

            // 2-2 Syntax sugar
            // USing Block .. 
            //using (SabahDbContext context = new SabahDbContext())
            //{
            //    // Queries in this connection 
            //    // context.Employes.Add() ;
            //}
            // 2-3 Using declare - Syntax sugar 
            using SabahDbContext context = new SabahDbContext();
            // Queries in this connection 
            // context.Employes.Add() ;

            Employee E01 = new Employee { Name = "Ahmed", Age = 25, Salary = 5000 };
            Employee E02 = new Employee { Name = "Ismail", Age = 29, Salary = 9000 };

            // Server in VS 

            // 1-Sh3bala
            // 2-why?
            // EF Change tracker !!
            // Track Chages - states - .. 
            // states for this object 
            // 3-why?
            // Network Performance
            // Minimise Round Trips !
            // 4-Customize
            // 5-diff methods represent model
            // self

            // app(DbContext)   -  database
            // No               -     No       >> detached
            // Yes              -     No       >> Added
            // Modified         -     No       >> Modified
            // deleted          -     No       >> Deleted
            // Yes(Same)        -     Yes(Same)>> Unchanged


            // 2- Query ..
            // CRUD Operation : 
            // 2-1 Create / Add : 
            // -> Add to Local/Cache/app scope
            Console.WriteLine(context.Entry(E02).State); // Detached
            context.Employees.Add(E02); // Added
            Console.WriteLine(context.Entry(E02).State); // Added
            // diff methods EF : 
            //context.Set<Employee>().Add(E02); // Added
            //context.Add(E02); // EF Core 3.1 2019 // syntax sugar // Added
            //context.Entry(E02).State = EntityState.Added;
            // -> Add to DB
            context.SaveChanges();

            Console.WriteLine(context.Entry(E02).State); // Uncahnged

            // EF generate insert : 
            // Context : State (added) : insert statement
            // Context : State (modified) : update statement
            // Context : State (deleted) : delete statement
            // .........

            // Read Data 
            // Emp Name of Id No 01 : 
            //var Emp = context.Employees.Where(E => E.EId == 1)
            //    .FirstOrDefault();
            //var Emp = context.Employees
            //    //.AsNoTracking()
            //    .FirstOrDefault(E => E.EId == 2);

            //Console.WriteLine(Emp?.Name ?? "NA");
            // EF Chjange tracker > Operation on DB 
            // REad Data !!
            // Change tracker : No !! 
            // Read Data > Customise ?

            // Update 
            // update to local :
            //Emp.Name = "Abdo";
            // update to DB :
            //context.SaveChanges();
            // update statement 

            // Delete :
            // delete to local
            //context.Employees.Remove(Emp); // deleted
            // delete to DB
            //context.SaveChanges();
            // delete statement 

            // self : 
            // AsTracking   VS  AsNoTracking : 3 real business cases 
        }

    }
}
