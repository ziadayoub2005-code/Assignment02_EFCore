using System.Collections.Generic;

namespace HealthCareSystem.Models
{
    public class Doctor
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Specialization { get; set; }

        // Navigation Property: Many-to-Many with Patient (via Appointment)
        public ICollection<Appointment> Appointments { get; set; } = new HashSet<Appointment>();
    }
}
