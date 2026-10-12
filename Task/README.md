# حل تاسك Entity Framework Core - Part 02 (.NET 5.0)

تم حل جميع متطلبات التاسك بدقة واحترافية وفقاً للتعليمات:
1. **استخدام .NET 5.0 و Entity Framework Core 5.0.17**.
2. **بناء الحل كـ Solution متكامل (`Task02_Solution.sln`)** يحتوي على المشاريع الثلاثة مع تطبيق Fluent API و Configuration Classes و Navigation Properties.
3. **توليد الـ Migrations وملفات الـ SQL DDL Scripts** لكل مشروع.
4. **توليد سكرين شوت احترافي لمخطط قاعدة البيانات (DB Diagram Screenshots)** لكل مشروع داخل مجلد `Screenshots/`.
5. **حل السؤال المقالي (LinkedIn article about Navigation Property)** بشكل شامل وإخراجه كملف PDF عالي الجودة بتنسيق حديث (`Navigation_Property_LinkedIn_Article.pdf`) بالإضافة إلى نسخة Markdown.

---

## 📁 هيكل المجلدات والملفات (Project Structure)

```text
Task/
├── Navigation_Property_LinkedIn_Article.pdf      <-- ملف الـ PDF للسؤال المقالي ومقال لينكد إن
├── Navigation_Property_LinkedIn_Article.md       <-- نسخة الماركداون للمقال
├── Navigation_Property_LinkedIn_Article.html     <-- كود الـ HTML المصمم للـ PDF
├── Part02.pdf                                    <-- ملف التاسك الأصلي
├── README.md                                     <-- هذا الملف التوثيقي
│
├── Screenshots/                                  <-- صور الـ DB Diagrams المطلوبة
│   ├── Ecommerce_DB_Diagram.png
│   ├── Library_DB_Diagram.png
│   └── HealthCare_DB_Diagram.png
│
└── Task02_Solution/                              <-- كود الحل بـ .NET 5.0
    ├── Task02_Solution.sln
    │
    ├── EcommerceSystem/                          <-- مشروع 1: E-commerce System
    │   ├── Models/ (Product, Category, Order, Customer, OrderDetail)
    │   ├── ConfigurationClasses/ (Fluent API لكل Entity)
    │   ├── DbContexts/ (EcommerceDbContext)
    │   ├── Migrations/ (InitialCreate)
    │   ├── EcommerceDb_Script.sql (ملف الـ SQL DDL المولد)
    │   └── Program.cs
    │
    ├── LibrarySystem/                            <-- مشروع 2: Library System
    │   ├── Models/ (Book, Author, Borrower, Loan)
    │   ├── ConfigurationClasses/ (Fluent API لكل Entity)
    │   ├── DbContexts/ (LibraryDbContext)
    │   ├── Migrations/ (InitialCreate)
    │   ├── LibraryDb_Script.sql (ملف الـ SQL DDL المولد)
    │   └── Program.cs
    │
    └── HealthCareSystem/                         <-- مشروع 3: Health Care System
        ├── Models/ (Patient, Doctor, Appointment)
        ├── ConfigurationClasses/ (Fluent API لكل Entity)
        ├── DbContexts/ (HealthCareDbContext)
        ├── Migrations/ (InitialCreate)
        ├── HealthCareDb_Script.sql (ملف الـ SQL DDL المولد)
        └── Program.cs
```

---

## 🛠️ تفاصيل المشاريع وعلاقات الـ Navigation Properties

### 1. Project 1: E-commerce System
* **One-to-Many:** `Category` ↔ `Product`
  * `Category` يحتوي على `ICollection<Product> Products`
  * `Product` يحتوي على `Category Category` و `int CategoryId`
* **One-to-Many:** `Customer` ↔ `Order`
  * `Customer` يحتوي على `ICollection<Order> Orders`
  * `Order` يحتوي على `Customer Customer` و `int CustomerId`
* **Many-to-Many:** `Order` ↔ `Product` عبر جدول وسيط ببيانات إضافية `OrderDetail`:
  * الحقول: `OrderId`, `ProductId`, `Quantity`
  * الـ Composite PK: `(OrderId, ProductId)`
  * علاقات الـ Foreign Key والـ Navigation Properties في الطرفين.

### 2. Project 2: Library System
* **One-to-Many:** `Author` ↔ `Book`
  * `Author` يحتوي على `ICollection<Book> Books`
  * `Book` يحتوي على `Author Author` و `int AuthorId`
* **Many-to-Many:** `Book` ↔ `Borrower` عبر جدول الإعارة `Loan`:
  * الحقول: `BookId`, `BorrowerId`, `LoanDate`, `ReturnDate` (Nullable)
  * الـ Composite PK: `(BookId, BorrowerId)`
  * Navigation Properties كاملة من الطرفين.

### 3. Project 3: Health Care System
* **Many-to-Many:** `Patient` ↔ `Doctor` عبر جدول المواعيد `Appointment`:
  * الحقول: `PatientId`, `DoctorId`, `AppointmentDate`
  * الـ Composite PK: `(PatientId, DoctorId, AppointmentDate)` لإتاحة تكرار المواعيد بين نفس المريض والطبيب في تواريخ مختلفة.

---

## 📄 السؤال المقالي (LinkedIn Article about Navigation Property)

تم إعداد مقال وشرح تفصيلي عالي الجودة داخل ملف:
👉 `Task/Navigation_Property_LinkedIn_Article.pdf`

يتضمن:
1. **بوست لينكد إن جاهز للنشر (Catchy Hook, Emojis, Core Differences, Hashtags).**
2. **الفرق الجوهري بين Foreign Key Property و Navigation Property** (مقارنة تفصيلية وجدول مقارنة).
3. **أنواع الـ Navigation Properties:**
   - Reference Navigation Property (في علاقات 1:1 و N:1).
   - Collection Navigation Property (في علاقات 1:N و M:N ولماذا نستخدم `HashSet<T>`).
4. **طرق تحميل البيانات المرتبطة (Loading Strategies):**
   - Eager Loading (`Include`, `ThenInclude`, والـ Filtered Include في EF Core 5.0).
   - Explicit Loading (`Entry().Reference().Load()`, `Collection().Query().Load()`).
   - Lazy Loading ومخاطر مشكلة **N+1 Query Problem**.
   - Projection (`Select`) وأهميته للـ Performance.
5. **مخططات قواعد البيانات (DB Diagrams) المرفقة لكل نظام.**

---

## 🚀 طريقة تشغيل وبناء الحل (Build & Run)

```bash
# بناء الحل بالكامل (كل المشاريع)
dotnet build Task/Task02_Solution/Task02_Solution.sln

# تشغيل كل مشروع على حدة للتحقق من الموديل والـ Navigation Properties
dotnet run --project Task/Task02_Solution/EcommerceSystem/EcommerceSystem.csproj
dotnet run --project Task/Task02_Solution/LibrarySystem/LibrarySystem.csproj
dotnet run --project Task/Task02_Solution/HealthCareSystem/HealthCareSystem.csproj
```
