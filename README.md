# Entity Framework Core - Assignment 02 (.NET 5.0)

مستودع حل تكليف اليوم الرابع لمادة **Entity Framework Core (Part 02)**، تم البناء والتطوير بالكامل باستخدام **.NET 5.0** و **EF Core 5.0.17**.

---

## 📌 الفهرس ومحتويات المستودع

1. **[مقال لينكد إن والحل المقالي (PDF)](file:///Users/mac/Desktop/banhaday04/Task/Navigation_Property_LinkedIn_Article.pdf):**
   * ملف PDF منسق وشامل بعنوان: **"Demystifying Navigation Properties in EF Core"**.
   * يتضمن بوست لينكد إن جاهز للنشر، شرح نظري معماري متقدم، المقارنة بين Foreign Key و Navigation Property، أنواع العلاقات واستراتيجيات الـ Loading (Eager, Explicit, Lazy, Projection)، وأهم الـ Best Practices.
   * يتوفر أيضاً كملف ماركداون: [Navigation_Property_LinkedIn_Article.md](file:///Users/mac/Desktop/banhaday04/Task/Navigation_Property_LinkedIn_Article.md).

2. **[المشاريع البرمجية (.NET 5.0 Solution)](file:///Users/mac/Desktop/banhaday04/Task/Task02_Solution/Task02_Solution.sln):**
   * **Project 1 (E-commerce System):**
     * Models: `Category`, `Product`, `Customer`, `Order`, `OrderDetail`.
     * علاقات 1:M و M:M (مع جدول وسيط يحمل حقل `Quantity` ومفتاح مركب `OrderId, ProductId`).
     * [EcommerceDb_Script.sql](file:///Users/mac/Desktop/banhaday04/Task/Task02_Solution/EcommerceSystem/EcommerceDb_Script.sql).
   * **Project 2 (Library System):**
     * Models: `Author`, `Book`, `Borrower`, `Loan`.
     * علاقات 1:M و M:M (مع جدول وسيط يحمل `LoanDate`, `ReturnDate` ومفتاح مركب `BookId, BorrowerId`).
     * [LibraryDb_Script.sql](file:///Users/mac/Desktop/banhaday04/Task/Task02_Solution/LibrarySystem/LibraryDb_Script.sql).
   * **Project 3 (Health Care System):**
     * Models: `Patient`, `Doctor`, `Appointment`.
     * علاقات M:M (مع جدول وسيط يحمل `AppointmentDate` ومفتاح مركب `PatientId, DoctorId, AppointmentDate`).
     * [HealthCareDb_Script.sql](file:///Users/mac/Desktop/banhaday04/Task/Task02_Solution/HealthCareSystem/HealthCareDb_Script.sql).

3. **[مخططات قواعد البيانات (Database Diagrams)](file:///Users/mac/Desktop/banhaday04/Task/Screenshots/):**
   * 🖼️ [E-commerce DB Diagram](file:///Users/mac/Desktop/banhaday04/Task/Screenshots/Ecommerce_DB_Diagram.png)
   * 🖼️ [Library DB Diagram](file:///Users/mac/Desktop/banhaday04/Task/Screenshots/Library_DB_Diagram.png)
   * 🖼️ [Health Care DB Diagram](file:///Users/mac/Desktop/banhaday04/Task/Screenshots/HealthCare_DB_Diagram.png)

4. **[مجلد المحاضرة والتطبيقات (Demos)](file:///Users/mac/Desktop/banhaday04/Demos/):**
   * يحتوي على كود محاضرة اليوم الرابع `EFGiza02` والرسومات التوضيحية للشرح.

---

## 🛠️ تقنيات المشروع (Technologies Used)
* **Framework:** .NET 5.0 (C# 9.0)
* **ORM:** Microsoft.EntityFrameworkCore 5.0.17
* **Database Provider:** Microsoft.EntityFrameworkCore.SqlServer 5.0.17
* **Tooling:** Microsoft.EntityFrameworkCore.Tools 5.0.17 & `dotnet-ef` CLI
* **Design Pattern:** Code-First Approach using Fluent API (`IEntityTypeConfiguration<T>`)

---

## 🚀 تشغيل وبناء المشاريع (How to Build & Run)

```bash
# استعادة الحزم وبناء الـ Solution بالكامل
dotnet restore Task/Task02_Solution/Task02_Solution.sln
dotnet build Task/Task02_Solution/Task02_Solution.sln

# تشغيل المشاريع الفردية
dotnet run --project Task/Task02_Solution/EcommerceSystem/EcommerceSystem.csproj
dotnet run --project Task/Task02_Solution/LibrarySystem/LibrarySystem.csproj
dotnet run --project Task/Task02_Solution/HealthCareSystem/HealthCareSystem.csproj
```
