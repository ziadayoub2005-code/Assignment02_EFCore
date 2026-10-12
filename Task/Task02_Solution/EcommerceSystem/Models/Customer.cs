using System.Collections.Generic;

namespace EcommerceSystem.Models
{
    public class Customer
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }

        // Navigation Property: One Customer has Many Orders
        public ICollection<Order> Orders { get; set; } = new HashSet<Order>();
    }
}
