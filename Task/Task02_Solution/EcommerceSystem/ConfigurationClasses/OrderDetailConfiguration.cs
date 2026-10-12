using EcommerceSystem.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace EcommerceSystem.ConfigurationClasses
{
    public class OrderDetailConfiguration : IEntityTypeConfiguration<OrderDetail>
    {
        public void Configure(EntityTypeBuilder<OrderDetail> builder)
        {
            builder.ToTable("OrderDetails");

            // Composite Primary Key (OrderId, ProductId)
            builder.HasKey(od => new { od.OrderId, od.ProductId });

            builder.Property(od => od.Quantity)
                   .IsRequired()
                   .HasDefaultValue(1);

            // Many-to-Many through OrderDetail:
            // Relationship 1: Order to OrderDetail
            builder.HasOne(od => od.Order)
                   .WithMany(o => o.OrderDetails)
                   .HasForeignKey(od => od.OrderId)
                   .OnDelete(DeleteBehavior.Cascade);

            // Relationship 2: Product to OrderDetail
            builder.HasOne(od => od.Product)
                   .WithMany(p => p.OrderDetails)
                   .HasForeignKey(od => od.ProductId)
                   .OnDelete(DeleteBehavior.Restrict);
        }
    }
}
