using System.Collections.Generic;

namespace EcommerceSystem.Models
{
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
        public int CategoryId { get; set; }

        // Navigation Property: Many Products belong to One Category
        public Category Category { get; set; }

        // Navigation Property: Many-to-Many with Order (via OrderDetail)
        public ICollection<OrderDetail> OrderDetails { get; set; } = new HashSet<OrderDetail>();
    }
}
