using System;
using System.Collections.Generic;

namespace EcommerceSystem.Models
{
    public class Order
    {
        public int Id { get; set; }
        public DateTime OrderDate { get; set; }
        public int CustomerId { get; set; }

        // Navigation Property: Many Orders belong to One Customer
        public Customer Customer { get; set; }

        // Navigation Property: Many-to-Many with Product (via OrderDetail)
        public ICollection<OrderDetail> OrderDetails { get; set; } = new HashSet<OrderDetail>();
    }
}
