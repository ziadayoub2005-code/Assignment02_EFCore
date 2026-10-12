using System.Collections.Generic;

namespace EcommerceSystem.Models
{
    public class Category
    {
        public int Id { get; set; }
        public string Name { get; set; }

        // Navigation Property: One Category has Many Products
        public ICollection<Product> Products { get; set; } = new HashSet<Product>();
    }
}
